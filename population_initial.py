import random
import matplotlib as plt
from data import data, nutrients
from itertools import chain
from collections import Counter


def initial_pop(pop_size, individual_size, data, nutrients, constraints):

    """

    Initial Population.

    Parameters:

        pop_size: Number of total individuals desired

        individual_size: Number of ingredients per individual

        data: data provided for the problem

        nutrients: constrains to the problem. Minimum intake necessary of nutrients.

        constraints: Boolean Value to apply or not the constraints on the initial population

    Output: List of n (pop_size) individuals, each a list of m (individual_size) ingredients

    """


    pop = []
    # Ensure that every ingredient is present at least once -> Attempt to ensure variety
    while len(Counter(chain.from_iterable(pop)).keys()) != len(data):
        pop = []
        # Populate
        while len(pop) != pop_size:

            # Generate individuals
            individual = []
            for _ in range(individual_size):
                # Randomly generate the individuals - list of ingredients of a size individual_size
                individual.append(random.randint(0, len(data)-1))

            # Application of the constraints -> Two trial will be make with the constraints
            if constraints == True:
                requirem_flag = 0

                for count_constrain in range(len(nutrients)):
                    ingest_value = 0
                    min_value = nutrients[count_constrain][1]

                    for ingredient in individual:
                        # Calculated the total intake of a certain nutrient per individual
                        ingest_value += data[ingredient][count_constrain + 2]

                    if ingest_value < min_value:
                        requirem_flag += 1

                if requirem_flag == 0:
                    pop.append(individual)
            else:
                pop.append(individual)

    return pop


def hist_top_10_ingredients(init_pop):
    counts = {}
    #this for loop created a dictionary of each ingredient and the amount of times it was selected
    for sublist in init_pop:
        for element in sublist:
            if element in counts:
                counts[element] += 1
            else:
                counts[element] = 1

    #new_dic is the sorted dictionary
    new_dic = sorted(counts.items(), key=lambda x:x[1], reverse=True)


    #extract the first 10 elements from new_dic (the ones more repeated)
    top_10 = new_dic[:10]

    #separate the values and counts into separate lists
    values, counts = zip(*top_10)

    plt.bar(range(len(values)), counts)

    # Set x-axis tick labels
    plt.xticks(range(len(values)), values)

    # Set labels and title
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.title('Histogram of 10 most selected ingredients')

    # Display the histogram
    plt.show()