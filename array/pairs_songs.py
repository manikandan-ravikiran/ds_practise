class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count,times = 0,[0 for i in range(61)]
		# Build up array
        for i in time:
            times[i%60] += 1
		# Exception cases of 0 and 30 -- (n+(n-1)/2)
        count += times[0]*(times[0]-1)//2 + times[30]*(times[30]-1)//2
		# Sum up remaning combinations
        count += sum(times[i]*times[60-i] for i in range(1,30))
        return count