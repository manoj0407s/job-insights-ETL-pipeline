import mysql.connector
from db_config import MYSQL_CONFIG

def load_jobs(jobs):
    # ✅ Connect directly using your existing `job_insights` database
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()

    # ✅ Create the jobs table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id VARCHAR(255) PRIMARY KEY,
            title VARCHAR(255),
            company VARCHAR(255),
            location VARCHAR(255),
            description TEXT,
            date_posted DATE
        )
    """)

    # ✅ Insert or update records
    insert_query = """
        INSERT INTO jobs (id, title, company, location, description, date_posted)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            title=VALUES(title),
            company=VALUES(company),
            location=VALUES(location),
            description=VALUES(description),
            date_posted=VALUES(date_posted)
    """

    data = [
        (
            job["id"],
            job["title"],
            job["company"],
            job["location"],
            job["description"],
            job["date_posted"]
        )
        for job in jobs
    ]

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()
