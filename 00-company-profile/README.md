# 00 · Company Profile: Meridian Pay (fictional)

Every compliance program starts with scope: what does the company do, what data does it hold, and which rules apply to it. Fill in each section briefly (2-5 lines).

## Business overview
- What Meridian Pay does: Helps merchants collect payments and lets individuals pay and finance their purchases.
- Customers (consumers / merchants / both): individuals and merchants.
- Countries of operation: Venezuela, Colombia, Peru, Chile, Argentina and Mexico.
- Headcount (approx.): About 150 employees.


## Data it handles
- Personal data (names, IDs, contact info): Full names, national ID numbers, dates of birth, home addresses, phone numbers and emails of individual customers; legal names, tax IDs and contact details of merchants.
- Financial data (payment instructions, credit history): Payment transactions, bank account statements, tokenized card numbers, credit applications and scores, loan balances and repayment history, merchant settlement records.
- Authentication data (passwords, tokens): Hashed passwords, PINs, one-time codes, merchant API keys and session tokens.
- Where it is stored (cloud provider, databases, SaaS tools): AWS (cloud), PostgreSQL on Amazon RDS (customer and transaction database), Amazon S3 (document uploads and backups), Google Workspace (email), Salesforce (CRM).

## Key systems
| System | Purpose | Hosted on | Business criticality (High/Med/Low) |
|--------|---------|-----------|-------------------------------------|
| Mobile app backend |Serves the customer app: sign-up, login, balances | AWS | High |
| Payments API |Processes payments and merchant settlements  | AWS | High |
| Customer database |Stores customer, credit and transaction records| AWS |High|
| Credit scoring engine | Evaluates loan applications | AWS | Medium |
| Internal tools (email, HR, CRM) |Day-to-day operations | SaaS |Medium|

## Applicable obligations
- Frameworks: PCI DSS (first priority), because Meridian Pay handles tokenized card numbers and processes card payments.
- Local regulation: Ley 25.326, because Meridian Pay handles full names and national ID numbers of customers in Argentina.
- Contractual requirements: card networks (Visa, Mastercard) and payment processors require PCI DSS compliance; large merchants may require proof of security (such as a SOC 2 report) before signing.

## Out of scope
Anything intentionally excluded and why.
