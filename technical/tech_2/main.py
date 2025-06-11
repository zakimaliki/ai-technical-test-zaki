import pandas as pd
import json

def process_data(df):
    # Extract email from _meta column
    df['email'] = df['_meta'].apply(lambda x: json.loads(x)['email'])
    
    # Calculate project count and highest salary
    project_count = df['email'].value_counts().idxmax()
    highest_salary = df.groupby('email')['total_earnings_idr'].sum().idxmax()
    
    # Create output DataFrame
    out_df = pd.DataFrame([
        {"qualification": "project_count", "top_contributor": project_count},
        {"qualification": "total_salary_idr", "top_contributor": highest_salary}
    ])
    
    # Process Q1 2024 data
    df['date'] = pd.to_datetime(df['date'])
    q1 = df[df['date'].dt.quarter == 1]
    top_roles = (
        q1.groupby(['client_company_id', 'project_role'])
        .agg(earnings=('total_earnings_idr', 'sum'), hourly_rate_idr=('hourly_rate_idr', 'mean'))
        .sort_values(by='earnings', ascending=False)
        .head(10)
        .reset_index()
    )
    
    return out_df, top_roles

if __name__ == "__main__":
    # Read data
    df = pd.read_csv('freelancers.csv')
    
    # Process data
    out_df, top_roles = process_data(df)
    
    # Save results
    out_df.to_csv("out.csv", index=False)
    top_roles.to_csv("top_roles.csv", index=False)