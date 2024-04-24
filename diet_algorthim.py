import random
from data import data, nutrients
from population_initial import initial_pop
from selection import ranking_selection, roulette_selection, tournament_selection
from crossover import onePoint_Crossover, shuffle_Crossover, arithmetic_Crossover
from mutation import inversion_mutation, scramble_mutation, swap_mutation
from utils import fitness_function
import statistics
import csv

def nutrient_intake(nutrients,individual, data):

    ingest_value = 0
    for count_constrain in range(len(nutrients)):
        for ingredient in individual:
            # Calculated the total intake of a certain nutrient per individual
            ingest_value += data[ingredient][count_constrain + 2]
    return ingest_value


def evolution(init_pop, gens, repro_prob, mut_prob, select_function, crossover_function, mutate_function, elitism, problem,w_penalty, fitness_constraint=True, cross_constraint=False):
    # store the actual population
    act_pop = []
    # Store the median information per generation
    med_fitness_gen = []
    # Generations to create
    for i in range(gens):
        new_pop = []
        counts = {}
        if i == 0:
            fitness_gen = []
            act_pop = init_pop
            for individual in act_pop:
                fitness_gen.append(fitness_function(individual, act_pop, data, fitness_constraint, w_penalty))
            med_fitness_gen.append(statistics.median(fitness_gen))

        while len(new_pop) < len(init_pop):

            if elitism == True:
                if problem == 'max':
                    elite = max(fitness_gen)
                    elite_indv = act_pop[fitness_gen.index(max(fitness_gen))]
                if problem == 'min':
                    elite = min(fitness_gen)
                    elite_indv = act_pop[fitness_gen.index(min(fitness_gen))]

            # Select two parents
            parent1, parent2 = select_function(act_pop, 3, data, problem, fitness_constraint, w_penalty), select_function(act_pop, 3, data, problem, fitness_constraint, w_penalty)
            if random.uniform(0,1) < repro_prob:
                offspring1, offspring2 = crossover_function(parent1, parent2, data, nutrients, cross_constraint)
            else:
                offspring1, offspring2 = parent1, parent2

            if random.uniform(0,1) < mut_prob:
                offspring1 = mutate_function(offspring1)
            if random.uniform(0,1) < mut_prob:
                offspring2 = mutate_function(offspring2)

            new_pop.append(offspring1)
            # In case the size of the population is impar
            if len(new_pop) < len(init_pop):
                new_pop.append(offspring2)

        fitness_gen = []
        for individual in new_pop:
            fitness_gen.append(fitness_function(individual, new_pop, data, fitness_constraint, w_penalty))
        med_fitness_gen.append(statistics.median(fitness_gen))

        if elitism:
            if problem == 'max':
                worst = min(fitness_gen)
                if elite > worst:
                    new_pop.pop(fitness_gen.index(worst))
                    fitness_gen.pop(fitness_gen.index(worst))
                    new_pop.append(elite_indv)
                    fitness_gen.append(fitness_function(elite_indv, act_pop, data, fitness_constraint, w_penalty))
            if problem == 'min':
                worst = max(fitness_gen)
                if elite < worst:
                    new_pop.pop(fitness_gen.index(worst))
                    fitness_gen.pop(fitness_gen.index(worst))
                    new_pop.append(elite_indv)
                    fitness_gen.append(fitness_function(elite_indv, act_pop, data, fitness_constraint, w_penalty))

        act_pop = new_pop

    return med_fitness_gen, new_pop[fitness_gen.index(min(fitness_gen))]


combinations = [[tournament_selection, arithmetic_Crossover, swap_mutation], [tournament_selection, shuffle_Crossover, swap_mutation],
                [tournament_selection, onePoint_Crossover, swap_mutation], [tournament_selection, arithmetic_Crossover, scramble_mutation],
                [tournament_selection, shuffle_Crossover, scramble_mutation], [tournament_selection, onePoint_Crossover, scramble_mutation],
                [tournament_selection, arithmetic_Crossover, inversion_mutation],[tournament_selection, shuffle_Crossover, inversion_mutation],
                [tournament_selection, onePoint_Crossover, inversion_mutation],
                [ranking_selection, arithmetic_Crossover, swap_mutation],[ranking_selection, shuffle_Crossover, swap_mutation],
                [ranking_selection, onePoint_Crossover, swap_mutation],[ranking_selection, arithmetic_Crossover, scramble_mutation],
                [ranking_selection, shuffle_Crossover, scramble_mutation],[ranking_selection, onePoint_Crossover, scramble_mutation],
                [ranking_selection, arithmetic_Crossover, inversion_mutation],[ranking_selection, shuffle_Crossover, inversion_mutation],
                [ranking_selection, onePoint_Crossover, inversion_mutation],
                [roulette_selection, arithmetic_Crossover, swap_mutation],[roulette_selection, shuffle_Crossover, swap_mutation],
                [roulette_selection, onePoint_Crossover, swap_mutation],[roulette_selection, arithmetic_Crossover, scramble_mutation],
                [roulette_selection, shuffle_Crossover, scramble_mutation],[roulette_selection, onePoint_Crossover, scramble_mutation],
                [roulette_selection, arithmetic_Crossover, inversion_mutation],[roulette_selection, shuffle_Crossover, inversion_mutation],
                [roulette_selection, onePoint_Crossover, inversion_mutation]]

mutations = [0.05, 0.1, 0.2]

for mutation in mutations:
    # Execute one combination 30 times
    for i, combination in enumerate(combinations):
        for trial in range(15):
            init_pop =  initial_pop(70, 5, data, nutrients, False)

            results = evolution(init_pop, 100, 0.95, mutation, combination[0], combination[1], combination[2], True, 'min', 5)
            med_fitness, best_individual = results

            # File to store the data for visualization purposes
            archive = f"output_{trial, i, mutation}.csv"

            rows = []

            # Add each value from med_fitness as a separate row
            for value in med_fitness:
                rows.append([value])

            # Add best_individual as the second column of the last row
            rows[-1].extend(best_individual)

            with open(archive, "w", newline="") as arquivo_csv:
                writer = csv.writer(arquivo_csv)

                writer.writerows(rows)