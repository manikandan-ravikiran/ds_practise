class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumval=0
        res=[]
        for value in nums:
            res.append(sumval+value)
            sumval+=value
        return res
