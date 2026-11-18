# 06 · Vendor Risk (Third-Party Risk Management)

Most breaches involve a supplier somewhere. This project defines how Meridian Pay decides which vendors are risky and what it asks of them.

## Files to produce
- `vendor-tiering.md`: criteria to classify vendors as Critical / Important / Low (data access, system criticality, replaceability).
- `vendor-questionnaire.md`: 25-30 security questions grouped by domain (access, encryption, incident handling, subprocessors, certifications).
- `vendor-assessment.csv`: 5 fictional vendors scored with the questionnaire.
- `score_vendors.py`: reads the CSV and ranks vendors by residual risk.

## Deliverables
- [ ] Tiering criteria
- [ ] Questionnaire
- [ ] 5 vendors assessed and ranked
- [ ] Recommendation per vendor: approve / approve with conditions / reject
- [ ] Link the process to control MP-VM-01
