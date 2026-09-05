class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0
        n =len(nums)
        actualsum=(n*(n+1))/2
        for i in nums:
            sum+=i
        missing = actualsum-sum
        return int(missing)
        
        


        