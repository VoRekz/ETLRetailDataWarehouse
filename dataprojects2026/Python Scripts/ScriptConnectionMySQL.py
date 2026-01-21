import pandas as pd
import pymysql
from sqlalchemy import create_engine

# 1. Database Connection Details
USER = 'root'
PASSWORD = 'Your SQL Password'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'dw'
TABLE_NAME = 'dimloyaltyinfo'

# 2. Create the Connection String
# Format: mysql+pymysql://user:password@host:port/database
connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

try:
    # 3. Create the Database Engine
    engine = create_engine(connection_string)

    # 4. Fetch the data into a DataFrame
    print(f"Connecting to MySQL and fetching data from {TABLE_NAME}...")
    query = f"SELECT * FROM {TABLE_NAME}"
    df = pd.read_sql(query, engine)

  # 5. Define the specific folder path
# The 'r' at the start handles the backslashes correctly for Windows
    output_folder = r"C:\Users\julio\OneDrive\Documents\dataprojects2026\Excel"
    output_file = f"{output_folder}\\{TABLE_NAME}Ver1_export.csv"
    
    print(f"Success! Data exported to {output_file}")
    print(f"Total rows exported: {len(df)}")

except Exception as e:
    print(f"An error occurred: {e}")

# 6. Export to CSV
try:
    df.to_csv(output_file, index=False)
    print(f"Success! Data exported to: {output_file}")
except FileNotFoundError:
    print("Error: The folder 'Excel' does not exist in that location. Please create it first.")

