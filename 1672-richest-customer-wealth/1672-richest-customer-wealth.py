class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total=[]
        for l in accounts:
           total.append(sum(l))
        return max(total)
        

        