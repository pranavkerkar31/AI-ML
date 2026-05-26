import pandas as pd
import numpy as np

# Load dataset
df = pd.read_excel(r"Data Engineering/data_quality_practice_dataset.xlsx")

# Open TXT file
with open("Data Engineering/data_quality_report.txt", "w") as f:

    f.write("========== DATA QUALITY REPORT ==========\n\n")

    # ---------------------------------------------------
    # 1. ACCURACY
    # ---------------------------------------------------
    f.write("1. ACCURACY\n")

    invalid_age = df[(df['Age'] < 18) | (df['Age'] > 60)]
    invalid_salary = df[df['Salary'] < 0]
    invalid_performance = df[df['Performance_Score'] > 5]

    f.write(f"Invalid Age Entries: {len(invalid_age)}\n")
    f.write(f"Invalid Salary Entries: {len(invalid_salary)}\n")
    f.write(f"Invalid Performance Scores: {len(invalid_performance)}\n\n")

    # ---------------------------------------------------
    # 2. COMPLETENESS
    # ---------------------------------------------------
    f.write("2. COMPLETENESS\n")

    missing_values = df.isnull().sum()

    f.write("Missing Values Per Column:\n")
    f.write(str(missing_values))
    f.write("\n\n")

    # ---------------------------------------------------
    # 3. CONSISTENCY
    # ---------------------------------------------------
    f.write("3. CONSISTENCY\n")

    unique_departments = df['Department'].unique()

    f.write("Unique Department Values:\n")
    f.write(str(unique_departments))
    f.write("\n")

    inconsistent_dept = df[
        df['Department'].isin(['it', 'I.T', 'Comp'])
    ]

    f.write(f"Inconsistent Department Entries: {len(inconsistent_dept)}\n\n")

    # ---------------------------------------------------
    # 4. TIMELINESS
    # ---------------------------------------------------
    f.write("4. TIMELINESS\n")

    df['Joining_Date'] = pd.to_datetime(df['Joining_Date'])

    latest_date = df['Joining_Date'].max()
    oldest_date = df['Joining_Date'].min()

    f.write(f"Latest Joining Date: {latest_date}\n")
    f.write(f"Oldest Joining Date: {oldest_date}\n\n")

    # ---------------------------------------------------
    # 5. BELIEVABILITY
    # ---------------------------------------------------
    f.write("5. BELIEVABILITY\n")

    unbelievable_data = df[
        (df['Age'] < 10) |
        (df['Salary'] > 1000000)
    ]

    f.write(f"Unbelievable Records Found: {len(unbelievable_data)}\n\n")

    # ---------------------------------------------------
    # 6. INTERPRETABILITY
    # ---------------------------------------------------
    f.write("6. INTERPRETABILITY\n")

    f.write("Column Names:\n")
    f.write(str(df.columns.tolist()))
    f.write("\n\n")

    f.write("Data Types:\n")
    f.write(str(df.dtypes))
    f.write("\n\n")

    # ---------------------------------------------------
    # EXTRA INFORMATION
    # ---------------------------------------------------
    f.write("========== EXTRA DATASET INFO ==========\n\n")

    f.write(f"Dataset Shape: {df.shape}\n\n")

    f.write("Statistical Summary:\n")
    f.write(str(df.describe()))
    f.write("\n\n")

print("TXT report generated successfully!")