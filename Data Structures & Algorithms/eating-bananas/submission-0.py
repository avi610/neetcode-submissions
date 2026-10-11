from functools import reduce

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # smallest number than can eat all n in h
        # n > h -- cant be done because you can only eat a full pile max in 1 h
        # n == h -- require k to be the max pile size
        # n < h -- There is some number that is the min number that allows us to eat all piles but how to find this
        # Does it have to be a pile size? [2, 2, 2, 2], h = 10 -- k = 1 is 8
        # potential answer for min is between 1 and max(piles) -- we can binary search potential solutions of 1000000000 which is the max
        
        maxPile = reduce(lambda x,y: max(x,y), piles, -1)
        lo, hi = 1, maxPile
        ans = hi

        while lo <= hi:
            k = (lo + hi) // 2

            spentTime = 0
            for p in piles:
                spentTime += math.ceil(float(p) / k)
            if spentTime <= h:
                ans = k
                hi = k - 1
            else:
                lo = k + 1
        return ans