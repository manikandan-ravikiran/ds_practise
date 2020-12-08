class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res, start, fmt = [], lower, lambda a, b: str(a) if a == b else str(a) + "->" + str(b)
        for n in nums:
            if start < n: res.append(fmt(start, n - 1))
            start = n + 1
        if start <= upper: res.append(fmt(start, upper))
        return res