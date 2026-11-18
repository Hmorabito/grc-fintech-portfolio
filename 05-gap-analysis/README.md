# 05 · Gap Analysis Report (SOC 2 readiness style)

An auditor-style report: where does Meridian Pay stand against SOC 2 Security criteria today, and what must change before an audit?

## Inputs
- `../03-control-mapping/controls.csv`
- `../02-risk-register/risk_register.csv`
- `../04-compliance-as-code/results/summary.md`

## Report structure (`gap-analysis-report.md`)
1. Executive summary (half a page, written for a CEO)
2. Scope and method
3. Results by criteria area (Common Criteria CC1-CC9)
4. Findings table: ID, description, severity, affected control, recommendation, owner, target date
5. Remediation roadmap (30 / 60 / 90 days)
6. Evidence request list (what an auditor would ask for)

## Deliverables
- [ ] `gap-analysis-report.md`
- [ ] `evidence-request-list.csv`
- [ ] Findings traceable back to the control library and risk register
