import pandas as pd

# Load CSV files (change path if needed)
projects = pd.read_csv("projects.csv")
issues = pd.read_csv("issues.csv")

# 1. Number of issues per project
issues_per_project = (
    issues.groupby("project_id")
    .agg(total_issues=("issue_id", "count"))
    .reset_index()
)

# 2. High severity issues per project
high_sev = (
    issues[issues["severity"] == "High"]
    .groupby("project_id")
    .agg(high_severity_issues=("issue_id", "count"))
    .reset_index()
)

# 3. Merge with projects table
project_kpis = (
    projects
    .merge(issues_per_project, on="project_id", how="left")
    .merge(high_sev, on="project_id", how="left")
)

# Replace NaN (missing values) with 0
project_kpis["total_issues"] = project_kpis["total_issues"].fillna(0).astype(int)
project_kpis["high_severity_issues"] = project_kpis["high_severity_issues"].fillna(0).astype(int)

# 4. Simple risk score (example)
project_kpis["risk_score"] = (
    project_kpis["high_severity_issues"] * 2 +
    (project_kpis["status"] == "At Risk").astype(int) * 3
)

print("Project KPIs:")
print(project_kpis)

# 5. Save for Tableau if you want
project_kpis.to_csv("project_kpis.csv", index=False)
print("\nSaved project_kpis.csv")