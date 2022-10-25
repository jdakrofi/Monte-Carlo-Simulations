from VideoPoker import play_poker
from VideoPoker import play_poker_randomly
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import seaborn as sns


random_survive = []
for _ in range(100):
    random_survive.append(play_poker_randomly(20, max_count=100, return_count=True))

smart_survive = []
for _ in range(100):
    smart_survive.append(play_poker(20, max_count=100, sim_strength=100, return_count=True))

smart_survive_2 = []
for _ in range(100):
    smart_survive_2.append(play_poker(20, max_count=500, sim_strength=50, return_count=True))

smart_survive_3 = []
smart_tally_3 = []
for player_num in range(53):
    print("Player", player_num)
    i, j = play_poker(20, max_count=1000, sim_strength=200, return_both=True)
    smart_survive_3.append(i)
    smart_tally_3.append(j)

survivors = 0
profitors = 0
for x in smart_tally_3:
    if len(x) == 1001:
        survivors += 1
        if x[-1] > 20:
            profitors += 1
print("Percent lasting 1000 hands: ", str(round(survivors/len(smart_tally_3),3)))
print("Percent with profit after 1000 hands: ", str(round(profitors/len(smart_tally_3),3)))




'''money_tally = play_poker(20, sim_strength=100, verbose=True)
plt.figure(dpi=100)
max_len = len(money_tally)
plt.plot(range(max_len), money_tally)
plt.plot([0, max_len], [20,20], 'r--', lw=2, alpha=0.5)
plt.xlabel("Number of Hands")
plt.ylabel("Amount of Money")
plt.show();'''

plt.figure(dpi=100)
sns.displot(random_survive, label='Random Play')
sns.displot(smart_survive, color='r', label="Smartest Play")
plt.legend(loc='upper right')
plt.title("Number of Hands Survived with $20 (Max Count = 100)")
plt.show()

plt.figure(dpi=100)
sns.distplot(smart_survive_2, color='r', label="Smartest Play", kde=True, bins=20)
plt.legend(loc='upper right')
plt.title("Number of Hands Survived with 20 Credits (50 Sims per hold combo)")
plt.show()

plt.figure(dpi=100)
sns.distplot(smart_survive_3, color='r', label="Smartest Play", kde=True, bins=20)
plt.legend(loc='upper right')
plt.title("Number of Hands Survived with 20 Credits (200 Sims per hold combo)")
plt.show()

max_len = 0
plt.figure(dpi=200)
plt.xlabel("Number of Hands")
plt.ylabel("Amount of Money")
plt.title("Money vs Number of Hands (53 players - 200 Sims per hold combo)")
for money_tally in smart_tally_3:
    n = len(money_tally)
    if n > max_len:
        max_len = n
    plt.plot(range(n), money_tally, lw=1)
plt.plot([0, max_len], [20,20], 'k--', lw=2, alpha=0.5)
plt.show()


