import unittest
from datetime import date, datetime, timedelta
from unittest.mock import patch, MagicMock
from jobsFromDb import initialize_jobs_from_database, all_jobs, Job
import math



class MockRow:
    def __init__(self, PARCA_KODU, KALIP_RAF_NO, ERKEK_KALIP_RAF_NO, TYPE, MAKINE, CYCLE_TIME, KALIP_GENISLIGI, PTARIH):
        self.PARCA_KODU = PARCA_KODU
        self.KALIP_RAF_NO = KALIP_RAF_NO
        self.ERKEK_KALIP_RAF_NO = ERKEK_KALIP_RAF_NO
        self.TYPE = TYPE
        self.MAKINE = MAKINE
        self.CYCLE_TIME = CYCLE_TIME
        self.KALIP_GENISLIGI = KALIP_GENISLIGI
        self.PTARIH = PTARIH

class TestJobInitialization(unittest.TestCase):
    def setUp(self):
        # Mock connection and cursor
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor

        # Mock database rows
        self.mock_erl_rows = [
            MockRow('P001', 'S001', 'E001', 'TOP', '870', 60, 100, datetime(2024, 3, 10)),
            MockRow('P002', 'S002', 'E002', 'MIDDLE', '870', 120, 200, datetime(2024, 3, 15)),
            MockRow('P003', 'S003', 'E003', 'FRONT', '870', 180, 300, None)  # This row has None PTARIH
        ]

        self.mock_kz_rows = [
            MockRow('P004', 'S004', 'E004', 'TOP', 'KZ', 90, 150, datetime(2024, 3, 20)),
            MockRow('P005', 'S005', 'E005', 'MIDDLE', 'KZ', 150, 250, datetime(2024, 3, 25))
        ]

        self.mock_xl_rows = [
            MockRow('P006', 'S006', 'E006', 'TOP', 'XL', 210, 350, datetime(2024, 3, 30)),
            MockRow('P007', 'S007', 'E007', 'FRONT', 'XL', 240, 450, datetime(2024, 4, 1))
        ]

        # Mock execute and fetchall methods
        self.mock_cursor.execute.side_effect = [None, None, None]
        self.mock_cursor.fetchall.side_effect = [self.mock_erl_rows, self.mock_kz_rows, self.mock_xl_rows]

    @patch('pyodbc.connect')
    def test_initialize_jobs_from_database(self, mock_connect):
        mock_connect.return_value = self.mock_conn

        # Commands to be tested
        erl_command = '''
        SELECT CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE, m.MAKINE, m.CYCLE_TIME, m.KALIP_GENISLIGI, s.PTARIH
        FROM SAP_URT_SIP s
        INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
        INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
        WHERE (CAST(TYPE AS varchar(50)) = 'TOP' OR CAST(TYPE AS varchar(50)) = 'MIDDLE' OR CAST(TYPE AS varchar(50)) = 'FRONT') AND  CAST(MAKINE AS varchar(50)) = '870'
        '''

        kz_command = '''
        SELECT top 50 CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE, m.MAKINE, m.CYCLE_TIME, m.KALIP_GENISLIGI, s.PTARIH
        FROM SAP_URT_SIP s
        INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
        INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
        WHERE (CAST(TYPE AS varchar(50)) = 'TOP' OR CAST(TYPE AS varchar(50)) = 'MIDDLE' OR CAST(TYPE AS varchar(50)) = 'FRONT') AND  CAST(MAKINE AS varchar(50)) = 'KZ'
        '''

        xl_command = '''
        SELECT top 50 CAST(m.PARCA_KODU AS varchar(50)) AS PARCA_KODU, m.KALIP_RAF_NO, m.ERKEK_KALIP_RAF_NO, m.TYPE, m.MAKINE, m.CYCLE_TIME, m.KALIP_GENISLIGI, s.PTARIH
        FROM SAP_URT_SIP s
        INNER JOIN SAP_URT_BILESEN b ON CAST(b.AUFNR AS varchar(50)) = CAST(s.AUFNR AS varchar(50))
        INNER JOIN PLAN_MAKINELER m ON CAST(m.PARCA_KODU AS varchar(50)) = CAST(b.MATNR AS varchar(50))
        WHERE (CAST(TYPE AS varchar(50)) = 'TOP' OR CAST(TYPE AS varchar(50)) = 'MIDDLE' OR CAST(TYPE AS varchar(50)) = 'FRONT') AND  CAST(MAKINE AS varchar(50)) = 'XL'
        '''

        # Test for erl_command
        jobs_list_erl = initialize_jobs_from_database(self.mock_cursor, erl_command)
        self.assertEqual(len(jobs_list_erl), 2)  # Only 2 valid rows, 1 row skipped due to None PTARIH

        # Test for kz_command
        jobs_list_kz = initialize_jobs_from_database(self.mock_cursor, kz_command)
        self.assertEqual(len(jobs_list_kz), 2)  # 2 valid rows

        # Test for xl_command
        jobs_list_xl = initialize_jobs_from_database(self.mock_cursor, xl_command)
        self.assertEqual(len(jobs_list_xl), 2)  # 2 valid rows

        all_jobs = jobs_list_erl + jobs_list_kz + jobs_list_xl

        for job in all_jobs:
            print(f"Job ID: {job.job_id}, Code: {job.code}, Mold Shelf No: {job.mold_shelf_no}, Male Mold Shelf No: {job.male_mold_shelf_no}, Type: {job.job_type}, Processing Time: {job.processing_time}, Mold Width: {job.mold_width}, Deadline: {job.deadline}")

        self.assertEqual(len(all_jobs), 6)
        print(f"Number of jobs created: {len(all_jobs)}")





class Job:
    current_job_id = 1

    def __init__(self, code, mold_shelf_no, male_mold_shelf_no, job_type, processing_time, mold_width, deadline):
        self.job_id = Job.current_job_id
        Job.current_job_id += 1
        self.code = code
        self.mold_shelf_no = mold_shelf_no
        self.male_mold_shelf_no = male_mold_shelf_no
        self.job_type = job_type
        self.processing_time = processing_time
        self.mold_width = mold_width
        self.deadline = deadline


all_jobs = []

def initialize_jobs_from_database(cursor, command):
    cursor.execute(command)
    jobs = []
    rows = cursor.fetchall()
    for row in rows:
        code = row[0]  # index 0 for PARCA_KODU
        mold_shelf_no = row[1]  # index 1 for KALIP_RAF_NO
        male_mold_shelf_no = row[2]  # index 2 for ERKEK_KALIP_RAF_NO
        job_type = row[3]  # index 3 for TYPE
        processing_time = row[4]  # index 4 for CYCLE_TIME
        mold_width = row[5]  # index 5 for KALIP_GENISLIGI
        date_from_db = row[6]  # index 6 for PTARIH

        if date_from_db is not None:
            today = date(2024, 3, 5)
            difference_in_days = (date_from_db - today).days
            deadline = (difference_in_days + 1) * 1440

            job = Job(code, mold_shelf_no, male_mold_shelf_no, job_type, math.ceil(processing_time / 60), mold_width, deadline)
            jobs.append(job)
            all_jobs.append(job)
        else:
            print(f"Skipping job with code {code} because PTARIH is None.")
    return jobs

class MockCursor:
    def __init__(self, data):
        self.data = data

    def execute(self, command):
        pass

    def fetchall(self):
        return self.data

class TestJobFiltering(unittest.TestCase):

    def setUp(self):
        self.today = date(2024, 3, 5)
        Job.current_job_id = 1

        self.jobs = [
            Job('Code1', 'Shelf1', 'MaleShelf1', 'TOP', 60, 'S', (self.today + timedelta(days=2)).strftime('%Y-%m-%d')),
            Job('Code2', 'Shelf2', 'MaleShelf2', 'BOTTOM', 90, 'M', (self.today + timedelta(days=3)).strftime('%Y-%m-%d')),
            Job('Code3', 'Shelf3', 'MaleShelf3', 'MIDDLE', 120, 'L', (self.today + timedelta(days=4)).strftime('%Y-%m-%d')),
            Job('Code4', 'Shelf4', 'MaleShelf4', 'FRONT', 150, 'ERL', (self.today + timedelta(days=1)).strftime('%Y-%m-%d')),
            Job('Code5', 'Shelf5', 'MaleShelf5', 'BACK', 180, 'S', (self.today + timedelta(days=5)).strftime('%Y-%m-%d')),
        ]

    def test_planned_job_filtering_by_mold_width(self):
        selected_widths = ['S', 'M']

        filtered_jobs = [job for job in self.jobs if job.mold_width in selected_widths]

        expected_filtered_codes = ['Code1', 'Code2', 'Code5']
        filtered_codes = [job.code for job in filtered_jobs]

        self.assertEqual(filtered_codes, expected_filtered_codes, f"Expected {expected_filtered_codes} but got {filtered_codes}")

    def test_unplanned_job_filtering_by_type(self):
        selected_types = ['TOP', 'FRONT']

        filtered_jobs = [job for job in self.jobs if job.job_type in selected_types]

        expected_filtered_codes = ['Code1', 'Code4']
        filtered_codes = [job.code for job in filtered_jobs]

        self.assertEqual(filtered_codes, expected_filtered_codes, f"Expected {expected_filtered_codes} but got {filtered_codes}")

if __name__ == '__main__':
    unittest.main()

mock_data = [

    ('Code1', 'Shelf1', 'MaleShelf1', 'TOP', 60, 'S', date(2024, 3, 7)),
    ('Code2', 'Shelf2', 'MaleShelf2', 'BOTTOM', 90, 'M', date(2024, 3, 8)),
    ('Code3', 'Shelf3', 'MaleShelf3', 'MIDDLE', 120, 'L', date(2024, 3, 8)),
    ('Code4', 'Shelf4', 'MaleShelf4', 'FRONT', 150, 'ERL',  date(2024, 3, 8)),
    ('Code5', 'Shelf5', 'MaleShelf5', 'BACK', 180, 'S', date(2024, 3, 8))
    # Add more mock rows as needed
]

mock_cursor = MockCursor(mock_data)
jobs = initialize_jobs_from_database(mock_cursor, 'SELECT command placeholder')
for job in jobs:
    print(job.__dict__)