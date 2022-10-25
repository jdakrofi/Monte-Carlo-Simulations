#from itertools import combinations
from CheckScore import jacks_or_better_scorer
from Deck import deck
import numpy as np

def combinations(lst, depth, start=0, prepend=[]):
    if depth <= 0:
        yield prepend
    else:
        for i in range(start, len(lst)):
            for combi in combinations(lst, depth-1, i+1, prepend+[lst[i]]):
                yield combi

        #print(prepend)

'''def diffcombo(lst):
    n = len(lst)
    res = [[]]

    def dfs(i, cur):
        if i == n:
            return
        res.append(cur + [lst[i]])
        dfs(i + 1, cur)
        dfs(i + 1, cur + [lst[i]])

    dfs(0, [])
    return res'''

'''cards = deck()
cards.shuffle()
cards.deal_five()
possible_hold_combos = [[]]
#diffcombo([0,1,2,3,4]) #[[]]#diffcombo(cards.hand) #[]


for i in range(1, 6):
    for c in combinations([0,1,2,3,4], i):
        possible_hold_combos.append(c)

#print(len(possible_hold_combos))

#for x in possible_hold_combos:
#    for c in x:
#        print(c)
#    print()

d = {}
for c in possible_hold_combos:
    d[str(c)]= []

#print(d)
cards.show_hand()
for combo in possible_hold_combos:
    for _ in range(5000):
        cards.draw_cards(ids_to_hold=combo, shuffle_remaining=True)
        jb = jacks_or_better_scorer(cards.final_hand)
        d[str(combo)].append(jb.score)

results= []
for key, value in d.items():
    results.append((key, np.mean(value)))

#ans = sorted(results, key=lambda x:x[1], reverse=True)
ans = eval(sorted(results, key=lambda x:x[1], reverse=True)[0][0])
print(ans)'''


