#YouTube Video : https://www.youtube.com/watch?v=5WZl3MMT0Eg

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)
        
        return maxSum
