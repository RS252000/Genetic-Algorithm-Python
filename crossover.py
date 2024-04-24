import random

def onePoint_Crossover(parent1, parent2, data, nutrients, constraints):

    """

        One Point Crossover: exchange of syntactic characteristics of two individuals - generating an offspring that
                             is the combination of the parents.

        Parameters:

            parent1: individual one for reproduction

            parent2: indivudal two for reproduction

            data: list with the information of the ingredients

            nutrients: constrains to the problem. Minimum intake necessary of nutrients.

            constraints: Boolean value. If restriction True when generating the initial population then True here.

        Output: Two individuals - Offspring

        """

    requirem_flag = 1

    # Repeat the cycle - depending on the activation of the constrains
    while requirem_flag != 0:

        # Choice of a random point for crossover
        # 1 and len(parent) -1 to ensure that some change is made
        cross_point = random.randint(1,len(parent1)-1)

        # Reproduction stage with two parents
        first_offspring = (parent1[:cross_point])
        first_offspring.extend(parent2[cross_point:])

        second_offspring = (parent2[:cross_point])
        second_offspring.extend(parent1[cross_point:])

        if constraints == False:

            requirem_flag = 0

        # Only accepting the offspring has valid if it respects the requirements
        elif constraints == True:

            requirem_flag = 0
            offsprings = []
            offsprings.append(first_offspring)
            offsprings.append(second_offspring)

            for count_constrain in range(len(nutrients)):
                ingest_value = 0
                min_value = nutrients[count_constrain][1]

                for offspring in offsprings:
                    for ingredient in offspring:
                        # Calculated the total intake of a certain nutrient per individual
                        ingest_value += data[ingredient][count_constrain + 2]
                if ingest_value < min_value:
                    requirem_flag += 1

    return first_offspring, second_offspring


def shuffle_Crossover(parent1, parent2, data, nutrients, constraints):

    """

        Shuffle Crossover: exchange of syntactic characteristics of two shuffled individuals - generating an offspring
                           that is the combination of the parents and unshuffle.

        Parameters:

            pop: population selected by population initial

            data: list with the information of the ingredients

            nutrients: constrains to the problem. Minimum intake necessary of nutrients.

            constraints: Boolean value. If restriction True when generating the initial population then True here.

        Output: Two individuals - Offspring

        """

    requirem_flag = 1

    # Repeat the cycle - depending on the activation of the constrains
    while requirem_flag != 0:

        # Generate a list of shuffled indexes
        shuffle_index = random.sample((range(0, len(parent1))), len(parent1))
        # Choice of the crosspoint
        cross_point = random.randint(1, len(parent1) - 1)
        # Shuffle the parents
        shuffle_parent1 = [parent1[i] for i in shuffle_index]
        shuffle_parent2 = [parent2[i] for i in shuffle_index]
        # Generate offspring
        s_first_offspring = shuffle_parent1[:cross_point] + shuffle_parent2[cross_point:]
        s_second_offspring = shuffle_parent2[:cross_point] + shuffle_parent1[cross_point:]
        # Unshuffle the offspring
        first_offspring = [order_element for order_element,index in sorted(sorted(zip(s_first_offspring, shuffle_index)), key=lambda t: t[1])]
        second_offspring = [order_element for order_element,index in sorted(sorted(zip(s_second_offspring, shuffle_index)), key=lambda t: t[1])]

        if constraints == False:

            requirem_flag = 0

        # Only accepting the offspring has valid if it respects the requirements
        elif constraints == True:

            requirem_flag = 0
            offsprings = []
            offsprings.append(first_offspring)
            offsprings.append(second_offspring)

            for count_constrain in range(len(nutrients)):
                ingest_value = 0
                min_value = nutrients[count_constrain][1]

                for offspring in offsprings:
                    for ingredient in offspring:
                        # Calculated the total intake of a certain nutrient per individual
                        ingest_value += data[ingredient][count_constrain + 2]
                if ingest_value < min_value:
                    requirem_flag += 1

    return first_offspring, second_offspring

def arithmetic_Crossover(parent1, parent2, data, nutrients, constraints):

    """

    Arithmetic: Generation of two offsprings based on the application of formula with a constant, alpha [0,1] to
                the two parents.

        Parameters:

            parent1: individual one for reproduction

            parent2: indivudal two for reproduction

            data: list with the information of the ingredients

            nutrients: constrains to the problem. Minimum intake necessary of nutrients.

            constraints: Boolean value. If restriction True when generating the initial population then True here.

        Output: Two individuals - Offspring

    """

    requirem_flag = 1

    # Repeat the cycle - depending on the activation of the constrains
    while requirem_flag != 0:

        # Generate random alpha
        alpha = random.uniform(0, 1)
        # Set the offsrping
        first_offspring = [None] * len(parent1)
        second_offspring = [None] * len(parent2)

        # Populate the offspring with genes
        for index in range(len(parent1)):

            first_offspring[index] = int(parent1[index] * alpha + (1-alpha) * parent2[index])
            second_offspring[index] = int(parent2[index] * alpha + (1-alpha) * parent1[index])
        if constraints == False:

            requirem_flag = 0

        # Only accepting the offspring has valid if it respects the requirements
        elif constraints == True:

            requirem_flag = 0
            offsprings = []
            offsprings.append(first_offspring)
            offsprings.append(second_offspring)

            for count_constrain in range(len(nutrients)):
                ingest_value = 0
                min_value = nutrients[count_constrain][1]

                for offspring in offsprings:
                    for ingredient in offspring:
                        # Calculated the total intake of a certain nutrient per individual
                        ingest_value += data[ingredient][count_constrain + 2]
                if ingest_value < min_value:
                    requirem_flag += 1

    return first_offspring, second_offspring


