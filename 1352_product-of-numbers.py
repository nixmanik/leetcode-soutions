"""
1352. Product of the Last K Numbers

Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:
    ProductOfNumbers() Initializes the object with an empty stream.
    void add(int num) Appends the integer num to the stream.
    int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.

The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

"""
import math

class ProductOfNumbers:

    def __init__(self):
        self.stream : list[int] = []

    def add(self, num: int) -> None:
        self.stream.append(num)

    def getProduct(self, k: int) -> int:
        return math.prod(self.stream[-k:])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

"""
This was straightforward but the leetcode charts showed this solution was less efficient in time and space than it could be. Instead of storing the num coming it, these solutions stored the running cumulative product:

    -- First initialise with 1 to cover first mult --
    def __init__(self):
        self.stream = [1]

    -- Add will keep the cumulative product in the list, if it's 0 everything before it would be zero product so zero it out and start again
    def add(self, num: int) -> None:
        if num == 0:
            self.stream = [1]
            return
        self.stream.append(self.stream[-1] * num)
    
    -- Return the last number divided by the cumulative product of the value in n-1-k where n is the length of the list
    def getProduct(self, k: int) -> int:
        last = len(self.stream) - 1 - k
        if last < 0:
            return 0
        return self.stream[-1] // self.stream[last]

My problem with this is that the problem specifies the integer be put into the stream, and not the cumulative product. But in this scope I guess it doesn't matter, it's still more efficient as long as the values entered don't need to be remembered themselves.

"""
