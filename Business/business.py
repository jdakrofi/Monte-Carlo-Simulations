"""
  Can a firm get users to purchase more item from its website
  by optimizing its retention rate?

  This application of the Monte Carlo Simulation attempts to answer that question.
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

'''
    Each row lists the connection probability between pages.
    That is, the probability that a user will leave the page in the right hand column
    and end up on one the pages listed in the top row
    For example. There is is 15% chance that a user leave the home and land on the
    FAQ page (column 2 of row 1)
        Internet	Home	FAQ	    Products	Item 1	Item 2	Purchase 1	Purchase 2
Internet	0.0	    0.40	0.20	0.10	    0.15	0.15	0.00	    0.00
Home	    0.4	    0.00	0.15	0.15	    0.15	0.15	0.00	    0.00
FAQ	        0.6 	0.15	0.00	0.25	    0.00	0.00	0.00	    0.00
Products	0.4	    0.10	0.05	0.00	    0.25	0.20	0.00	    0.00
Item 1	    0.4	    0.10	0.05	0.10	    0.00	0.20	0.15	    0.00
Item 2	    0.4	    0.10	0.05	0.10	    0.20	0.00	0.00	    0.15
Purchase 1	0.0	    0.00	0.00	0.00	    0.00	0.00	0.00	    0.00
Purchase 2  0.0	    0.00	0.00	0.00	    0.00	0.00	0.00	    0.00    
'''


def CTR(flag):
    landing_dist = [[0., 0.4, 0.2, 0.1, 0.15, 0.15, 0.0, 0.0],  # Not our page
                    [0.4, 0., 0.15, 0.15, 0.15, 0.15, 0.0, 0.0],  # home page
                    [0.6, 0.15, 0., 0.25, 0.0, 0.0, 0.0, 0.0],  # FAQ
                    [0.4, 0.1, 0.05, 0., 0.25, 0.2, 0.0, 0.0],  # product page
                    [0.4, 0.1, 0.05, 0.1, 0., 0.2, 0.15, 0.],  # item 1 page
                    [0.4, 0.1, 0.05, 0.1, 0.2, 0., 0., 0.15],  # item 2 page
                    [0., 0., 0., 0., 0., 0., 0., 0.],  # purchase item 1
                    [0., 0., 0., 0., 0., 0., 0., 0.]]  # purchase item 2

    # Bounce rate from FAQ page is reduced by 10%. It is redistributed between the home page (8%)
    # And the product page (2%)
    new_landing_dist = [[0., 0.4, 0.2, 0.1, 0.15, 0.15, 0.0, 0.0],  # Not our page
                        [0.4, 0., 0.15, 0.15, 0.15, 0.15, 0.0, 0.0],  # home page
                        [0.5, 0.23, 0., 0.27, 0.0, 0.0, 0.0, 0.0],  # FAQ
                        [0.4, 0.1, 0.05, 0., 0.25, 0.2, 0.0, 0.0],  # product page
                        [0.4, 0.1, 0.05, 0.1, 0., 0.2, 0.15, 0.],  # item 1 page
                        [0.4, 0.1, 0.05, 0.1, 0.2, 0., 0., 0.15],  # item 2 page
                        [0., 0., 0., 0., 0., 0., 0., 0.],  # purchase item 1
                        [0., 0., 0., 0., 0., 0., 0., 0.]]  # purchase item 2

    if flag == 1:
        return landing_dist
    elif flag == 2:
        return new_landing_dist
    else:
        return None


# cols = ["Internet", "Home", "FAQ", "Products", "Item 1", "Item 2", "Purchase 1", "Purchase 2"]


def simulate_user(flag, debug=False):
    """
        This function simulates a user's movement around the website
        The user starts off in the internet at large.
        np.random is used to decide what page the go to next based on the probabilities stored in
        landing_dist and new_landing_dist arrays.
        If the user lands on a purchase item page, the loop is broken and the cost of the item
        bought is returned.
    """
    cost_of_item_1 = 100
    cost_of_item_2 = 75
    possible_clicks = np.arange(8)  # an array of evenly spaced elements
    user_page = 0  # start in the internet at large
    dist = CTR(flag)
    while True:  # stop if the user is purchasing or leaving
        user_page = np.random.choice(possible_clicks, p=dist[user_page])
        if debug:
            print(user_page)
        if user_page in [0, 6, 7]:
            break

    if user_page == 6:
        return cost_of_item_1
    if user_page == 7:
        return cost_of_item_2
    else:
        return 0


# print(simulate_user(CTR, debug=True))
def measure_revenue(flag, number_of_users=10000):
    """
        This function is used to track the number of purchases of each item made and the revenue generated.
        It also tracks the number of users who did not buy anything (bounces)
    """
    cost_of_item_1 = 100
    cost_of_item_2 = 75
    money = 0.
    bounces = 0.
    item1_purchases = 0.
    item2_purchases = 0.

    for _ in range(number_of_users):
        user_result = simulate_user(flag)
        money += float(user_result)
        if user_result == cost_of_item_1:
            item1_purchases += 1.
        elif user_result == cost_of_item_2:
            item2_purchases += 1.
        else:
            bounces += 1.
    return money, bounces, item1_purchases, item2_purchases


def stats():
    """
        In this function the following histogram are plotted:
        The revenue generated per user given  the landing_dist Matrix was used
        The revenue generated per user given  the new_landing_dist Matrix was used
        A comparison of the 2 histograms on the same plot to ascertain if to the website optimise
        Click-Through rated improve the firm's retention rate. That is, did users buy more products

    """
    track_revenue = []
    track_item1 = []
    track_item2 = []
    track_bounces = []

    number_of_user_groups = 1000
    number_of_users = 1000

    for _ in range(number_of_user_groups):
        money, bounces, item1_purchases, item2_purchases = measure_revenue(flag=1, number_of_users=number_of_users)
        track_revenue.append(money)
        track_bounces.append(bounces)
        track_item1.append(item1_purchases)
        track_item2.append(item2_purchases)

    print("Average Revenue/user: ", np.mean(track_revenue) / number_of_users)
    print("Average Bounce Rate: ", np.mean(bounces) / number_of_users)
    print("Average Item 1 Purchase Rate: ", np.mean(item1_purchases) / number_of_users)
    print("Average Item 2 Purchase Rate: ", np.mean(item2_purchases) / number_of_users)

    # print(np.array(track_revenue)/number_of_users)
    plt.figure(dpi=100)
    plt.hist(np.array(track_revenue) / number_of_users, bins=15)
    plt.xlabel("Average Revenue Per User")
    plt.ylabel("Counts")
    plt.title("Measuring Revenue Per User Given landing_dist Matrix")
    plt.show()

    track_revenue_2 = []
    track_item1_2 = []
    track_item2_2 = []
    track_bounces_2 = []

    for _ in range(number_of_user_groups):
        money, bounces, item1_purchases, item2_purchases = measure_revenue(flag=2, number_of_users=number_of_users)
        track_revenue_2.append(money)
        track_bounces_2.append(bounces)
        track_item1_2.append(item1_purchases)
        track_item2_2.append(item2_purchases)

    print("Average Revenue/user: ", np.mean(track_revenue_2) / number_of_users)
    print("Average Bounce Rate: ", np.mean(track_bounces_2) / number_of_users)
    print("Average Item 1 Purchases: ", np.mean(track_item1_2) / number_of_users)
    print("Average Item 2 Purchases: ", np.mean(track_item2_2) / number_of_users)

    plt.figure(dpi=100)
    plt.hist(np.array(track_revenue_2) / number_of_users, bins=15)
    plt.xlabel("Average Revenue Per User")
    plt.ylabel("Counts")
    plt.title("Measuring Revenue Per User Given new_landing_dist Matrix")
    plt.show()

    plt.figure(dpi=250)
    plt.hist(np.array(track_revenue) / number_of_users, bins=15, color='b', label="Original Site (landing_dist)")
    plt.hist(np.array(track_revenue_2) / number_of_users, bins=15, color='r', label="Optimized Site (new_landing_dist)")
    plt.xlabel("Average Revenue Per User")
    plt.ylabel("Counts")
    plt.legend(loc="upper right")
    plt.title("Measuring Revenue Per User Given Different landing distribution Matrices")
    plt.show()

    print("Percentage Improvement: ", (np.mean(track_revenue_2) - np.mean(track_revenue)) / np.mean(track_revenue))


if __name__ == "__main__":
    stats()
