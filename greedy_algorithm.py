from job_creator.jobsFromDb import *
import time


class Machine:
    # To generate sequentially increasing machine IDs

    def __init__(self, id):
        self.machine_id = id
        self.finish_time = 0
        self.jobs_queue = []

    def display_queue(self):
        print(f"Machine {self.machine_id} Queue:")
        for job in self.jobs_queue:
            print(job.job_id)
        print("\n")

def calculate_setup_time_change_KZ(previous_job, current_job):
    mold_width_change = current_job.mold_width != previous_job.mold_width
    mold_shelf_no_change = current_job.mold_shelf_no != previous_job.mold_shelf_no
    male_mold_shelf_no_change = current_job.male_mold_shelf_no != previous_job.male_mold_shelf_no

    if mold_width_change:
        if (previous_job.mold_width == 'S' and current_job.mold_width == 'M') or \
                (previous_job.mold_width == 'M' and current_job.mold_width == 'S') or \
                (previous_job.mold_width == 'M' and current_job.mold_width == 'L') or \
                (previous_job.mold_width == 'L' and current_job.mold_width == 'M'):
            return 4
        elif (previous_job.mold_width == 'S' and current_job.mold_width == 'L') or \
                (previous_job.mold_width == 'L' and current_job.mold_width == 'S'):
            return 6
    else:
        if mold_shelf_no_change:
            return 2
        else:
            if male_mold_shelf_no_change:
                return 1

    return 0  # NO CHANGE


def calculate_setup_time_change_XL(previous_job, current_job):
    mold_width_change = current_job.mold_width != previous_job.mold_width
    mold_shelf_no_change = current_job.mold_shelf_no != previous_job.mold_shelf_no
    male_mold_shelf_no_change = current_job.male_mold_shelf_no != previous_job.male_mold_shelf_no

    if mold_width_change:
        if (previous_job.mold_width == 'S' and current_job.mold_width == 'M') or \
                (previous_job.mold_width == 'M' and current_job.mold_width == 'S') or \
                (previous_job.mold_width == 'M' and current_job.mold_width == 'L') or \
                (previous_job.mold_width == 'L' and current_job.mold_width == 'M'):
            return 8
        elif (previous_job.mold_width == 'S' and current_job.mold_width == 'L') or \
                (previous_job.mold_width == 'L' and current_job.mold_width == 'S'):
            return 12
    else:
        if mold_shelf_no_change:
            return 4
        else:
            if male_mold_shelf_no_change:
                return 2

    return 0  # NO CHANGE


def calculate_setup_time_change_ERL(previous_job, current_job):
    mold_width_change = current_job.code != previous_job.code

    if mold_width_change:
        return 2
    else:
        return 0



def greedy_algorithm(jobs, machines,calculate_setup_time_func):
    # Sort jobs by deadlines in ascending order
    sorted_jobs = sorted(jobs, key=lambda x: x.deadline)

    # Dictionary to store start and finish times for each job
    job_times = {}
    final_solution = []

    for job in sorted_jobs:
        best_machine = None
        min_finish_time = float('inf')

        for machine in machines:
            previous_job = machine.jobs_queue[-1] if machine.jobs_queue else None
            setup_time = calculate_setup_time_func(previous_job, job) if previous_job else 0
            job_finish_time = machine.finish_time + setup_time + job.processing_time

            if job_finish_time < min_finish_time:
                min_finish_time = job_finish_time
                best_machine = machine

        # Assign the job to the best machine
        best_machine.jobs_queue.append(job)
        best_machine.finish_time = min_finish_time


        # Calculate start time considering previous job
        job_start_time = best_machine.finish_time - job.processing_time
        final_solution.append([job.job_id, best_machine.machine_id, len(best_machine.jobs_queue) - 1])

        # Store start and finish times for the job
        job_times[(best_machine.machine_id, len(best_machine.jobs_queue) - 1)] = (
            job_start_time,
            min_finish_time,
            max(0, min_finish_time - job.deadline),
            job.job_id
    )

    total_tardiness = sum(max(0, job_times[key][1] - job.deadline) for key in job_times)

    # Print start and finish times with tardiness for each job
    print("Job Schedule:")
    for machine_id, position in job_times.keys():
        times = job_times[(machine_id, position)]  # Access tuple elements by index
        print(
            f"Job {times[3]}: Start Time: {times[0]}, End Time: {times[1]}, Tardiness: {times[2]}")
    print(final_solution)
    print(job_times)
    print(total_tardiness)
    return final_solution, job_times, total_tardiness


num_machines_erl = 3
num_machines_kz = 8
num_machines_xl = 4

jobs_erl = jobs_list_erl
jobs_kz = jobs_list_kz
jobs_xl = jobs_list_xl

    # Create machines for each type
machines_erl = [Machine(value) for value in range(num_machines_erl)]
machines_kz = [Machine(value) for value in range(num_machines_kz)]
machines_xl = [Machine(value) for value in range(num_machines_xl)]


    # Call greedy algorithm for each type of job
start_time_erl = time.time()
final_solution_erl, job_times_greedy_erl, total_tardiness_erl = greedy_algorithm(jobs_erl, machines_erl, calculate_setup_time_change_ERL)
end_time_erl = time.time()

time_elapsed_erl = end_time_erl - start_time_erl
print("Time elapsed for ERL:", time_elapsed_erl, "seconds")

start_time_kz= time.time()
final_solution_kz, job_times_greedy_kz, total_tardiness_kz = greedy_algorithm(jobs_kz, machines_kz, calculate_setup_time_change_KZ)
end_time_kz = time.time()

time_elapsed_kz = end_time_kz - start_time_kz
print("Time elapsed for KZ:", time_elapsed_kz, "seconds")

start_time_xl = time.time()
final_solution_xl, job_times_greedy_xl, total_tardiness_xl = greedy_algorithm(jobs_xl, machines_xl, calculate_setup_time_change_XL)
end_time_xl = time.time()

time_elapsed_xl = end_time_xl - start_time_xl
print("Time elapsed for XL:", time_elapsed_xl, "seconds")





