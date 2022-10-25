"""
    If there was a drunk guy walking randomly around a bar,
    how often would he make it to the bathroom?

    This application of the Monte Carlo Simulation aims to
    answer that question.
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


def convert_to_rads(degrees):
    """
    Converting degrees to radians
    Input: degrees (0-360) int
    Output: float, angle in radians
    """

    return float((degrees * np.pi) / 180)
    # return float(((2*np.pi)/360)*degrees)


def take_step(position, step_size):
    """
    Takes a step for our walker
    Input:  Current (x,y) position
    Output: New (x,y) position
    """

    angle_degrees = np.random.randint(0, 360)
    angle_radians = convert_to_rads(angle_degrees)
    new_x = position[0] + step_size*np.cos(angle_radians)
    new_y = position[1] + step_size*np.sin(angle_radians)
    return [new_x, new_y]


def check_the_rules(position, x_range, y_range, goal_range):
    """
    This function to decide if our walker dies, lives or has succeeded

    Input: Walkers Current position = position (x,y) ;
           Dimensions of the room = x_range (low, high), y_range (low, high) ;
           Position of the toilet = goal_range (low_x, low_y, high_x, high_y)

    Output: Int(0- dead, 1-lives, 2-succeeded)
    """

    x = position[0]
    y = position[1]

    if x < x_range[0] or x > x_range[1]:
        return 0

    if y < y_range[0] or y > y_range[1]:
        return 0

    if goal_range[0] < x < goal_range[2] and goal_range[1] < y < goal_range[3]:
        return 2

    return 1


def walker_episode(position=None, x_range=(0, 10), y_range=(0, 10), number_of_steps=50, step_size=1, goal_range=(9, 9, 10, 10)):
    """
    This function sets the walker in motion and then checks the rules.
    The walker is placed into the room (with a starting position)
    then keeps walking till the upper limit of steps (number_of_steps) is exceeded.
    Before taking each step the "dice" is rolled to decide which direction the
    walker moves in.
    The path of the walker is tracked and visualized.
    """

    position_tracker = []

    if not position or len(position) != 2:
        position = [np.random.uniform(x_range[0], x_range[1]), np.random.uniform(y_range[0], y_range[1])]
        position_tracker = [position]

    position_tracker.append(position)

    for _ in range(number_of_steps):
        position = take_step(position, step_size)
        position_tracker.append(position)
        survives = check_the_rules(position, x_range, y_range, goal_range)
        if survives == 0 or survives == 2:
            break

    return position_tracker, survives


def draw_path():
    """
    This function runs ten thousand random simulations
    It also estimates the "percentage chance that he makes it to the bathroom"
    And plots the path of the ten thousandth (last) step
    """
    results = {0: 0, 1: 0, 2: 0}
    epochs = 10000
    for _ in range(epochs):
        walk_path, outcome = walker_episode(position=[5, 5], number_of_steps=100)
        results[outcome] += 1
    print("Goal Percentage:", results[2] / epochs * 100)
    print("Still Alive, but no goal: ", results[1] / epochs * 100)
    print("Crashed in to wall: ", results[0] / epochs * 100)

    x, y = zip(*walk_path)
    plt.figure(dpi=100)
    plt.plot(x,y)
    plt.scatter(x[-1], y[-1], marker='x', c='r', s=200);
    plt.plot([9, 10, 10, 9, 9], [9, 9, 10, 10, 9], 'k--')
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.show()


def draw_many_paths():
    """
    This function run as many simuations as it takes to get a success
    And plots each with a '.' identifying the start point
    and a 'x' demarcating where the path terminates
    """

    outcome = 0
    walk_paths = []
    while outcome !=2:
        walk_path, outcome = walker_episode(position=[4, 4], number_of_steps=20, step_size=2)
        walk_paths.append(walk_path)

    plt.figure(dpi=100)
    for walk_path in walk_paths:
        x, y = zip(*walk_path)
        plt.plot(x, y)
        plt.scatter(x[-1], y[-1], marker='x', c='r', s=200)
        plt.scatter([4], [4], marker='o', c='k', s=200, zorder=10)
    plt.plot([9, 10, 10, 9, 9], [9, 9, 10, 10, 9], 'k--')
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.show()


def get_Confidence():
    """
    This function runs 1-10000 simulations in increments of 10.
    It then charts how the rate of success varies as the number simulations increases
    """

    survival_estimations = []
    for epoch in range(1, 10000, 10):
        results = {0: 0, 1: 0, 2: 0}
        for _ in range(epoch):
            walk_path, outcome = walker_episode(position=[5, 5], number_of_steps=100)
            results[outcome] += 1
        survival_estimations.append(results[2]/epoch * 100)

    len(survival_estimations)
    plt.figure(dpi=100)
    plt.xlabel("Number of Epochs")
    plt.ylabel("Estimated 'Goal' Rate")
    # Takes a long time under for number of steps less than 100.
    plt.plot(range(1, 10000, 10), survival_estimations)
    plt.plot([0, 10000], [np.mean(survival_estimations), np.mean(survival_estimations)], 'r--')
    plt.title("Estimating the Goal Rate (Avg: %.3f)" %np.mean(survival_estimations))
    plt.show()


if __name__ == '__main__':

    # get_Confidence()
    # draw_path()
    draw_many_paths()


""" def get_results():
    results = {0: 0, 1: 0, 2: 0}
    epochs = 10000
    for _ in range(epochs):
        walk_path, outcome = walker_episode(position=[5, 5], number_of_steps=100)
        results[outcome] += 1
    print("Goal Percentage:", results[2] / epochs * 100)
    print("Still Alive, but no goal: ", results[1] / epochs * 100)
    print("Crashed in to wall: ", results[0] / epochs * 100)

   while result == 0:
        # modification
        walk_path, result = walker_episode(position= [4,4], number_of_steps=100)
        #print(result)

    #print(walk_path)
    draw_path(walk_path"""