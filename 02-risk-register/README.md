# 02 · Risk Register

A risk register lists what could go wrong, how likely and how damaging it would be, and what the company decides to do about it.

## Method
- **Likelihood** (1-5): 1 = rare, 5 = almost certain within 12 months.
- **Impact** (1-5): 1 = negligible, 5 = severe (regulatory action, major financial loss, loss of customer trust).
- **Score** = Likelihood × Impact (1-25).
- **Rating:** 1-4 Low · 5-9 Medium · 10-16 High · 17-25 Critical.
- **Treatment options:** Mitigate, Accept, Transfer, Avoid.

## Files
- `risk_register.csv`: the register (target: 15-20 risks).
- `heatmap.py`: reads the CSV, prints a ranked summary and generates `heatmap.png`.

## Run
```bash
pip install -r requirements.txt
python heatmap.py
```

## Deliverables
- [ ] 15+ risks covering access, data, cloud, third parties, people, availability, fraud
- [ ] Every risk has an owner and a treatment
- [ ] `heatmap.png` committed
- [ ] Short summary of the top 5 risks added below

## Top risks summary
_To be written once the register is complete._
