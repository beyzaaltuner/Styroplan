# __________INITIALIZE__________
# Randomize the initially defined jobs using shuffle.
# Assign each job to a machine.
# Assign each job -gene- to a unique position within its assigned machine.
# Machine --> Dictionary: Key --> machine ID, Value --> dictionary: holds processing time for that machine.

# __________FITNESS AND TARDINESS EVALUATION__________
# Calculates the fitness of a chromosome based on the tardiness criterion --> the maximum completion time among all machines.
# Initialize Tardiness list --> with zeros (the length of the list == the number of machines) --> finish time of each machine.
# The finish time - job's deadline --> tardiness: If the job finishes before its deadline --> tardiness == 0; otherwise --> the difference.
# Calculate tardiness for each machine. Then sum up the tardiness values for all machines = total tardiness of the chromosome.
# Return the total tardiness as the fitness value of the chromosome.

# __________CROSSOVER__________
# Randomly select a parent to determine dominant genes
# Generate a random parent string of zeros and ones --> the length == the length of the parent chromosomes

# =====OFFSPRING1=====
# First for the parent string find the indices where the value equals 1 and get the gene from parent1.
# Then fill the same index of offspring1 with that gene.
# Then find the indices with value 0, select the genes from parent2.
# Start from the beginning of the parent2.
# -->If the job in that index is not assigned in the offspring1 from parent1 before, add that gene to offspring1 where the index equals to the index of the parent string.
# -->If assigned move to the next index of the parent2.
# Fill all the empty indices of offspring1.

# =====OFFSPRING2=====
# For the offspring2, we will be repeating the same procedure but this time the dominant value will be 0.
# First for the parent string find the indices where the value equals 0 and get the gene from parent2.
# Then fill the same index of offspring2 with that gene.
# Then find the indices with value 1, select the genes from parent1.
# Start from the beginning of the parent1.
# -->If the job in that index is not assigned in the offspring2 from parent2 before, add that gene to offspring2 where the index equals to the index of the parent string.
# -->If assigned move to the next index of the parent1.
#  Fill all the empty indices of offspring2.

# ????? Probability of each position = 0.5 is not included ?????

# __________MUTATION__________
# Initialize mutated_chromosome --> a copy of the input chromosome.
# Iterates over each gene in the chromosome

import random
import time

from job_creator.jobsFromDb import *


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


def initialize_population(population_size, num_machines, jobs):
    population = []
    for _ in range(population_size):

        random.shuffle(jobs)
        chromosome = []
        for job in jobs:
            machine = random.randint(0, num_machines - 1)
            position = len([gene for gene in chromosome if gene[
                1] == machine])
            chromosome.append([job.job_id, machine, position])
        population.append(chromosome)

    return population


def calculate_fitness_1(chromosome, machines):
    # Initialize variables
    machine_finish_times = [0] * len(machines)
    total_tardiness = 0
    penalty_factor = 1000  # Adjust as needed

    # Track assigned positions on each machine
    assigned_positions = {machine: set() for machine in machines.keys()}

    # print(f"Current chromosome: {chromosome}")
    for i, gene in enumerate(chromosome):
        job_id, machine, position = gene

        # Check if the position is already assigned
        if position in assigned_positions[machine]:
            # Penalize the chromosome for assigning multiple jobs to the same position on the same machine
            total_tardiness += penalty_factor
        else:
            current_job = machines[machine][job_id]
            setup_time = 0

            # if not the first job in the chromosome, should calculate the setup
            if i > 0:
                # Get the previous job
                previous_gene = chromosome[i - 1]
                previous_job = machines[previous_gene[1]][previous_gene[0]]
                setup_time = calculate_setup_time_change_KZ(previous_job, current_job)

            # Update machine finish time and check tardiness
            machine_finish_times[machine] += machines[machine][job_id].processing_time + setup_time
            job_tardiness = max(0, machine_finish_times[machine] - machines[machine][job_id].deadline)
            total_tardiness += job_tardiness
            # Update assigned positions
            assigned_positions[machine].add(position)

    # print(f"Total tardiness of this chromosome is {total_tardiness} \n")

    return total_tardiness


def calculate_fitness(chromosome, machines, calculate_setup_time_func):
    # Initialize variables
    machine_finish_times = [0] * len(machines)
    total_tardiness = 0
    penalty_factor = 1000  # Adjust as needed

    # Track assigned positions on each machine
    assigned_positions = {machine: set() for machine in machines.keys()}

    # Sort jobs assigned to each machine based on their positions
    sorted_solution = []
    for machine_id in range(len(machines)):
        jobs_on_machine = [gene for gene in chromosome if gene[1] == machine_id]
        sorted_jobs = sorted(jobs_on_machine, key=lambda x: x[2])  # Sort based on position
        sorted_solution.extend(sorted_jobs)

    for i, gene in enumerate(sorted_solution):
        job_id, machine, position = gene
        job = machines[machine][job_id]

        # Check if the position is already assigned
        if position in assigned_positions[machine]:
            # Penalize the chromosome for assigning multiple jobs to the same position on the same machine
            total_tardiness += penalty_factor
        else:
            setup_time = 0
            if i != 0:
                # Get the previous job
                previous_gene = sorted_solution[i - 1]
                previous_job = machines[previous_gene[1]][previous_gene[0]]
                if previous_gene[1] == gene[1]:
                    setup_time = calculate_setup_time_func(previous_job, job)
                else:
                    setup_time = 0
            # Update machine finish time
            start_time = machine_finish_times[machine] + setup_time
            end_time = start_time + job.processing_time

            # Check tardiness
            job_tardiness = max(0, end_time - job.deadline)
            total_tardiness += job_tardiness

            # Update machine finish time for the next job
            machine_finish_times[machine] = end_time

            # Update assigned positions
            assigned_positions[machine].add(position)

    return total_tardiness


# Perform crossover to produce offsprings
def crossover(parent1, parent2):
    offspring1 = [None] * len(parent1)  # [None, None, None, None, None, None, None, None]
    offspring2 = [None] * len(parent2)  # [None, None, None, None, None, None, None, None]

    parent_string = [random.randint(0, 1) for _ in range(len(parent1))]
    #print(f"Random String: {parent_string}")

    # Offspring1 --> Dominant parent string value : 1
    for i in range(len(parent_string)):
        if parent_string[i] == 1:
            offspring1[i] = parent1[i]
        else:
            offspring1[i] = None

    # Fill empty indices of offspring1
    offspring1_job_ids = [gene[0] for gene in offspring1 if gene is not None]
    for i in range(len(offspring1)):
        if offspring1[i] is None:
            for gene in parent2:
                if gene[0] not in offspring1_job_ids:
                    offspring1[i] = gene
                    offspring1_job_ids.append(gene[0])
                    break

    # Offspring2 --> Dominant parent string value : 0
    for i in range(len(parent_string)):
        if parent_string[i] == 0:
            offspring2[i] = parent2[i]
        else:
            offspring2[i] = None

    # Fill empty indices of offspring2
    offspring2_job_ids = [gene[0] for gene in offspring2 if gene is not None]
    for i in range(len(offspring2)):
        if offspring2[i] is None:
            for gene in parent1:
                if gene[0] not in offspring2_job_ids:
                    offspring2[i] = gene
                    offspring2_job_ids.append(gene[0])
                    break

    # Print offsprings
    #print("Offspring 1:", offspring1)
    #print("Offspring 2:", offspring2)
    return offspring1, offspring2


# Apply mutation to the chromosome (Shuffle job ids)
def mutate(chromosome, mutation_rate):
    mutated_chromosome = chromosome[:]

    job_ids = [gene[0] for gene in chromosome]
    print(job_ids)
    if random.random() < mutation_rate:
        mutated_chromosome = []
        for gene in chromosome:

            random_index = random.randint(0, len(job_ids) - 1)
            job_id = job_ids[random_index]
            mutated_gene = [job_id, gene[1], gene[2]]
            job_ids.remove(job_id)
            mutated_chromosome.append(mutated_gene)
    return mutated_chromosome


# Apply mutation to the chromosome (Shuffle positions in the same machine)
def mutate2(chromosome, mutation_rate):
    mutated_chromosome = chromosome[:]
    machine_assignments = {gene[1]: [] for gene in chromosome}

    if random.random() < mutation_rate:
        # Gather job positions by machine
        for gene in chromosome:
            _, machine_id, position = gene
            machine_assignments[machine_id].append(position)

        # Shuffle job positions within each machine
        for machine_id, positions in machine_assignments.items():
            random.shuffle(positions)
            for gene in mutated_chromosome:
                if gene[1] == machine_id:
                    gene[2] = positions.pop(0)  # Assign shuffled positions back to genes

    return mutated_chromosome


def genetic_algorithm(population_size, mutation_rate, max_generations, num_machines, jobs, calculate_setup_time_func):
    population = initialize_population(population_size, num_machines, jobs)
    machines = {i: {} for i in range(num_machines)}

    for job in jobs:
        for machine_schedule in machines.values():
            machine_schedule[job.job_id] = job

    for generation in range(max_generations):
        fitness_scores = [calculate_fitness(chromosome, machines, calculate_setup_time_func) for chromosome in
                          population]

        penalty_indices = [i for i, score in enumerate(fitness_scores) if score >= 1000]
        for index in sorted(penalty_indices, reverse=True):
            del population[index]
            del fitness_scores[index]

        selected_parents = [population[i] for i in sorted(range(len(population)), key=lambda x: fitness_scores[x])[:2]]

        parent1, parent2 = selected_parents[0], selected_parents[1]
        child1, child2 = crossover(parent1, parent2)

        if child1 not in population:
            population.append(child1)
        if child2 not in population:
            population.append(child2)

        child1 = mutate2(child1, mutation_rate)
        child2 = mutate2(child2, mutation_rate)

        if child1 not in population:
            population.append(child1)
        if child2 not in population:
            population.append(child2)

        if 0 in fitness_scores:
            break

    best_solution_index = fitness_scores.index(min(fitness_scores))
    best_solution = population[best_solution_index]
    tardiness = calculate_fitness(best_solution, machines, calculate_setup_time_func)
    print(
        f"Total tardiness in the found solution: {calculate_fitness(best_solution, machines, calculate_setup_time_func)}")

    job_times = calculate_start_and_end_times(best_solution, machines, calculate_setup_time_func)

    return best_solution, job_times, tardiness # Return both the best solution and job times




def calculate_start_and_end_times(best_solution, machines, calculate_setup_time_func):
    # Sort jobs assigned to each machine based on their positions
    sorted_solution = []
    for machine_id in range(len(machines)):
        jobs_on_machine = [gene for gene in best_solution if gene[1] == machine_id]
        sorted_jobs = sorted(jobs_on_machine, key=lambda x: x[2])  # Sort based on position
        sorted_solution.extend(sorted_jobs)

    job_times = {}  # Dictionary to store start and end times of jobs
    machine_finish_times = [0] * len(machines)  # Initialize finish times for each machine

    # Iterate over each gene in the sorted solution
    for i, gene in enumerate(sorted_solution):
        job_id, machine_id, position = gene
        job = machines[machine_id][job_id]
        setup_time = 0

        if i != 0:
            # Get the previous job
            previous_gene = sorted_solution[i - 1]
            previous_job = machines[previous_gene[1]][previous_gene[0]]
            if previous_gene[1] == gene[1]:
                setup_time = calculate_setup_time_func(previous_job, job)

        start_time = machine_finish_times[machine_id] + setup_time
        end_time = start_time + job.processing_time
        machine_finish_times[machine_id] = end_time  # Update machine finish time


        job_tardiness = max(0, end_time - job.deadline)
        job_times[(machine_id, position)] = (start_time, end_time, job_tardiness, job_id)

        # Print job details
        print(f"Job {job_id}: Start Time={start_time}, End Time={end_time}, Tardiness={job_tardiness} on Machine {machine_id}")

    return job_times




population_size = 1000
mutation_rate = 0.1
max_generations = 100

num_machines_erl = 3
num_machines_kz = 8
num_machines_xl = 4
# Example implementation
jobs_erl = jobs_list_erl
jobs_kz = jobs_list_kz
jobs_xl = jobs_list_xl

start_time_erl = time.time()
best_solution_erl, job_times_erl, tardiness_erl = genetic_algorithm(population_size, mutation_rate, max_generations, num_machines_erl,
                                                     jobs_erl, calculate_setup_time_change_ERL)
end_time_erl = time.time()
print("Best solution for ERL:", best_solution_erl)
print("Job times for ERL:", job_times_erl)
print("Tardiness for ERL:", tardiness_erl)

start_time_kz= time.time()
best_solution_kz, job_times_kz, tardiness_kz = genetic_algorithm(population_size, mutation_rate, max_generations, num_machines_kz,
                                                   jobs_kz, calculate_setup_time_change_KZ)
end_time_kz= time.time()

print("Best solution for KZ:", best_solution_kz)
print("Job times for KZ:", job_times_kz)
print("Tardiness for KZ:", tardiness_kz)

start_time_xl = time.time()
best_solution_xl, job_times_xl, tardiness_xl = genetic_algorithm(population_size, mutation_rate, max_generations, num_machines_xl,
                                                   jobs_xl, calculate_setup_time_change_XL)
end_time_xl = time.time()

print("Best solution for XL:", best_solution_xl)
print("Job times for XL:", job_times_xl)
print("Tardiness for XL:", tardiness_xl)



time_elapsed_erl = end_time_erl - start_time_erl
time_elapsed_kz = end_time_kz - start_time_kz
time_elapsed_xl = end_time_xl - start_time_xl
print("Time elapsed for ERL:", time_elapsed_erl, "seconds")
print("Time elapsed for KZ:", time_elapsed_kz, "seconds")
print("Time elapsed for XL:", time_elapsed_xl, "seconds")








