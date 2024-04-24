from data import nutrients

def fitness_function(individual, pop, data, constraints, w_penalty):
    counts = {}
    fitness = 0
    penalty = 0

    if constraints:
        subt_total_minimum = []
        price = 0
        total_calories = 0
        total_protein = 0
        total_calcium = 0
        total_iron = 0
        total_vitamin_a = 0
        total_vitamin_b1 = 0
        total_vitamin_b2 = 0
        total_niacin = 0
        total_vitamin_c = 0

        for dish in individual:
            price += data[dish][2]
            total_calories += data[dish][3]
            total_protein += data[dish][4]
            total_calcium += data[dish][5]
            total_iron += data[dish][6]
            total_vitamin_a += data[dish][7]
            total_vitamin_b1 += data[dish][8]
            total_vitamin_b2 += data[dish][9]
            total_niacin += data[dish][10]
            total_vitamin_c += data[dish][11]

        fitness = price

        diet_total_nut = [total_calories, total_protein, total_calcium, total_iron, total_vitamin_a,
                          total_vitamin_b1, total_vitamin_b2, total_niacin, total_vitamin_c]

        for nutrient, min_requirement in zip(diet_total_nut, nutrients):
            subt_total_minimum.append((nutrient - min_requirement[1]))
            if nutrient - min_requirement[1] < 0:
                fitness += 1

        for sublist in pop:
            for element in list(set(sublist)):
                if element in counts:
                    counts[element] += 1
                else:
                    counts[element] = 1

        for ingredient in individual:
            if counts[ingredient] != 1:
                penalty += counts[ingredient]

        if max(counts) != min(counts):
            penalty = ((penalty - min(counts)) / (max(counts) - min(counts)))*w_penalty
        else:
            penalty = 0.5

        fitness += penalty

    else:
        fitness = 0
        for ingredient in individual:
            fitness += data[ingredient][2]
            
        for sublist in pop:
            for element in list(set(sublist)):
                if element in counts:
                    counts[element] += 1
                else:
                    counts[element] = 1

        for ingredient in individual:
            if counts[ingredient] != 1:
                penalty += counts[ingredient]

        if max(counts) != min(counts):
            penalty = ((penalty - min(counts)) / (max(counts) - min(counts)))*w_penalty
        else:
            penalty = 0.5

        fitness += penalty

    return fitness
