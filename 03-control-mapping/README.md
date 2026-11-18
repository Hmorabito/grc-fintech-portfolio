# 03 · Control Mapping (Crosswalk)

One internal control library, mapped to three frameworks. This shows that a single well-designed control can satisfy several audits at once, and exposes where coverage is missing.

## Frameworks used
- **NIST CSF 2.0**: six functions: Govern, Identify, Protect, Detect, Respond, Recover.
- **ISO/IEC 27001:2022**: Annex A, 93 controls in four themes (Organizational, People, Physical, Technological).
- **SOC 2**: Trust Services Criteria (Security/Common Criteria, Availability, Processing Integrity, Confidentiality, Privacy).

## Files
- `controls.csv`: the control library (target: 30 controls).
- `gap_check.py`: reports missing mappings, owners, evidence and coverage by framework.

## Columns
| Column | Meaning |
|--------|---------|
| control_id | Internal ID, e.g. MP-AC-01 |
| control_name | Short name |
| description | What the control requires |
| nist_csf | NIST CSF 2.0 subcategory IDs (separate several with `;`) |
| iso_27001 | Annex A references |
| soc2 | TSC references |
| owner | Responsible role |
| status | Implemented / Partial / Planned / Not implemented |
| evidence | What proves it works (screenshot, config export, ticket, report) |

## Run
```bash
python gap_check.py
```

## Deliverables
- [ ] 30 controls covering access, change, logging, incident, vendor, data, continuity, people
- [ ] Every control mapped to at least one reference in each framework (or an explicit "N/A" with reason)
- [ ] `gap_check.py` output pasted into the "Findings" section below

## Findings
_To be written after running the gap check._
