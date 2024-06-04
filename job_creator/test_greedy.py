import unittest
import time
from job_creator.jobsFromDb import jobs_list_erl, jobs_list_kz, jobs_list_xl
from greedy_algorithm import greedy_algorithm, calculate_setup_time_change_ERL, calculate_setup_time_change_KZ, \
    calculate_setup_time_change_XL, Machine


class TestGreedyAlgorithmLarge(unittest.TestCase):

    def setUp(self):
        self.num_machines_erl = 3
        self.num_machines_kz = 8
        self.num_machines_xl = 4

    def test_greedy_algorithm_erl(self):
        jobs = jobs_list_erl  # Increase job set size
        machines = [Machine(i) for i in range(self.num_machines_erl)]

        start_time = time.time()
        final_solution, job_times, total_tardiness = greedy_algorithm(jobs, machines, calculate_setup_time_change_ERL)
        end_time = time.time()

        execution_time = end_time - start_time
        self.assertIsNotNone(final_solution)
        self.assertIsInstance(job_times, dict)
        self.assertIsInstance(total_tardiness, int)
        self.assertGreaterEqual(total_tardiness, 0)
        self.verify_job_assignments(final_solution, self.num_machines_erl, jobs)
        self.verify_optimality(job_times, total_tardiness)
        self.verify_performance(execution_time, total_tardiness)

    def test_greedy_algorithm_kz(self):
        jobs = jobs_list_kz
        machines = [Machine(i) for i in range(self.num_machines_kz)]

        start_time = time.time()
        final_solution, job_times, total_tardiness = greedy_algorithm(jobs, machines, calculate_setup_time_change_KZ)
        end_time = time.time()

        execution_time = end_time - start_time
        self.assertIsNotNone(final_solution)
        self.assertIsInstance(job_times, dict)
        self.assertIsInstance(total_tardiness, int)
        self.assertGreaterEqual(total_tardiness, 0)
        self.verify_job_assignments(final_solution, self.num_machines_kz, jobs)
        self.verify_optimality(job_times, total_tardiness)
        self.verify_performance(execution_time, total_tardiness)

    def test_greedy_algorithm_xl(self):
        jobs = jobs_list_xl  # Increase job set size
        machines = [Machine(i) for i in range(self.num_machines_xl)]

        start_time = time.time()
        final_solution, job_times, total_tardiness = greedy_algorithm(jobs, machines, calculate_setup_time_change_XL)
        end_time = time.time()

        execution_time = end_time - start_time
        self.assertIsNotNone(final_solution)
        self.assertIsInstance(job_times, dict)
        self.assertIsInstance(total_tardiness, int)
        self.assertGreaterEqual(total_tardiness, 0)
        self.verify_job_assignments(final_solution, self.num_machines_xl, jobs)
        self.verify_optimality(job_times, total_tardiness)
        self.verify_performance(execution_time, total_tardiness)

    def verify_job_assignments(self, final_solution, num_machines, jobs):
        assigned_jobs = set()
        machine_assignments = {i: [] for i in range(num_machines)}

        for job_id, machine_id, position in final_solution:
            self.assertIn(machine_id, range(num_machines))
            self.assertNotIn(job_id, assigned_jobs, f"Job {job_id} is assigned more than once.")
            assigned_jobs.add(job_id)
            machine_assignments[machine_id].append(position)

        for job in jobs:
            self.assertIn(job.job_id, assigned_jobs, f"Job {job.job_id} is not assigned.")

    def verify_optimality(self, job_times, total_tardiness):
        known_upper_bound = 0  # Replace this with a realistic value for your dataset
        self.assertLessEqual(total_tardiness, known_upper_bound, "Tardiness is less than known lower bound.")
        print(f"Total tardiness in the solution: {total_tardiness}")

    def verify_performance(self, execution_time, total_tardiness):
        acceptable_execution_time = 300  # seconds, adjust based on requirements
        acceptable_tardiness_threshold = 10000  # adjust based on requirements and job set size

        self.assertLessEqual(execution_time, acceptable_execution_time,
                             f"Execution time exceeds acceptable limit: {execution_time} seconds.")
        self.assertLessEqual(total_tardiness, acceptable_tardiness_threshold,
                             f"Tardiness exceeds acceptable threshold: {total_tardiness}.")
        print(f"Execution time: {execution_time} seconds")
        print(f"Total tardiness: {total_tardiness}")


class Job:
    def __init__(self, job_id, mold_width=None, mold_shelf_no=None, male_mold_shelf_no=None, code=None):
        self.job_id = job_id
        self.mold_width = mold_width
        self.mold_shelf_no = mold_shelf_no
        self.male_mold_shelf_no = male_mold_shelf_no
        self.code = code


class TestGreedySetupTimeCalculations(unittest.TestCase):

    def test_calculate_setup_time_change_ERL(self):
        job1 = Job(job_id=1, code='23575831')
        job2 = Job(job_id=2, code='23575831')
        job3 = Job(job_id=3, code='23575832')

        self.assertEqual(calculate_setup_time_change_ERL(job1, job2), 0)
        self.assertEqual(calculate_setup_time_change_ERL(job1, job3), 2)

    def test_calculate_setup_time_change_KZ(self):
        job1 = Job(job_id=1, mold_width='S', mold_shelf_no=1, male_mold_shelf_no=2)
        job2 = Job(job_id=2, mold_width='M', mold_shelf_no=1, male_mold_shelf_no=2)
        job3 = Job(job_id=3, mold_width='L', mold_shelf_no=3, male_mold_shelf_no=4)
        job4 = Job(job_id=4, mold_width='M', mold_shelf_no=3, male_mold_shelf_no=4)
        job5 = Job(job_id=5, mold_width='M', mold_shelf_no=3, male_mold_shelf_no=2)

        self.assertEqual(calculate_setup_time_change_KZ(job1, job2), 4)
        self.assertEqual(calculate_setup_time_change_KZ(job1, job3), 6)
        self.assertEqual(calculate_setup_time_change_KZ(job2, job4), 2)
        self.assertEqual(calculate_setup_time_change_KZ(job4, job5), 1)
        self.assertEqual(calculate_setup_time_change_KZ(job5, job5), 0)

    def test_calculate_setup_time_change_XL(self):
        job1 = Job(job_id=1, mold_width='S', mold_shelf_no=1, male_mold_shelf_no=2)
        job2 = Job(job_id=2, mold_width='M', mold_shelf_no=1, male_mold_shelf_no=2)
        job3 = Job(job_id=3, mold_width='L', mold_shelf_no=3, male_mold_shelf_no=4)
        job4 = Job(job_id=4, mold_width='M', mold_shelf_no=3, male_mold_shelf_no=4)
        job5 = Job(job_id=5, mold_width='M', mold_shelf_no=3, male_mold_shelf_no=2)

        self.assertEqual(calculate_setup_time_change_XL(job1, job2), 8)
        self.assertEqual(calculate_setup_time_change_XL(job1, job3), 12)
        self.assertEqual(calculate_setup_time_change_XL(job2, job4), 4)
        self.assertEqual(calculate_setup_time_change_XL(job4, job5), 2)
        self.assertEqual(calculate_setup_time_change_XL(job5, job5), 0)


if __name__ == '__main__':
    unittest.main()
