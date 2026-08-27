class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        for n in nums:
            l.append(n*n)
        l.sort()
        return l
        