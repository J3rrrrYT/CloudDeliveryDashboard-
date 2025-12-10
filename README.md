# Cloud Delivery & Project Risk Dashboard

This project simulates a portfolio of consulting projects and shows how a Project Manager can monitor **delivery health** and **risk** using data.

It combines:

- **Python (pandas)** – to calculate KPIs per project  
- **Tableau** – to build an interactive delivery dashboard  
- **CSV data** – simple project and issue datasets  

The goal is to demonstrate how a Consulting Project Manager can:
- Track issues and severity across projects  
- Identify at-risk engagements with a calculated `risk_score`  
- Give stakeholders a clear view of project health

---

## 📁 Repository Structure

```text
CloudDeliveryDashboard/
│
├── README.md
├── data/
│   ├── projects.csv        # project list (name, customer, dates, status)
│   ├── issues.csv          # issues with severity, category, status
│   └── usage.csv           # (optional) progress/usage over time
│
├── python/
│   └── analyze_projects.py # Python script to build project KPIs & risk_score
│
└── tableau/
    └── delivery_dashboard.twbx   # Tableau dashboard file
