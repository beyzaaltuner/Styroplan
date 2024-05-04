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
from job_creator.jobs import *


class Job:
    def __init__(self, job_id, processing_time, deadline):
        self.job_id = job_id
        self.processing_time = processing_time
        self.deadline = deadline


def initialize_population(population_size, num_machines, jobs):
    population = []
    for _ in range(population_size):
        # Shuffle jobs to ensure that each chromosome starts with a different permutation of jobs.
        random.shuffle(jobs)
        chromosome = []
        for job in jobs:
            machine = random.randint(0, num_machines - 1)  # Randomly assigns a machine index to the job
            position = len([gene for gene in chromosome if gene[
                1] == machine])  # Counts the number of existing genes (jobs) on the same machine within the chromosome
            chromosome.append([job.job_id, machine, position])
        population.append(chromosome)

    print(f"Initial Population: {population}")
    return population


def calculate_fitness(chromosome, machines):
    # Initialize variables
    machine_finish_times = [0] * len(machines)
    total_tardiness = 0
    penalty_factor = 1000  # Adjust as needed

    # Track assigned positions on each machine
    assigned_positions = {machine: set() for machine in machines.keys()}

    # print(f"Current chromosome: {chromosome}")
    for gene in chromosome:
        job_id, machine, position = gene

        # Check if the position is already assigned
        if position in assigned_positions[machine]:
            # Penalize the chromosome for assigning multiple jobs to the same position on the same machine
            total_tardiness += penalty_factor
        else:
            # Update machine finish time and check tardiness
            machine_finish_times[machine] += machines[machine][job_id].processing_time
            job_tardiness = max(0, machine_finish_times[machine] - machines[machine][job_id].deadline)
            total_tardiness += job_tardiness
            # Update assigned positions
            assigned_positions[machine].add(position)

    # print(f"Total tardiness of this chromosome is {total_tardiness} \n")

    return total_tardiness


# Perform crossover to produce offsprings
def crossover(parent1, parent2):
    offspring1 = [None] * len(parent1)  # [None, None, None, None, None, None, None, None]
    offspring2 = [None] * len(parent2)  # [None, None, None, None, None, None, None, None]

    parent_string = [random.randint(0, 1) for _ in range(len(parent1))]
    print(f"Random String: {parent_string}")

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
    print("Offspring 1:", offspring1)
    print("Offspring 2:", offspring2)
    return offspring1, offspring2


# Apply mutation to the chromosome (Shuffle job ids)
def mutate(chromosome, mutation_rate):
    print(f"Chromosome before mutation: {chromosome}")
    mutated_chromosome = chromosome[:]

    job_ids = [gene[0] for gene in chromosome]
    print(job_ids)
    if random.random() < mutation_rate:
        mutated_chromosome = []
        for gene in chromosome:
            print(f"Mutation in progress...")
            random_index = random.randint(0, len(job_ids)-1)
            job_id = job_ids[random_index]
            mutated_gene = [job_id, gene[1], gene[2]]
            job_ids.remove(job_id)
            mutated_chromosome.append(mutated_gene)
    print(f"Chromosome after mutation: {mutated_chromosome}")
    return mutated_chromosome


# Apply mutation to the chromosome (Shuffle positions in the same machine)
def mutate2(chromosome, mutation_rate):
    print(f"Chromosome before mutation: {chromosome}")
    mutated_chromosome = chromosome[:]
    machine_assignments = {gene[1]: [] for gene in chromosome}

    if random.random() < mutation_rate:
        print(f"Mutation in progress...")
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

    print(f"Chromosome after mutation: {mutated_chromosome}")
    return mutated_chromosome


def genetic_algorithm(population_size, mutation_rate, max_generations, num_machines, jobs):
    population = initialize_population(population_size, num_machines, jobs)
    machines = {i: {} for i in range(num_machines)}  # {0: {}, 1: {}, 2: {}}

    for job in jobs:
        for machine_schedule in machines.values():
            machine_schedule[job.job_id] = job
    print(f"Machines after filling dictionary {machines}")

    for generation in range(max_generations):
        # Evaluate fitness
        fitness_scores = [calculate_fitness(chromosome, machines) for chromosome in population]

        # Find indices of chromosomes with penalties
        penalty_indices = [i for i, score in enumerate(fitness_scores) if score >= 1000]

        # Remove chromosomes with very big fitness value from the population
        for index in sorted(penalty_indices, reverse=True):
            del population[index]
            del fitness_scores[index]

        print(f"Population after deleting chromosomes with penalty {population}")
        print(f"Fitness values after deleting chromosomes with penalty {fitness_scores}")

        # Perform selection
        selected_parents = [population[i] for i in sorted(range(len(population)), key=lambda x: fitness_scores[x])[:2]]
        print(f"Selected parents: {selected_parents}")

        # Check parents' fitness values
        print(f"Fitness values of parents: \nParent 1: {calculate_fitness(selected_parents[0], machines)}\nParent 2: {calculate_fitness(selected_parents[1], machines)}")

        # Perform crossover
        parent1 = selected_parents[0]
        parent2 = selected_parents[1]
        child1, child2 = crossover(parent1, parent2)
        if child1 not in population:
            population.append(child1)

        if child2 not in population:
            population.append(child2)

        # Apply mutation to the offspring chromosomes
        child1 = mutate2(child1, mutation_rate)
        child2 = mutate2(child2, mutation_rate)

        # Add mutated offspring to the population if they are not already present
        if child1 not in population:
            population.append(child1)

        if child2 not in population:
            population.append(child2)

        print(f"Population after mutation is performed {population}")
        print(f"Fitness values after mutation is performed {fitness_scores}")

        # Termination condition
        if 0 in fitness_scores:
            break

    # Return the best solution found
    best_solution_index = fitness_scores.index(min(fitness_scores))
    best_solution = population[best_solution_index]
    print(f"Total tardiness in the found solution: {calculate_fitness(best_solution, machines)}")
    return best_solution


# Example implementation
jobs = initialize_jobs_from_database(cursor)
population_size = 1000
mutation_rate = 0.1
max_generations = 100
num_machines = 3

best_solution = genetic_algorithm(population_size, mutation_rate, max_generations, num_machines, jobs)
print("Best solution:", best_solution)