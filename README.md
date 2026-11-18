# GRC Fintech Portfolio

A hands-on Governance, Risk & Compliance (GRC) portfolio built around a **fictional** fintech company, *Meridian Pay*, a payments and consumer-credit platform operating in Latin America.

> Meridian Pay is invented for this portfolio. Any resemblance to a real company is coincidental. No real company data is used.

## Purpose

Show, with working artifacts, how a security compliance program is designed, measured and maintained:

- Policies written for a real operating context, not copied templates.
- A quantified risk register with a repeatable scoring method.
- A single control library mapped across **NIST CSF 2.0**, **ISO/IEC 27001:2022 (Annex A)** and **SOC 2 (Trust Services Criteria)**.
- Automated control testing against a cloud account (compliance as code).
- An audit-style gap analysis and a third-party risk process.

## Projects

| # | Project | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 00 | [Company profile](00-company-profile/) | Scoping: what is being protected and why | Not started |
| 01 | [Security policies](01-policies/) | Governance: writing enforceable policy | Not started |
| 02 | [Risk register](02-risk-register/) | Risk assessment, scoring, heatmap | Not started |
| 03 | [Control mapping (crosswalk)](03-control-mapping/) | Framework fluency, gap detection | Not started |
| 04 | [Compliance as code](04-compliance-as-code/) | Automated control testing on AWS | Not started |
| 05 | [Gap analysis report](05-gap-analysis/) | Audit-readiness reporting | Not started |
| 06 | [Vendor risk](06-vendor-risk/) | Third-party risk management | Not started |

Progress is tracked in [PROGRESS.md](PROGRESS.md).

## Skills demonstrated

Risk assessment · Policy writing · Control design · Framework mapping (NIST CSF, ISO 27001, SOC 2) · Gap analysis · Evidence collection · Third-party risk · Python automation · Git/GitHub workflow

## Repository conventions

- Documents are written in Markdown, data in CSV/YAML.
- Every control references the framework IDs it satisfies.
- No credentials or real personal data are ever committed (see `.gitignore`).
