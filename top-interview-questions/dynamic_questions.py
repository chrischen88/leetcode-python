from typing import List


def climbStairs(n: int) -> int:
    cache = {}
    cache[1] = 1
    cache[2] = 2
    idx = 3
    for idx in range(3,n+1):
        cache[idx] = cache[idx-1] + cache[idx-2]
    return cache[n]

def maxProfit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0
    
    min_prev_price = prices[0]
    max_profit = 0
    
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i]-min_prev_price)
        min_prev_price = min(min_prev_price, prices[i])
        
    return max_profit

def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    cur_sum = nums[0]
    for i in range(1, len(nums)):
        cur_sum = max(nums[i], cur_sum + nums[i])
        max_sum = max(cur_sum, max_sum)
        
    return max_sum

def rob(nums: List[int]) -> int:
    if len(nums) <= 2:
        return max(nums)
    dp = {}
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])
    return dp[len(nums)-1]