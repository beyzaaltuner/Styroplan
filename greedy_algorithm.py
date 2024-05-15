import math

class Job:
    def __init__(self, job_id, processing_time, deadline):
        self.job_id = job_id
        self.processing_time = processing_time
        self.deadline = deadline
        self.job_finish_time = None

    def __str__(self):
        return str(self.job_id) + " "

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
            print(job)
        print("\n")


def greedy_algorithm(jobs, num_machines):
    # Initialize machines
    machines = [Machine() for _ in range(num_machines)]


    # Sort jobs by deadlines in ascending order (Earliest Due Date)
    jobs.sort(key=lambda x: x.deadline)

    print("Jobs after being sorted by deadlines:")
    for j in jobs:
        print(j.__str__())


    # Assign jobs to machines considering finish time (workload) balance
    for job in jobs:
        # Sort machines by finish_time (workload)
        machines.sort(key=lambda x: x.finish_time)

        print("Machines and their finish times after sorting :")
        for mc in machines:
            print(f"Machine {mc.machine_id} and its current finish time: {mc.finish_time}")

        # Since machines are sorted according to finish time, first one in the list has the minimum finsh time
        min_finish_time_machine = machines[0]
        min_finish_time_machine.finish_time += job.processing_time
        min_finish_time_machine.jobs_queue.append(job)
        job.job_finish_time = min_finish_time_machine.finish_time

        print(f"Job {job.__str__()} has the finish time of: {job.job_finish_time} and its deadline is: {job.deadline}")


    # Calculate tardiness
    total_tardiness = 0
    for machine in machines:
        for job in machine.jobs_queue:
            if job.job_finish_time > job.deadline:
                # Calculate job's tardiness
                job_tardiness = job.job_finish_time - job.deadline

                # Add the job's tardiness to the total tardiness
                total_tardiness += job_tardiness

    return total_tardiness, machines

jobs = [Job(1, 4, 13), Job(2, 4, 13), Job(3, 4, 13), Job(4, 4, 13), Job(5, 4, 13), Job(6, 4, 3), Job(7, 4, 3), Job(8, 4, 3)]
number_of_machines = 3
total_tardiness, machines = greedy_algorithm(jobs, number_of_machines)
print("Total tardiness", total_tardiness)
print("Jobs in machines: ")
for machine in machines:
    machine.display_queue()