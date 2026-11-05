from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json, html

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sample-data"

CASES = {
    "aml": ("AML — Harbourline Bank synthetic case", DATA / "aml-case.json"),
    "fraud": ("Fraud — synthetic payment scam case", DATA / "fraud-case.json"),
    "qa": ("Quality failure — deliberately incomplete synthetic case", DATA / "quality-failure-case.json"),
}

def load_case(key):
    label, path = CASES.get(key, CASES["aml"])
    return label, json.loads(path.read_text(encoding="utf-8"))

def analyse(case):
    tx = case.get("transactions", [])
    incoming = sum(t["amount_aud"] for t in tx if t.get("direction") == "incoming")
    outgoing = sum(t["amount_aud"] for t in tx if t.get("direction") == "outgoing")
    summary = {
        "transaction_count": len(tx),
        "incoming_aud": incoming,
        "outgoing_aud": outgoing,
        "net_inflow_aud": incoming - outgoing,
    }
    if case.get("pathway") == "AML":
        prompts = [
            "Who are the counterparties and what is their relationship with the customer?",
            "What is the source and purpose of incoming funds?",
            "What is the purpose and destination of outgoing funds?",
            "Is the activity consistent with the customer's known profile and expected activity?",
            "Has the customer explanation been corroborated by independent evidence?"
        ]
    else:
        prompts = [
            "What is the reported event chronology and how is each step evidenced?",
            "What did the customer understand and authorise at the time of payment?",
            "Who controls the beneficiary account and what is the relationship to the customer?",
            "What communications or independent evidence support or contradict the reported scam?",
            "What happened to the funds after receipt, if that information is lawfully available?"
        ]
    gaps = case.get("evidence_missing_or_unverified", case.get("known_gaps", []))
    return summary, prompts, gaps

def quality_review(case):
    record = case.get("investigation_record", {})
    checks = []
    checks.append(("Investigation summary", bool(record.get("summary")) and "complete" not in record.get("summary","").lower()))
    checks.append(("Counterparty analysis", record.get("counterparty_analysis") not in (None, "", "Not completed.")))
    checks.append(("Source/purpose assessment", record.get("source_of_funds") not in (None, "", "Not assessed.")))
    checks.append(("Customer explanation assessed", record.get("customer_explanation") not in (None, "", "Not obtained.")))
    checks.append(("Evidence references recorded", bool(record.get("evidence_references"))))
    checks.append(("Further enquiries documented", record.get("further_enquiries") not in (None, "", "None recorded.")))
    conclusion = record.get("conclusion", "")
    checks.append(("Conclusion appropriately qualified", not any(w in conclusion.lower() for w in ["is involved", "guilty", "committed"]) if conclusion else False))
    return [{"criterion": n, "result": "Review required" if ok else "Gap identified"} for n, ok in checks]

def page(key="aml"):
    label, case = load_case(key)
    summary, prompts, gaps = analyse(case)
    qa = quality_review(case) if key == "qa" else []
    esc = lambda x: html.escape(str(x))
    txrows = "".join(
        f"<tr><td>{esc(t.get('id'))}</td><td>{esc(t.get('date'))}</td><td>{esc(t.get('direction'))}</td><td>${t.get('amount_aud',0):,.2f}</td><td>{esc(t.get('counterparty',t.get('beneficiary','—')))}</td></tr>"
        for t in case.get("transactions", [])
    )
    prompt_html = "".join(f"<li>{esc(p)}</li>" for p in prompts)
    gap_html = "".join(f"<li>{esc(g)}</li>" for g in gaps) or "<li>No gaps supplied in this case file.</li>"
    qa_html = "".join(f"<tr><td>{esc(x['criterion'])}</td><td>{esc(x['result'])}</td></tr>" for x in qa)
    customer = case.get("customer", {})
    customer_html = "".join(f"<li><b>{esc(k.replace('_',' ').title())}:</b> {esc(v)}</li>" for k,v in customer.items())
    options = "".join(f'<option value="{k}" {"selected" if k==key else ""}>{esc(v[0])}</option>' for k,v in CASES.items())
    report = {"case_id":case.get("case_id"),"pathway":case.get("pathway"),"transaction_summary":summary,"investigative_prompts":prompts,"evidence_gaps":gaps,"quality_review":qa}
    report_json = html.escape(json.dumps(report, indent=2))
    return f"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>AML & Fraud Investigation Demonstrator</title>
<style>
body{{font-family:Arial,sans-serif;max-width:1050px;margin:32px auto;padding:0 18px;color:#172033;line-height:1.5;background:#f7f8fa}}
h1{{font-size:28px}} h2{{font-size:19px;margin-top:28px}} .sub{{color:#536174}}
.card{{background:white;border:1px solid #dce1e8;border-radius:10px;padding:18px;margin:14px 0}}
.notice{{background:#fff7df;border:1px solid #ead38a;padding:12px;border-radius:8px}}
.metrics{{display:flex;gap:12px;flex-wrap:wrap}} .metric{{background:#f0f4fa;padding:12px;border-radius:8px;min-width:150px}}
.metric b{{display:block;font-size:21px}} table{{width:100%;border-collapse:collapse}} td,th{{padding:9px;border-bottom:1px solid #e4e8ee;text-align:left}}
select,button{{padding:10px;border:1px solid #aab5c4;border-radius:6px;font-size:15px}} button{{background:#1d4ed8;color:white;border:0;cursor:pointer}}
code,pre{{white-space:pre-wrap;overflow-wrap:anywhere}} footer{{color:#637083;font-size:13px;margin:28px 0}}
</style></head><body>
<h1>Intelligent AML & Fraud Investigation and Quality Assurance</h1>
<p class="sub">Local synthetic-data workflow demonstrator · Rules-based prototype · No external services</p>
<div class="notice"><b>Demonstration only:</b> This prototype does not make AML, fraud, customer, account, reimbursement or regulatory decisions. All sample data is fictional. Human assessment is required.</div>
<div class="card"><form method="get"><label for="case"><b>Select a synthetic case</b></label><br><br><select id="case" name="case">{options}</select> <button type="submit">Load case</button></form></div>
<h2>Case overview</h2><div class="card"><b>{esc(label)}</b><ul>{customer_html}</ul><p><b>Case ID:</b> {esc(case.get("case_id"))} · <b>Pathway:</b> {esc(case.get("pathway"))}</p></div>
<h2>Transaction summary</h2><div class="metrics">
<div class="metric">Transactions<b>{summary['transaction_count']}</b></div>
<div class="metric">Incoming<b>${summary['incoming_aud']:,.2f}</b></div>
<div class="metric">Outgoing<b>${summary['outgoing_aud']:,.2f}</b></div>
<div class="metric">Net inflow<b>${summary['net_inflow_aud']:,.2f}</b></div></div>
<div class="card"><table><thead><tr><th>ID</th><th>Date</th><th>Direction</th><th>Amount</th><th>Counterparty / beneficiary</th></tr></thead><tbody>{txrows}</tbody></table></div>
<h2>Investigation prompts</h2><div class="card"><ol>{prompt_html}</ol><p class="sub">These are prompts for an investigator, not findings of wrongdoing.</p></div>
<h2>Evidence gaps / unverified information</h2><div class="card"><ul>{gap_html}</ul></div>
<h2>Independent quality review</h2><div class="card">
<p>The deliberately incomplete QA case is designed to demonstrate checklist challenge. For other cases, use the separate checklist document and assess the actual investigation record.</p>
{"<table><thead><tr><th>Criterion</th><th>Prototype result</th></tr></thead><tbody>"+qa_html+"</tbody></table>" if qa else "<p>Select the quality failure case to run the sample checklist review.</p>"}
</div>
<h2>Export demonstration report</h2><div class="card"><button onclick="downloadReport()">Download JSON report</button><script type="application/json" id="report">{report_json}</script><script>
function downloadReport(){{const raw=document.getElementById('report').textContent;const blob=new Blob([raw],{{type:'application/json'}});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='case-demonstration-report.json';a.click();URL.revokeObjectURL(a.href);}}
</script></div>
<footer>Portfolio prototype. Deterministic rules and checklist logic only; no AI model, production controls or external integrations.</footer>
</body></html>"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        key = parse_qs(urlparse(self.path).query).get("case", ["aml"])[0]
        if key not in CASES: key = "aml"
        body = page(key).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))

if __name__ == "__main__":
    print("Open http://127.0.0.1:8000 in your browser. Press Ctrl+C to stop.")
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
