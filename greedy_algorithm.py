from job_creator.jobsFromDb import *

class Machine:
    machine_id_count = 0  # To generate unique machine IDs
    def __init__(self):
        Machine.machine_id_count += 1
        self.machine_id = Machine.machine_id_count
        self.finish_time = 0
        self.jobs_queue = []

    def display_queue(self):
        print(f"Machine {self.machine_id} Queue:")
        for job in self.jobs_queue:
            print(job)
        print("\n")


def greedy_algorithm(jobs, num_machines):
    machines = [Machine() for _ in range(num_machines)]  # Initialize machines

    initial_jobs = initial_jobs_erl

    # Initially each machine has a job assigned
    for i, job in enumerate(initial_jobs[:num_machines]):
        machines[i % num_machines].finish_time += job.processing_time
        machines[i % num_machines].jobs_queue.append(job)
        job.job_finish_time = machines[i % num_machines].finish_time

    print("Queue after first initialization")
    for m in machines:
        m.display_queue()

    jobs.sort(key=lambda x: x.deadline)  # Sort jobs by deadlines in ascending order (Earliest Due Date)

    print("Jobs after being sorted by deadlines:")
    for j in jobs:
        print(j.job_id)


    # Assign jobs to machines considering workload balance
    for job in jobs:
        # Sort machines by finish_time/workload
        machines.sort(key=lambda x: x.finish_time)

        print("Machines and their finish times after sorting :")
        for mc in machines:
            print(f"Machine {mc.machine_id} and its current finish time: {mc.finish_time}")

        min_finish_time_machine = machines[0]  # Since machines are sorted according to finish time, first one in the list has the minimum finsh time
        min_finish_time_machine.finish_time += job.processing_time
        min_finish_time_machine.jobs_queue.append(job)
        job.job_finish_time = min_finish_time_machine.finish_time

        print(f"Job {job.job_id} has the finish time of: {job.job_finish_time} and its deadline is: {job.deadline}")


    # Calculate tardiness
    total_tardiness = 0
    for machine in machines:
        for job in machine.jobs_queue:
            if job.job_finish_time > job.deadline:
                job_tardiness = job.job_finish_time - job.deadline  # Calculate job's tardiness
                total_tardiness += job_tardiness  # Add the job's tardiness to the total tardiness

    return total_tardiness, machines


jobs = jobs_list_erl


number_of_machines = 3
total_tardiness, machines = greedy_algorithm(jobs, number_of_machines)
print("Total tardiness", total_tardiness)
print("Jobs in machines: ")
for machine in machines:
    machine.display_queue()