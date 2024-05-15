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
SELECT CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE, m.MAKINE, m.CYCLE_TIME, m.KALIP_GENISLIGI, s.PTARIH
FROM SAP_URT_SIP s
INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
WHERE (CAST(TYPE AS varchar(50)) = 'TOP' OR CAST(TYPE AS varchar(50)) = 'MIDDLE' OR CAST(TYPE AS varchar(50)) = 'FRONT') AND  CAST(MAKINE AS varchar(50)) = '870'
'''



kz_command = '''
SELECT CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE, m.MAKINE, m.CYCLE_TIME, m.KALIP_GENISLIGI, s.PTARIH
FROM SAP_URT_SIP s
INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
WHERE (CAST(TYPE AS varchar(50)) = 'TOP' OR CAST(TYPE AS varchar(50)) = 'MIDDLE' OR CAST(TYPE AS varchar(50)) = 'FRONT') AND  CAST(MAKINE AS varchar(50)) = 'KZ'
'''

xl_command = '''
SELECT CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE, m.MAKINE, m.CYCLE_TIME, m.KALIP_GENISLIGI, s.PTARIH
FROM SAP_URT_SIP s
INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
WHERE (CAST(TYPE AS varchar(50)) = 'TOP' OR CAST(TYPE AS varchar(50)) = 'MIDDLE' OR CAST(TYPE AS varchar(50)) = 'FRONT') AND  CAST(MAKINE AS varchar(50)) = 'XL'
'''


class Job:
    current_job_id = 1

    def __init__(self, code, mold_shelf_no, male_mold_shelf_no, processing_time, mold_width, deadline):
        self.job_id = Job.current_job_id
        Job.current_job_id += 1
        self.code = code
        self.mold_shelf_no = mold_shelf_no
        self.male_mold_shelf_no = male_mold_shelf_no
        self.processing_time = processing_time
        self.mold_width = mold_width
        self.deadline = deadline


all_jobs = []

def initialize_jobs_from_database(cursor, command):
    cursor.execute(command)
    jobs = []
    rows = cursor.fetchall()
    # Print each row
    for row in rows:
        print(row)
    for row in rows:
        code = row.PARCA_KODU
        mold_shelf_no = row.KALIP_RAF_NO
        male_mold_shelf_no = row.ERKEK_KALIP_RAF_NO
        processing_time = row.CYCLE_TIME
        mold_width = row.KALIP_GENISLIGI
        date_from_db = row.PTARIH

        if date_from_db is not None:  # Check explicitly for None values
            # Calculate deadline based on the difference between today's date and date from the database
            today = date(2024, 3, 5)
            difference_in_days = (date_from_db.date() - today).days
            deadline = (difference_in_days + 1) * 1440

            job = Job(code, mold_shelf_no, male_mold_shelf_no, math.ceil(processing_time / 60), mold_width,
                      deadline)
            jobs.append(job)
            all_jobs.append(job)
        else:
            # Handle case where PTARIH is None (e.g., NULL in the database)
            print(f"Skipping job with code {code} because PTARIH is None.")
    return jobs


jobs_list_erl = initialize_jobs_from_database(cursor, erl_command)
jobs_list_kz = initialize_jobs_from_database(cursor, kz_command)
jobs_list_xl = initialize_jobs_from_database(cursor, xl_command)


for job in all_jobs:
    print(
        f"Job ID: {job.job_id}, Code: {job.code}, Mold Shelf No: {job.mold_shelf_no}, Male Mold Shelf No: {job.male_mold_shelf_no}, Processing Time: {job.processing_time}, Mold Width: {job.mold_width}, Deadline: {job.deadline}")


job_count = len(all_jobs)
print(f"Number of jobs created: {job_count}")

# Close the cursor and connection
cursor.close()
conn.close()
