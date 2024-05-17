from job_creator.jobsFromDb import *


class Machine:
    # To generate sequentially increasing machine IDs
    machine_id_count = 0
    def __init__(self):
        Machine.machine_id_count += 1
        self.machine_id = Machine.machine_id_count
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
        job.job_finish_time = min_finish_time

        # Calculate start time considering previous job
        job_start_time = best_machine.finish_time - job.processing_time

        # Store start and finish times for the job
        job_times[job.job_id] = {
            'start_time': job_start_time,
            'finish_time': min_finish_time,
            'tardiness': max(0, min_finish_time - job.deadline)
        }


    total_tardiness = sum(job_times[job_id]['tardiness'] for job_id in job_times)

    # Print start and finish times with tardiness for each job
    print("Job Schedule:")
    for job_id, times in job_times.items():
        print(
            f"Job {job_id}: Start Time: {times['start_time']}, Finish Time: {times['finish_time']}, Tardiness: {times['tardiness']}")

    return total_tardiness

if __name__ == "__main__":
    num_machines_erl = 3
    num_machines_kz = 8
    num_machines_xl = 4
    # Example implementation
    jobs_erl = jobs_list_erl
    jobs_kz = jobs_list_kz
    jobs_xl = jobs_list_xl


    machines_erl = [Machine() for _ in range(num_machines_erl)]
    tardiness_erl = greedy_algorithm(jobs_erl, machines_erl, calculate_setup_time_change_ERL)
    print("Total tardiness for ERL:", tardiness_erl)
    print("Jobs in machines for ERL: ")
    for machine in machines_erl:
        machine.display_queue()

    machines_kz = [Machine() for _ in range(num_machines_kz)]
    tardiness_kz = greedy_algorithm(jobs_kz, machines_kz, calculate_setup_time_change_KZ)
    print("Total tardiness for KZ:", tardiness_kz)
    print("Jobs in machines for KZ: ")
    for machine in machines_kz:
        machine.display_queue()

    machines_xl = [Machine() for _ in range(num_machines_xl)]
    tardiness_xl = greedy_algorithm(jobs_xl, machines_xl, calculate_setup_time_change_XL)
    print("Total tardiness for XL:", tardiness_xl)
    print("Jobs in machines for XL: ")
    for machine in machines_xl:
        machine.display_queue()