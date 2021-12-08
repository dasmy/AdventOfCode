import numpy as np


def simulate_lanternfish(days, initial_population):
    population = np.asarray(initial_population)

    print(f'Initial state: {population}')

    for day in range(1, days + 1):
        population -= 1

        ready = population < 0
        num_new = np.count_nonzero(ready)
        population[ready] = 6
        population = np.concatenate((population, 8*np.ones((num_new, ))))

        print(f'After {day:5d} days [{len(population):5d} fish]: {population}')




simulate_lanternfish(18, [3, 4, 3, 1, 2])
simulate_lanternfish(80, [4,1,3,2,4,3,1,4,4,1,1,1,5,2,4,4,2,1,2,3,4,1,2,4,3,4,5,1,1,3,1,2,1,4,1,1,3,4,1,2,5,1,4,2,2,1,1,1,3,1,5,3,1,2,1,1,1,1,4,1,1,1,2,2,1,3,1,3,1,3,4,5,1,2,2,1,1,1,4,1,5,1,3,1,3,4,1,3,2,3,4,4,4,3,4,5,1,3,1,3,5,1,1,1,1,1,2,4,1,2,1,1,1,5,1,1,2,1,3,1,4,2,3,4,4,3,1,1,3,5,3,1,1,5,2,4,1,1,3,5,1,4,3,1,1,4,2,1,1,1,1,1,1,3,1,1,1,1,1,4,5,1,2,5,3,1,1,3,1,1,1,1,5,1,2,5,1,1,1,1,1,1,3,5,1,3,2,1,1,1,1,1,1,1,4,5,1,1,3,1,5,1,1,1,1,3,3,1,1,1,4,4,1,1,4,1,2,1,4,4,1,1,3,4,3,5,4,1,1,4,1,3,1,1,5,5,1,2,1,2,1,2,3,1,1,3,1,1,2,1,1,3,4,3,1,1,3,3,5,1,2,1,4,1,1,2,1,3,1,1,1,1,1,1,1,4,5,5,1,1,1,4,1,1,1,2,1,2,1,3,1,3,1,1,1,1,1,1,1,5])
