"""

3789. Minimum Cost to Acquire Required Items

You are given five integers cost1, cost2, costBoth, need1, and need2.

There are three types of items available:

An item of type 1 costs cost1 and contributes 1 unit to the type 1 requirement only.
An item of type 2 costs cost2 and contributes 1 unit to the type 2 requirement only.
An item of type 3 costs costBoth and contributes 1 unit to both type 1 and type 2 requirements.
You must collect enough items so that the total contribution toward type 1 is at least need1 and the total contribution toward type 2 is at least need2.

Return an integer representing the minimum possible total cost to achieve these requirements.

Constraints:
1 <= cost1, cost2, costBoth <= 106
0 <= need1, need2 <= 109

"""
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1 == need2 == 0: return 0
        total = 0
        total += min((cost1 + cost2), costBoth) * min(need1, need2)
        remainder = abs(need1 - need2)
        total += min(costBoth, cost1) * remainder if need1 > need2 else min(costBoth, cost2) * remainder
        return total

"""
This had a runtime of 0ms on LC and 19.06mb space, putting it in 100% time and 97.89% space. I wonder if this could be more elegant though. Maybe I'll research a nicer way to write it in the future.
"""