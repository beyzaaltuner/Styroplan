import pyodbc
from datetime import date

server = 'localhost\\SQLEXPRESS' 
database = 'StyroPlanDB' 

conn_str = (
    f'DRIVER={{SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

class Job:
    def __init__(self, job_id, processing_time, deadline):
        self.job_id = job_id
        self.processing_time = processing_time
        self.deadline = deadline
        

def initialize_jobs_from_database(self):
    self.cursor.execute(f'''
        SELECT CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE, m.MAKINE, m.CYCLE_TIME, m.KALIP_GENISLIGI, s.PTARIH
        FROM SAP_URT_SIP s
        INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
        INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
        ORDER BY CAST(s.AUFNR AS varchar(50)) ASC''')
    jobs = []
    rows = self.cursor.fetchall()
    # Print each row
    for row in rows:
        print(row)
    for row in rows:
        job_id = row.PARCA_KODU
        processing_time = row.CYCLE_TIME
        date_from_db = row.PTARIH

        

        if date_from_db is not None:  # Check explicitly for None values
            # Calculate deadline based on the difference between today's date and date from the database
            today = date(2024,3,31)
            difference_in_days = (date_from_db.date() - today).days
            deadline = difference_in_days + 1  # Add processing time to the difference

            job = Job(job_id, processing_time, deadline)
            jobs.append(job)
        else:
            # Handle case where PTARIH is None (e.g., NULL in the database)
            print(f"Skipping job with ID {job_id} because PTARIH is None.")
    return jobs

jobs = initialize_jobs_from_database(cursor)

for job in jobs:
    print(f"Job ID: {job.job_id}, Processing Time: {job.processing_time}, Deadline: {job.deadline}")

job_count = len(jobs)
print(f"Number of jobs created: {job_count}")


# Close the cursor and connection
cursor.close()
conn.close()


