"""
     If I know that 50% of the time I eat chicken after I eat beef,
    what percentage of my overall meals are chicken?

    This program is Monte Carlo Simulation which estimates the probability of eating
    a particular meal tomorrow given the meal eaten today
"""

import numpy as np
import matplotlib.pyplot as plt


def Meal_stats():
    """
        This is a matrix that holds the probabilities of meal being eaten tomorrow
        given the meal eaten today
        The rows are "today's meal" and columns are "chances of this meal tomorrow,
        given today's meal"

                Beef Chkn Vege
        Beef	25%	 50%  25%
        Chkn	75%	 20%  5%
        Vege	50%	 50%  0%
    """
    dinner_matrix= [[.25, .5, .25],
                    [.75, .2, .05],
                    [.50, .5, 0.0]]

    """
        The first meal is picked randomly with each meal having an equal chance
        0= beef; 1= chicken; 2= vegetarian
    """
    possible_options= [0, 1, 2]

    starting_meal = np.random.choice(possible_options)
    # print(starting_meal)

    number_of_meals_to_simulate= 1000000
    meal_counter = {0:0, 1:0, 2:0}
    chicken_percentage_over_time =[]

    meal = starting_meal
    meal_counter[meal] +=1

    """ 
       The probabilities in the dinner matrix are used to sample future meal choices, given the current meal.
       
       For example, if beef was eaten today the top array in the dinner matrix 
       is selected and the probabilities in that array are use by np.random.choice
       to select the next meal.
       
       The meal_counter dictionary is used to keep track of which meal has been consumed.
    """

    for sim_num in range(number_of_meals_to_simulate):
        meal = np.random.choice(possible_options, p=dinner_matrix[meal])
        meal_counter[meal] += 1
        chicken_percentage_over_time.append(meal_counter[1]/(sim_num+1))
    #print(meal_counter)

    meal_names = ['beef', 'chicken', 'vegetarian']
    for key, value in meal_counter.items():
        print(meal_names[key], ":", "%.3f" % (value/number_of_meals_to_simulate*100.),'%')

    """"
        Plotting the percentage of beef meals eaten across a million meals (simulations)
        in total.
    """

    fig, ax = plt.subplots(3, 1)
    ax[0].plot(range(number_of_meals_to_simulate)[:100], chicken_percentage_over_time[:100], label='% of First 100 Meals that are Chicken')
    ax[1].plot(range(number_of_meals_to_simulate)[:1000], chicken_percentage_over_time[:1000], c='r', label='% of First 1000 Meals that are Chicken')
    ax[2].plot(range(number_of_meals_to_simulate), chicken_percentage_over_time, c='g', label='% of All Meals that are Chicken')
    ax[2].set_xlabel("Number of Meals Simulated", fontsize=15)
    ax[1].set_ylabel("Chicken Meal Percentage", fontsize=15)
    ax[0].legend(loc="upper right")
    ax[1].legend(loc="upper right")
    ax[2].legend(loc="upper right")
    plt.style.use('seaborn')
    plt.show()


if __name__ == '__main__':
    Meal_stats()