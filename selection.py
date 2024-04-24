import random
from utils import fitness_function



def ranking_selection(pop, tor_size, data, problem, constraints, w_penalty):

    """

    Ranking Selection: Individuals are sorted based on their fitness.
                       Only takes into account a position on the raking and not the value itself.

    Parameters:

        pop: population at time t

        data: list with the information of the ingredients

        problem: max or min

    Output: One individual

    """

    fitness_values = []
    selection_prob = []

    for individual in pop:
        fitness_values.append((individual, fitness_function(individual, pop, data, constraints, w_penalty)))

    # Maximize the problem -> higher fitness = last ranking
    if problem == 'max':

        fitness_values = sorted(fitness_values, key=lambda x: x[1])

    # Minimize the problem -> lower fitness = last ranking
    elif problem == 'min':

        fitness_values = sorted(fitness_values, key=lambda x: x[1], reverse= True)

    # Using a linear function for selection: probability of selection per individual
    for index, fitness_value in enumerate(fitness_values):
        selection_prob.append((fitness_value[0], (index+1)/((len(fitness_values)))))

    # Select a random individual
    selec_flag = 0
    while selec_flag != 1:

        new_indv = random.choice(selection_prob)
        num = random.uniform(0,1)

        if new_indv[1] > num:
            selec_flag = 1

    return new_indv[0]

def roulette_selection(pop, tor_size, data, problem, constraints,w_penalty):

    """

        Roulette Selection: Probability of a given individual is its fitness divided by the total fitness. (Max)


        Parameters:

            pop: population at time t

            data: list with the information of the ingredients

            problem: max or min

        Output: One individual

    """

    fitness_values = []

    # Get the fitness values
    for individual in pop:
        fitness_values.append(fitness_function(individual, pop, data, constraints, w_penalty))

    if problem == "min":

        # Sum total fitness
        total_fitness = sum(fitness_values)
        # Get a 'position' on the wheel
        total = sum([total_fitness/fitness for fitness in fitness_values])
        spin = random.uniform(0, total)
        position = 0
        # Find individual in the position of the spin
        for individual in pop:
            position += total_fitness/fitness_function(individual, pop, data, constraints, w_penalty)
            if position > spin:
                return individual

    if problem == 'max':

        # Sum total fitness
        total_fitness = sum(fitness_values)
        # Get a 'position' on the wheel
        spin = random.uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in pop:
            position += fitness_function(individual, pop, data, constraints, w_penalty)
            if position > spin:
                return individual


def tournament_selection(population, tour_size, data, problem, constraints, w_penalty):

    """

        Tournament selection: n individuals are randomly selected - with repetition - to compete.
                              The individual with the best fitness wins and is selected.

        Parameters:

            pop: population at time t

            data: list with the information of the ingredients

            tour_size: tournament size. How many individuals should participate.

            problem: max or min

        Output: The individual that wins the tournament

    """

    tournament = [random.randint(0, len(population)-1) for _ in range(tour_size)]
    fitness_values = []

    for individual in tournament:
        fitness_values.append(fitness_function(population[individual], population, data, constraints, w_penalty))

    if problem == "max":
        return population[tournament[fitness_values.index(max(fitness_values))]]
        print(population[tournament[fitness_values.index(max(fitness_values))]])
    if problem == "min":
        return population[tournament[fitness_values.index(min(fitness_values))]]
