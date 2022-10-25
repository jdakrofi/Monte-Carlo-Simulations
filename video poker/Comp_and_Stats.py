"""
  Can one beat the casino in video poker?

  Using combinations of cards, multiple randomized simulations and expected returns,
  this application of the Monte Carlo Simulation attempts to answer that question

  Unfortunately the answer is no, but along the way is observed that by playing poker with the
  aid of a Monte Carlo Simulation is infinitely better than playing randomly.
"""
from VideoPoker import play_poker, play_poker_randomly
import matplotlib.pyplot as plt


def graph_play_poker_1():
    """
        This function plots the winning of one player over the course of the
        number of hands they play.
    """
    money_tally = play_poker(20, sim_strength=100, verbose=True)
    plt.figure(dpi=100)
    max_len = len(money_tally)
    plt.plot(range(max_len), money_tally)
    plt.plot([0, max_len], [20,20], 'r--', lw=2, alpha=0.5)
    plt.xlabel("Number of Hands")
    plt.ylabel("Amount of Money")
    plt.show()


def hist_bi_modalComp():
    """
        This function produces a graph comparing the outcomes of play video poker randomly
        verse computing the best hand (statistically) to play with  by using a monte carlo
        simulation
    """
    random_survive = []
    for _ in range(100):
        random_survive.append(play_poker_randomly(20, max_count=100, return_count=True))

    smart_survive = []
    for _ in range(100):
        smart_survive.append(play_poker(20, max_count=100, sim_strength=10, return_count=True))

    plt.figure(dpi=100)
    plt.hist(random_survive, label="Random Play")
    plt.hist(smart_survive, label="Smartest Play")
    plt.legend(loc='upper right')
    plt.title("Number of Hands Survived with 20 Credits (Max 100 Hands)")
    plt.show()


def graph_play_poker_200():
    """
        This function simulates the games of 53 players.
        Just want to gauge how many players can last beyond a thousand games
        And how many of them finish with a profit.
    """
    count = []
    money_tally = []
    for player_num in range(53):
        print("Player ", player_num)
        j = play_poker(20, max_count=1000, sim_strength=100)
        money_tally.append(j)

    total_survivors = 0
    total_profiters = 0
    for x in money_tally:
        if len(x) == 1001:
            total_survivors += 1
            if x[-1] > 20:
                total_profiters += 1
    print("% of players lasting a 1000 hands: ", str(round(total_survivors/len(money_tally),3)))
    print("% of players with profit after a 1000 hands: ", str(round(total_profiters / len(money_tally), 3)))

    max_max_len = 0
    plt.figure(dpi=100)
    plt.xlabel("Number of Hands")
    plt.ylabel("Amount of Money")
    plt.title("Money vs Number of Hands (53 players - 100 sims per combo)")
    for tally in money_tally:
        max_len = len(tally)
        if max_len > max_max_len:
            max_max_len = max_len
        plt.plot(range(max_len), tally, lw=1)
    plt.plot([0, max_max_len], [20, 20], 'k--', lw=2, alpha=0.5)
    plt.show()


if __name__ == '__main__':
    graph_play_poker_1()
    hist_bi_modalComp()
    graph_play_poker_200()
