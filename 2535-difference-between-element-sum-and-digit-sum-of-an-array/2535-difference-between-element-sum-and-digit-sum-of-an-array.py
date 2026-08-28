class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elemsum=0
        digitsum=0
        for num in nums:
            elemsum+=num
            while num!=0:
                dig=num%10
                digitsum+=dig
                num=num//10
        return elemsum-digitsum



        