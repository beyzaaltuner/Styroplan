from pyomo.environ import *
from job_creator.jobsFromDb import *

def max_zero(x):
    return x if x >= 0 else 0

data = {
    'J': {1, 2, 3, 4, 5, 6, 7, 8, 9},
    'ID': {1: 23575832, 2: 23477358, 3: 23799694, 4: 23799694, 5: 23469288,  6: 23469287, 7: 23364110, 8: 23525756, 9: 23364110},  # Jobs id
    'ID_D': {1: 31, 2: 110, 3: 13, 4: 110, 5: 55, 6: 49, 7: 49, 8: 110, 9: 80},
    'ID_E': {1: 7, 2: 50, 3: 67, 4: 55, 5: 55, 6: 85, 7: 110, 8: 43, 9: 7},
    'ID_SIZE': {1: 1, 2: 1, 3: 3, 4: 1, 5: 3, 6: 3, 7: 3, 8: 1, 9: 2},
    'L': {"KZ1", "KZ2", "KZ3", "KZ4", "KZ5", "KZ6", "KZ7", "KZ8"},  # Machines
    'K': {1, 2, 3, 4, 5, 6, 7, 8, 9},  # Positions
    'di': {1: 9, 2: 4, 3: 5, 4: 3, 5: 6, 6: 2, 7: 1, 8: 6, 9: 5},  # due dates
    'pi': {1: 5, 2: 5, 3: 6, 4: 4, 5: 7, 6: 10, 7: 3, 8: 4, 9: 5},  # process times
}
#jobs_kz = jobs_list_kz

#job_ids = {job.job_id for job in jobs_kz}
#data['J'] = job_ids

#job_id_to_code = {job.job_id: job.code for job in jobs_kz}
#data['ID'] = job_id_to_code

#job_id_to_deadlines = {job.job_id : job.deadline for job in jobs_kz}
#data['di'] = job_id_to_deadlines

#job_id_to_process_times = {job.job_id : job.processing_time for job in jobs_kz}
#data['pi'] = job_id_to_process_times

model = ConcreteModel()

# Sets
model.J = Set(initialize=data['J'])  # jobs
model.L = Set(initialize=data['L'])  # machines
model.K = Set(initialize=data['K'])  # position

# Parameters
model.di = Param(model.J, initialize=data['di'])
model.pi = Param(model.J, initialize=data['pi'])

def tij_init(model, i, j):
    new_set_up_time = 0  # Initialize new_set_up_time
    size_change = abs(data['ID_SIZE'][i] - data['ID_SIZE'][j])

    if size_change == 0:
        if data['ID_D'][i] != data['ID_D'][j]:
            new_set_up_time += 2
        else:
            if data['ID_E'][i] != data['ID_E'][j]:
                new_set_up_time += 1

    else:
        if size_change == 1:
            new_set_up_time += 4
        elif size_change == 2:
            new_set_up_time += 6

    return new_set_up_time

# Initialize tij parameter
model.tij = Param(model.J, model.J, initialize=tij_init)

# Big M constant
M = 1000  # large constant

# Decision variables
model.si = Var(model.J, within=NonNegativeReals)
model.fi = Var(model.J, within=NonNegativeReals)
model.ui = Var(model.J, within=NonNegativeReals)
model.yilk = Var(model.J, model.L, model.K, within=Binary)
model.xij = Var(model.J, model.J, within=Binary)
model.tardiness = Var(model.J, within=NonNegativeReals)

# Objective is to minimize tardiness
def objective_rule(model):
    return sum(model.tardiness[i] for i in model.J)
model.Objective = Objective(rule=objective_rule, sense=minimize)

# All jobs should assign to a machine, no jobs left (1)
def assign_to_machine_constraint(model, i):
    return sum(model.yilk[i, l, k] for l in model.L for k in model.K) == 1
model.assign_to_machine_constraint = Constraint(model.J, rule=assign_to_machine_constraint)

# At most one job i can be assigned to a machine l at a specific position k (2)
def unique_order_constraint(model, i, l, k):
    return sum(model.yilk[i, l, k] for i in model.J) <= 1
model.unique_order_constraint = Constraint(model.J, model.L, model.K, rule=unique_order_constraint)

# Job precedence constraint (3)
def job_precedence_constraint(model, l, k):
    if k > 1:
        return sum(model.yilk[i, l, k] for i in model.J) - sum(model.yilk[i, l, k - 1] for i in model.J) <= 0
    else:
        return Constraint.Skip
model.job_precedence_constraint = Constraint(model.L, model.K, rule=job_precedence_constraint)

# Job sequence position constraint (4)
def job_sequence_position_constraint(model, i, j, k, l):
    if k > 1 and i != j:
        return model.yilk[j, l, k] + model.yilk[i, l, k - 1] - model.xij[i, j] <= 1
    else:
        return Constraint.Skip
model.JobSequencePositionConstraint = Constraint(model.J, model.J, model.K, model.L, rule=job_sequence_position_constraint)

# Start time order constraint (6)
def start_time_order_constraint(model, i, j):
    if i != j:
        return model.si[j] >= model.fi[i] + model.tij[i, j] - M * (1 - model.xij[i, j])
    else:
        return Constraint.Skip
model.start_time_order_constraint = Constraint(model.J, model.J, rule=start_time_order_constraint)

# Tardiness constraint (7)
def tardiness_constraint(model, i):
    return model.tardiness[i] >= model.fi[i] - model.di[i]
model.TardinessConstraint = Constraint(model.J, rule=tardiness_constraint)

# Completion time constraint (5)
def completion_time_constraint(model, i):
    return model.fi[i] == model.si[i] + model.pi[i] * sum(model.yilk[i, l, k] for l in model.L for k in model.K)
model.completion_time_constraint = Constraint(model.J, rule=completion_time_constraint)


solver = SolverFactory('gurobi')
solver.solve(model)

# Display results
job_sequence = [(i, value(model.fi[i])) for i in model.J]
job_sequence.sort(key=lambda x: x[1])  # Sort jobs based on finish times

print("Optimal job sequence:")
for i, finish_time in job_sequence:
    tardiness_value = max_zero(finish_time - model.di[i])
    assigned_machine = None
    for l in model.L:
        for k in model.K:
            if model.yilk[i, l, k].value == 1:
                assigned_machine = l
                break
        if assigned_machine:
            break
    print(f"Job {i}: Start Time = {value(model.si[i])}, Finish Time = {finish_time}, Tardiness = {tardiness_value}, Process Time = {model.pi[i]}, Machine = {assigned_machine}")

total_tardiness = sum(max_zero(job[1] - model.di[job[0]]) for job in job_sequence)
print("Total Tardiness:", total_tardiness)

# Display variable values
for v in model.component_objects(Var, active=True):
    print("Variable", v)
    varobject = getattr(model, str(v))
    for index in varobject:
        print(" ", index, varobject[index].value)