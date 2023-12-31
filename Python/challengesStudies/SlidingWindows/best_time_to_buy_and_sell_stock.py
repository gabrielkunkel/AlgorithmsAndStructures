from typing import List


class BestTimeToBuyAndSellStock:
    @staticmethod
    def my_attempt(prices: List[int]) -> int:
        minimum_price, total = prices[0], 0
        i = 1
        while i < len(prices):
            if prices[i] < minimum_price:
                minimum_price = prices[i]
            elif (prices[i] - minimum_price) > total:
                total = prices[i] - minimum_price
            i += 1

        return total

    @staticmethod
    def faster_maybe_interesting(prices: List[int]) -> int:
        buy = sell = prices[0]
        profit = 0
        for x in prices:
            if x < buy:
                buy = sell = x
            elif x > sell:
                sell = x
                profit = max(profit, x - buy)
        return profit


