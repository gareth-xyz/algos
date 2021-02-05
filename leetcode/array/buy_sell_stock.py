# 122. Best Time to Buy and Sell Stock II

def max_profit(prices):
    # my poor answer

    # low = None
    # high = None
    # prof_a = 0
    # low = high = prices[0]
    # for i in prices:
    #     if i < low:
    #         low = i
    #     elif i > high:
    #         high = i
    # if prices.index(low) < prices.index(high):
    #     prof_a = high - low

    # # iterate through and just sell each time 
    # prof_b = 0
    # pos = 1
    # for i in prices:
    #     temp = prices[pos:]
    #     print(temp)
    #     if temp != []:
    #         if i < temp[0]:
    #             prof_b += (temp[0] - i)
    #             pos += 1
    #         else:
    #             pos += 1

    # return max([prof_a, prof_b])

    # neat python answer uses range to loop
    # also uses max to to either add the positive diff, or discard if no positive
    profit = 0
    for i in range(1, len(prices)):
        profit += max(prices[i]-prices[i-1], 0)
    return profit

if __name__ == '__main__':
    print(max_profit( [6,1,3,2,4,7] ))