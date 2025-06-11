import pandas as pd
import json
import pytest # type: ignore
from main import process_data

def test_process_data():
    # Read data from freelancers.csv
    df = pd.read_csv('freelancers.csv')
    
    # Process data
    out_df, top_roles = process_data(df)
    
    # Test output format
    assert len(out_df) == 2
    assert 'qualification' in out_df.columns
    assert 'top_contributor' in out_df.columns
    
    # Test project count
    project_count_row = out_df[out_df['qualification'] == 'project_count']
    assert len(project_count_row) == 1
    assert '@example.com' in project_count_row['top_contributor'].iloc[0]
    
    # Test total salary
    total_salary_row = out_df[out_df['qualification'] == 'total_salary_idr']
    assert len(total_salary_row) == 1
    assert '@example.com' in total_salary_row['top_contributor'].iloc[0]
    
    # Test top roles
    assert len(top_roles) <= 10  # Should have at most 10 rows
    assert 'client_company_id' in top_roles.columns
    assert 'project_role' in top_roles.columns
    assert 'earnings' in top_roles.columns
    assert 'hourly_rate_idr' in top_roles.columns
    
    # Test Q1 2024 filtering (all dates in top_roles must be Q1)
    if not top_roles.empty:
        # Get the original df filtered to Q1 and matching top_roles
        df['date'] = pd.to_datetime(df['date'])
        q1 = df[df['date'].dt.quarter == 1]
        for _, row in top_roles.iterrows():
            filtered = q1[(q1['client_company_id'] == row['client_company_id']) & (q1['project_role'] == row['project_role'])]
            assert not filtered.empty
            assert all(filtered['date'].dt.quarter == 1)
    
    # Test earnings sorting
    assert top_roles['earnings'].is_monotonic_decreasing  # Should be sorted in descending order 