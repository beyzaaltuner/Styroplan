import math

import pyodbc as pyodbc
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

erl_command = '''
SELECT  CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE, m.MAKINE, m.CYCLE_TIME, m.KALIP_GENISLIGI, s.PTARIH
FROM SAP_URT_SIP s
INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
WHERE (CAST(TYPE AS varchar(50)) = 'TOP' OR CAST(TYPE AS varchar(50)) = 'MIDDLE' OR CAST(TYPE AS varchar(50)) = 'FRONT') AND  CAST(MAKINE AS varchar(50)) = '870'
ORDER BY CAST(s.AUFNR AS varchar(50)) ASC'''

kz_command = '''
SELECT  CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE, m.MAKINE, m.CYCLE_TIME, m.KALIP_GENISLIGI, s.PTARIH
FROM SAP_URT_SIP s
INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
WHERE (CAST(TYPE AS varchar(50)) = 'TOP' OR CAST(TYPE AS varchar(50)) = 'MIDDLE' OR CAST(TYPE AS varchar(50)) = 'FRONT') AND  CAST(MAKINE AS varchar(50)) = 'KZ'
ORDER BY CAST(s.AUFNR AS varchar(50)) ASC'''

xl_command = '''
SELECT  CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE, m.MAKINE, m.CYCLE_TIME, m.KALIP_GENISLIGI, s.PTARIH
FROM SAP_URT_SIP s
INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
WHERE (CAST(TYPE AS varchar(50)) = 'TOP' OR CAST(TYPE AS varchar(50)) = 'MIDDLE' OR CAST(TYPE AS varchar(50)) = 'FRONT') AND  CAST(MAKINE AS varchar(50)) = 'XL'
ORDER BY CAST(s.AUFNR AS varchar(50)) ASC'''
class Job:
    current_job_id = 1
    def __init__(self, code, processing_time, deadline):
        self.job_id = Job.current_job_id
        Job.current_job_id += 1
        self.code = code
        self.processing_time = processing_time
        self.deadline = deadline
        

def initialize_jobs_from_database(cursor):
    cursor.execute(erl_command)
    jobs = []
    rows = cursor.fetchall()
    # Print each row
    for row in rows:
        print(row)
    for row in rows:
        code = row.PARCA_KODU
        processing_time = row.CYCLE_TIME
        date_from_db = row.PTARIH

        if date_from_db is not None:  # Check explicitly for None values
            # Calculate deadline based on the difference between today's date and date from the database
            today = date(2024,3,20)
            difference_in_days = (date_from_db.date() - today).days
            deadline = difference_in_days + 1

            job = Job(code, math.ceil(processing_time/24), deadline)
            jobs.append(job)
        else:
            # Handle case where PTARIH is None (e.g., NULL in the database)
            print(f"Skipping job with code {code} because PTARIH is None.")
    return jobs

jobs_list = initialize_jobs_from_database(cursor)

for job in jobs_list:
    print(f"Job ID: {job.job_id}, Code: {job.code}, Processing Time: {job.processing_time}, Deadline: {job.deadline}")

job_count = len(jobs_list)
print(f"Number of jobs created: {job_count}")

# Close the cursor and connection
cursor.close()
conn.close()
