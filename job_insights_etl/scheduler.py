import schedule
import time
import subprocess
from datetime import datetime

def run_etl():
    print(f"🔁 Running ETL job at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
    subprocess.run(["python", "main.py"])
    print("✅ ETL job completed.\n")

# Run every 1 minute
schedule.every(1).minutes.do(run_etl)

print("🔄 Starting ETL scheduler (runs every 1 minute)...")

while True:
    schedule.run_pending()
    time.sleep(1)
