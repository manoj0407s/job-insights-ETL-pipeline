from extract import extract_jobs
from transform import transform_jobs
from load import load_jobs
from datetime import datetime

def main():
    print(f"⏰ ETL started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print("🔍 Extracting job data...")
    raw = extract_jobs()

    print("🧹 Transforming job data...")
    clean = transform_jobs(raw)

    print("💾 Loading data into MySQL...")
    load_jobs(clean)

    print("✅ ETL Job Done!")

if __name__ == "__main__":
    main()
