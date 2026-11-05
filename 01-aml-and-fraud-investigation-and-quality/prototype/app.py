#!/usr/bin/env python3
"""Local, rules-based AML and fraud investigation demonstration. Synthetic data only."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import json, html

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sample-data"
CASES = {
    "aml": DATA / "aml-case.json",
    "fraud": DATA / "fraud-case.json",
    "qa": DATA / "quality-failure-case.json",
}
def load(key):
    with CASES[key].open(encoding="utf-8") as f:
        return json.load(f)
def money(n):
    return f"AUD {n:,.2f}"
def analyse(case):
    tx = case.get("transactions", [])
    incoming = sum(x["amount_aud"] for x in tx if x["direction"] == "IN")
    outgoing = sum(x["amount_aud"] for x in tx if x["direction"] == "OUT")
    checks = case.get("quality_checks", {})
    failed = [k for k,v in checks.items() if not v]
    return {"incoming":incoming,"outgoing":outgoing,"net":incoming-outgoing,
            "transaction_count":len(tx),"failed_checks":failed}
def esc(x):
    return html.escape(str(x))
def list_html(items):
    return "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>" if items else "<p>None recorded.</p>"
def render(key):
    c = load(key); a = analyse(c)
    options = [("aml","AML example"),("fraud","Fraud example"),("qa","Incomplete case — QA challenge")]
    nav = " ".join(f'<a class="tab {"active" if k==key else ""}" href="/?case={k}">{label}</a>' for k,label in options)
    txrows = "".join(f"<tr><td>{esc(t['date'])}</td><td>{esc(t['direction'])}</td><td>{esc(t['counterparty'])}</td><td>{money(t['amount_aud'])}</td><td>{esc(t['source_id'])}</td></tr>" for t in c["transactions"])
    facts = "".join(f"<li>{esc(x['text'])} <small>Source: {esc(x['source'])}</small></li>" for x in c.get("recorded_facts",[]))
    statements = "".join(f"<li>{esc(x['text'])} <small>Source: {esc(x['source'])} · {esc(x.get('verification_status',''))}</small></li>" for x in c.get("customer_statements",[]))
    checks = "".join(f"<tr><td>{esc(k.replace('_',' ').capitalize())}</td><td><span class='{"pass" if v else "fail"}'>{'Addressed in supplied case' if v else 'Gap flagged'}</span></td></tr>" for k,v in c.get("quality_checks",{}).items())
    prompts = (["Establish who made each incoming payment and the relationship to the customer.",
                "Assess the source of funds and the purpose of the incoming and outgoing payments.",
                "Test the personal-loan explanation against proportionate supporting information."]
               if c["case_type"]=="AML" else
               ["Establish the caller's identity and the reported method of contact.",
                "Distinguish payment authentication from whether the customer was deceived.",
                "Establish beneficiary details, onward movement and recovery enquiries."])
    if key=="qa":
        prompts = ["Challenge the unsupported conclusion.",
                   "Identify the missing payer, recipient and transaction purpose information.",
                   "Require supporting evidence and a revised reasoned case position."]
    data = json.dumps({"case_id":c["case_id"],"case_type":c["case_type"],"analysis":a,
                       "provisional_position":c["provisional_position"],"quality_checks":c["quality_checks"]},indent=2)
    return f"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Investigation and Quality Demonstrator</title><style>
:root{{--ink:#172b4d;--muted:#5e6c84;--line:#dfe3e8;--blue:#155eef;--bg:#f6f8fb}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 Arial,sans-serif}}
header{{background:#102a43;color:white;padding:24px max(22px,calc((100% - 1120px)/2))}}header h1{{margin:0 0 5px;font-size:25px}}header p{{margin:0;color:#d9e5f2}}
main{{max-width:1120px;margin:22px auto;padding:0 18px}}.notice{{background:#fff8e6;border:1px solid #f0d58c;padding:12px 15px;border-radius:8px;margin-bottom:16px}}
nav{{display:flex;gap:8px;flex-wrap:wrap;margin:15px 0}}.tab{{padding:9px 13px;background:white;border:1px solid var(--line);border-radius:7px;color:var(--ink);text-decoration:none}}.active{{background:#eaf1ff;border-color:#91b4ff;color:#174ea6;font-weight:bold}}
.card{{background:white;border:1px solid var(--line);border-radius:10px;padding:18px;margin:14px 0}}h2{{font-size:19px;margin:0 0 12px}}h3{{font-size:16px;margin:14px 0 6px}}.muted,small{{color:var(--muted)}}.metrics{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}.metric{{background:#f7f9fc;padding:13px;border-radius:8px}}.metric b{{display:block;font-size:19px;margin-top:4px}}
table{{width:100%;border-collapse:collapse;font-size:14px}}th,td{{text-align:left;padding:9px;border-bottom:1px solid var(--line);vertical-align:top}}th{{background:#f7f9fc}}.scroll{{overflow-x:auto}}.pass,.fail{{font-weight:bold}}.pass{{color:#16794b}}.fail{{color:#b42318}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}a.button{{display:inline-block;background:var(--blue);color:white;padding:10px 14px;border-radius:7px;text-decoration:none}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#f4f6f8;padding:14px;border-radius:7px;font-size:13px}}
footer{{color:var(--muted);font-size:13px;padding:15px 0 30px}}@media(max-width:700px){{.metrics{{grid-template-columns:1fr 1fr}}.grid{{grid-template-columns:1fr}}}}
</style></head><body><header><h1>Investigation & Quality Demonstrator</h1><p>Business-led workflow prototype · Synthetic cases · Predefined rules only</p></header>
<main><div class="notice"><b>Demonstration only:</b> This is not an AI model and must not be used for real customer or bank decisions. Unusual activity is not proof of wrongdoing. Human judgement remains essential.</div>
<nav>{nav}</nav>
<section class="card"><h2>{esc(c['title'])}</h2><p class="muted">{esc(c['case_id'])} · {esc(c['case_type'])} · {esc(c['review_period'])}</p><p>{esc(c['case_summary'])}</p><div class="metrics">
<div class="metric">Incoming payments<b>{money(a['incoming'])}</b></div><div class="metric">Outgoing payments<b>{money(a['outgoing'])}</b></div><div class="metric">Net movement<b>{money(a['net'])}</b></div><div class="metric">Transactions<b>{a['transaction_count']}</b></div></div></section>
<section class="card"><h2>Transaction information</h2><div class="scroll"><table><thead><tr><th>Date</th><th>Direction</th><th>Payment party</th><th>Amount</th><th>Reference</th></tr></thead><tbody>{txrows}</tbody></table></div></section>
<div class="grid"><section class="card"><h2>Recorded facts</h2><ul>{facts}</ul><h3>Customer statements</h3><ul>{statements}</ul></section>
<section class="card"><h2>What still needs to be established</h2>{list_html(c.get('unknowns',[]))}<h3>Suggested next enquiries</h3>{list_html(c.get('next_enquiries',[]))}</section></div>
<section class="card"><h2>Investigation prompts</h2>{list_html(prompts)}<h3>Provisional case position recorded in sample</h3><p>{esc(c['provisional_position'])}</p><small>This is the position written into the synthetic case data, not a decision made by the application.</small></section>
<section class="card"><h2>Independent quality checklist</h2><p class="muted">The application checks whether supplied checklist fields are marked complete. A flag is a prompt for reviewer judgement, not a final quality finding.</p><div class="scroll"><table><thead><tr><th>Review area</th><th>Supplied case status</th></tr></thead><tbody>{checks}</tbody></table></div><p><b>Items flagged:</b> {len(a['failed_checks'])}</p></section>
<section class="card"><h2>Management themes across sample cases</h2><p class="muted">This small, deliberately selected sample is not representative and is not a bank performance measure.</p><ul><li>Counterparty information and relationships</li><li>Source and purpose of funds</li><li>Testing customer explanations</li><li>Evidence support for conclusions</li><li>Fraud chronology, fund movement and recovery information</li></ul><small>These are themes in the supplied synthetic examples, not measured industry trends.</small></section>
<section class="card"><h2>Export this case snapshot</h2><p>Download the selected case's basic calculation and supplied quality checklist as JSON.</p><a class="button" href="/export?case={key}">Download case review (JSON)</a></section>
<footer>Local demonstration only · No external network calls · No database · No AI model · No real customer data</footer></main></body></html>"""
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed=urlparse(self.path); q=parse_qs(parsed.query)
        key=q.get("case",["aml"])[0]
        if key not in CASES: key="aml"
        if parsed.path=="/export":
            c=load(key); a=analyse(c)
            payload={"case_id":c["case_id"],"case_type":c["case_type"],"transaction_analysis":a,
                     "provisional_position_from_sample":c["provisional_position"],
                     "notice":"Synthetic demonstration only. Rules-based, not AI. Not a bank decision."}
            raw=json.dumps(payload,indent=2).encode()
            self.send_response(200); self.send_header("Content-Type","application/json")
            self.send_header("Content-Disposition",f'attachment; filename="{c["case_id"].lower()}-review.json"')
            self.send_header("Content-Length",str(len(raw))); self.end_headers(); self.wfile.write(raw); return
        body=render(key).encode()
        self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8")
        self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
    def log_message(self,fmt,*args):
        pass
if __name__=="__main__":
    print("Open http://127.0.0.1:8000 in your browser. Press Ctrl+C to stop.")
    HTTPServer(("127.0.0.1",8000),Handler).serve_forever()
