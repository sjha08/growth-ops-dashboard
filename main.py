"""
Growth Ops Dashboard
--------------------
Loads sample business data, calculates weekly KPIs, and prints summary insights.
"""

import pandas as pd

def load_data(path: str = "sample_data/weekly_metrics.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def summarize_growth(df: pd.DataFrame) -> dict:
    latest = df.iloc[-1]
    prev = df.iloc[-2]
    growth_rate = round((latest["revenue"] - prev["revenue"]) / prev["revenue"] * 100, 2)
    conv_change = round(latest["conversion_rate"] - prev["conversion_rate"], 2)
    churn_change = round(prev["churn"] - latest["churn"], 2)

    return {
        "revenue_growth_%": growth_rate,
        "conversion_delta": conv_change,
        "churn_improvement": churn_change
    }

def print_summary(metrics: dict):
    print("Weekly Growth Summary:")
    print(f"- Revenue Growth: +{metrics['revenue_growth_%']}%")
    print(f"- Conversion Rate Change: {metrics['conversion_delta']} pts")
    print(f"- Churn Improvement: {metrics['churn_improvement']} pts")
    print("\nInsight: Revenue and conversion are trending upward, churn is stabilizing.")

if __name__ == "__main__":
    data = load_data()
    results = summarize_growth(data)
    print_summary(results)

