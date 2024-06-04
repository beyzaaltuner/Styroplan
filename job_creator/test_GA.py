import unittest
import random
import time
from genetic_algorithm import genetic_algorithm, calculate_setup_time_change_ERL, calculate_setup_time_change_KZ, calculate_setup_time_change_XL
from job_creator.jobsFromDb import jobs_list_erl, jobs_list_kz, jobs_list_xl

class TestGeneticAlgorithm(unittest.TestCase):

    def setUp(self):
        self.population_size = 1000
        self.mutation_rate = 0.1
        self.max_generations = 100

    def test_genetic_algorithm_large_erl(self):
        num_machines = 3
        jobs = jobs_list_erl  # Increase job set size

        start_time = time.time()
        best_solution, job_times, tardiness = genetic_algorithm(self.population_size, self.mutation_rate, self.max_generations, num_machines, jobs, calculate_setup_time_change_ERL)
        end_time = time.time()

        execution_time = end_time - start_time
        self.assertIsNotNone(best_solution)
        self.assertIsInstance(job_times, dict)
        self.assertIsInstance(tardiness, int)
        self.assertGreaterEqual(tardiness, 0)
        self.verify_job_assignments(best_solution, num_machines, jobs)
        self.verify_optimality(job_times, tardiness)
        self.verify_performance(execution_time, tardiness)

    def test_genetic_algorithm_large_kz(self):
        num_machines = 8
        jobs = jobs_list_kz   # Increase job set size

        start_time = time.time()
        best_solution, job_times, tardiness = genetic_algorithm(self.population_size, self.mutation_rate, self.max_generations, num_machines, jobs, calculate_setup_time_change_KZ)
        end_time = time.time()

        execution_time = end_time - start_time
        self.assertIsNotNone(best_solution)
        self.assertIsInstance(job_times, dict)
        self.assertIsInstance(tardiness, int)
        self.assertGreaterEqual(tardiness, 0)
        self.verify_job_assignments(best_solution, num_machines, jobs)
        self.verify_optimality(job_times, tardiness)
        self.verify_performance(execution_time, tardiness)

    def test_genetic_algorithm_large_xl(self):
        num_machines = 4
        jobs = jobs_list_xl  # Increase job set size

        start_time = time.time()
        best_solution, job_times, tardiness = genetic_algorithm(self.population_size, self.mutation_rate, self.max_generations, num_machines, jobs, calculate_setup_time_change_XL)
        end_time = time.time()

        execution_time = end_time - start_time
        self.assertIsNotNone(best_solution)
        self.assertIsInstance(job_times, dict)
        self.assertIsInstance(tardiness, int)
        self.assertGreaterEqual(tardiness, 0)
        self.verify_job_assignments(best_solution, num_machines, jobs)
        self.verify_optimality(job_times, tardiness)
        self.verify_performance(execution_time, tardiness)

    def verify_job_assignments(self, best_solution, num_machines, jobs):
        assigned_jobs = set()
        machine_assignments = {i: [] for i in range(num_machines)}

        for gene in best_solution:
            job_id, machine, position = gene
            self.assertIn(machine, range(num_machines))
            self.assertNotIn(job_id, assigned_jobs, f"Job {job_id} is assigned more than once.")
            assigned_jobs.add(job_id)
            machine_assignments[machine].append(position)

        for job in jobs:
            self.assertIn(job.job_id, assigned_jobs, f"Job {job.job_id} is not assigned.")

    def verify_optimality(self, job_times, tardiness):
        # Assuming we have a known lower bound for tardiness for comparison
        known_upper_bound = 10  # Replace this with a realistic value for your dataset
        self.assertLessEqual(tardiness, known_upper_bound, "Tardiness is greater than known lower bound.")
        print(f"Total tardiness in the solution: {tardiness}")

    def verify_performance(self, execution_time, tardiness):
        # Set acceptable limits for execution time and solution quality
        acceptable_execution_time = 300  # seconds, adjust based on requirements
        acceptable_tardiness_threshold = 10000  # adjust based on requirements and job set size

        self.assertLessEqual(execution_time, acceptable_execution_time,
                                f"Execution time exceeds acceptable limit: {execution_time} seconds.")
        self.assertLessEqual(tardiness, acceptable_tardiness_threshold,
                                f"Tardiness exceeds acceptable threshold: {tardiness}.")
        print(f"Execution time: {execution_time} seconds")
        print(f"Total tardiness: {tardiness}")


class Job:
    def __init__(self, job_id, mold_width=None, mold_shelf_no=None, male_mold_shelf_no=None, code=None, processing_time=0, deadline=0):
        self.job_id = job_id
        self.mold_width = mold_width
        self.mold_shelf_no = mold_shelf_no
        self.male_mold_shelf_no = male_mold_shelf_no
        self.code = code
        self.processing_time = processing_time
        self.deadline = deadline


class TestGeneticSetupTimeCalculations(unittest.TestCase):

    def setUp(self):
        # Setup some dummy jobs
        self.jobs_erl = [
            Job(job_id=1, code='23575831', processing_time=2, deadline=10),
            Job(job_id=2, code='23575831', processing_time=3, deadline=15),
            Job(job_id=3, code='23575832', processing_time=4, deadline=20),
        ]

        self.jobs_kz = [
            Job(job_id=1, mold_width='S', mold_shelf_no=1, male_mold_shelf_no=2, processing_time=2, deadline=10),
            Job(job_id=2, mold_width='M', mold_shelf_no=1, male_mold_shelf_no=2, processing_time=3, deadline=15),
            Job(job_id=3, mold_width='L', mold_shelf_no=3, male_mold_shelf_no=4, processing_time=4, deadline=20),
            Job(job_id=4, mold_width='M', mold_shelf_no=3, male_mold_shelf_no=4, processing_time=5, deadline=5),
            Job(job_id=5, mold_width='M', mold_shelf_no=3, male_mold_shelf_no=2, processing_time=2, deadline=20)
        ]

        self.jobs_xl = [
            Job(job_id=1, mold_width='S', mold_shelf_no=1, male_mold_shelf_no=2, processing_time=2, deadline=10),
            Job(job_id=2, mold_width='M', mold_shelf_no=1, male_mold_shelf_no=2, processing_time=3, deadline=15),
            Job(job_id=3, mold_width='L', mold_shelf_no=3, male_mold_shelf_no=4, processing_time=4, deadline=20),
            Job(job_id=4, mold_width='M', mold_shelf_no=3, male_mold_shelf_no=4, processing_time=5, deadline=5),
            Job(job_id=5, mold_width='M', mold_shelf_no=3, male_mold_shelf_no=2, processing_time=2, deadline=20)
        ]

    def test_calculate_setup_time_change_ERL(self):
        job1 = self.jobs_erl[0]
        job2 = self.jobs_erl[1]
        job3 = self.jobs_erl[2]

        self.assertEqual(calculate_setup_time_change_ERL(job1, job2), 0)
        self.assertEqual(calculate_setup_time_change_ERL(job1, job3), 2)

    def test_calculate_setup_time_change_KZ(self):
        job1 = self.jobs_kz[0]
        job2 = self.jobs_kz[1]
        job3 = self.jobs_kz[2]
        job4 = self.jobs_kz[3]
        job5 = self.jobs_kz[4]

        self.assertEqual(calculate_setup_time_change_KZ(job1, job2), 4)
        self.assertEqual(calculate_setup_time_change_KZ(job1, job3), 6)
        self.assertEqual(calculate_setup_time_change_KZ(job2, job4), 2)
        self.assertEqual(calculate_setup_time_change_KZ(job4, job5), 1)
        self.assertEqual(calculate_setup_time_change_KZ(job5, job5), 0)

    def test_calculate_setup_time_change_XL(self):
        job1 = self.jobs_xl[0]
        job2 = self.jobs_xl[1]
        job3 = self.jobs_xl[2]
        job4 = self.jobs_kz[3]
        job5 = self.jobs_kz[4]

        self.assertEqual(calculate_setup_time_change_XL(job1, job2), 8)
        self.assertEqual(calculate_setup_time_change_XL(job1, job3), 12)
        self.assertEqual(calculate_setup_time_change_XL(job2, job4), 4)
        self.assertEqual(calculate_setup_time_change_XL(job4, job5), 2)
        self.assertEqual(calculate_setup_time_change_XL(job5, job5), 0)


if __name__ == '__main__':
    unittest.main()