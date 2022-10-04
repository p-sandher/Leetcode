class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        l, r = 0, 1
        maxPrice = 0
        #l --> buy 
        #r--> sell
        # think of a graph
        
        while r < len(prices):
            if prices[l] < prices[r]: 
                #find the profit
                profit = prices[r] - prices[l]
                #compare the currentprice and the profit 
                maxPrice = max(maxPrice, profit)
            else: 
                l = r
            r+=1
        return maxPrice
