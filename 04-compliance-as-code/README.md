# 04 · Compliance as Code

Instead of checking cloud settings by hand, run an open-source scanner that tests them against a benchmark and produces evidence automatically.

## Tool
[Prowler](https://github.com/prowler-cloud/prowler), an open-source cloud security tool that checks AWS accounts against frameworks such as CIS, and can report against ISO 27001 and SOC 2 mappings. Check its documentation for the current install steps and supported framework names before running.

## Safety rules (read first)
- Use a **free-tier, dedicated AWS account** with nothing real in it.
- Create a **read-only IAM user** for the scan (the `SecurityAudit` and `ViewOnlyAccess` managed policies).
- **Never commit** access keys, raw scan output or account IDs. `.gitignore` already blocks `prowler-output/raw/`.
- Set a billing alert before you start.

## Workflow
1. Create the AWS account and read-only user.
2. Install and configure Prowler locally.
3. Run a scan against a CIS benchmark.
4. Save a **sanitized** summary (counts by severity, no account IDs) in `results/summary.md`.
5. Pick 5 failed checks and map each one to a control in `../03-control-mapping/controls.csv`.
6. Write a remediation note for each of the 5.

## Deliverables
- [ ] `results/summary.md` with sanitized findings
- [ ] 5 findings mapped to internal controls, each with severity, risk and fix
- [ ] Before/after: fix at least one finding and re-scan
