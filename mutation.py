from population_initial import initial_pop
import random

def scramble_mutation(offspring):

    """

        Scramble Mutation: For a random individual select two random positions and shuffle the gene between them.

        Parameters:

            pop: population selected by population initial

        Output: Mutaded individual

    """
    # Choice of the crosspoints
    cross_point = random.sample((range(0, len(offspring))), 2)
    cross_point.sort()

    # There is no mutation if the random points are consecutive
    while cross_point[1]-cross_point[0] == 1:
        # Choice of the crosspoints
        cross_point = random.sample((range(0, len(offspring))), 2)
        cross_point.sort()

    # Generate a list of shuffled indexes
    shuffle_sublist = offspring[cross_point[0]:cross_point[1]]
    random.shuffle(shuffle_sublist)
    # Shuffle the individual - Mutation]
    offspring[cross_point[0]:cross_point[1]] = shuffle_sublist

    return offspring


def swap_mutation(offspring):

    """

        Swap Mutation: For a random individual select two random positions and switch those genes.

        Parameters:

            pop: population selected

        Output: Mutaded individual

    """

    # Select a random individual by index
    # indiv = random.randint(0, len(pop)-1)
    # indiv_orig = pop[indiv].copy() - to test purposes
    # Choice of the crosspoints
    cross_point = random.sample((range(0, len(offspring))), 2)
    cross_point.sort()

    # Generate the mutation
    offspring[cross_point[0]], offspring[cross_point[1]] = offspring[cross_point[1]], offspring[cross_point[0]]

    return offspring

def inversion_mutation(offspring):

    """

        Inversion Mutation: For a random individual select two random positions and inverse the gene order between them.

        Parameters:

            pop: population selected

        Output: Mutaded individual

    """

    # Select a random individual index
    # Choice of the crosspoints
    cross_point = random.sample((range(0, len(offspring))), 2)
    cross_point.sort()

    # There is no mutation if the random points are consecutive
    while cross_point[1]-cross_point[0] == 1:
        # Choice of the crosspoints
        cross_point = random.sample((range(0, len(offspring))), 2)
        cross_point.sort()

    # Generate a list of the inverted indexes - Mutation
    offspring[cross_point[0]:cross_point[1]] = offspring[cross_point[0]:cross_point[1]][::-1]

    return offspring
