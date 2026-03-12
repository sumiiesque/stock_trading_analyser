import random

def profit(prices, buy, sell):
    if sell <= buy:
        return -999
    return prices[sell] - prices[buy]


def climb(prices, start):

    n = len(prices)
    buy = start
    sell = start + 1

    best_profit = profit(prices, buy, sell)

    while True:

        improved = False

        for i in range(n):
            for j in range(i+1, n):

                p = profit(prices, i, j)

                if p > best_profit:
                    buy = i
                    sell = j
                    best_profit = p
                    improved = True

        if not improved:
            break

    return buy, sell, best_profit


def hillclimbing(prices, restarts=10):

    n = len(prices)

    best_buy = 0
    best_sell = 1
    best_profit = profit(prices, 0, 1)

    for _ in range(restarts):

        start = random.randint(0, n-2)

        buy, sell, p = climb(prices, start)

        if p > best_profit:
            best_profit = p
            best_buy = buy
            best_sell = sell

    return best_buy, best_sell, best_profit
