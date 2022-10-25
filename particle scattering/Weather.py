import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

def check_weather():
    transition_matrix = [[0.8, 0.2], [0.5, 0.5]]
    average_sunniness = []
    weather_state = [0, 1]
    current_weather = np.random.choice(weather_state)
    #print(current_weather)
    daily_weather_log = []

    for _ in range(10000):
        current_weather = np.random.choice(weather_state, p=transition_matrix[current_weather])
        daily_weather_log.append(current_weather)
        average_sunniness.append(round(1.-np.mean(daily_weather_log), 3))

    plt.figure(dpi=100)
    plt.plot(range(len(average_sunniness)), average_sunniness)
    plt.xlabel('Number of iterations')
    plt.ylabel('Average Sunniness')
    plt.show()
    return round(1.-np.mean(daily_weather_log), 3)

if __name__ == '__main__':
    print(check_weather())



