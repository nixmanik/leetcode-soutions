# 0032. Longest Valid Parentheses

# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lvp = 0
        stack = [-1]    # this -1 is to avoid breaking the algo at index 0
        for i, c in enumerate(s):
            if c == '(': stack.append(i)
            else:
                stack.pop()
                # if the stack is empty, append this index
                if not stack: stack.append(i)
                # if something is there calculate lvp 
                else: lvp = max(lvp, i - stack[-1])
        return lvp

"""
Explaining this because it confused me a lot.

This finds the LVP in one iteration, doing the following at each character in the string:
1. IF this is an opening bracket, append it to stack to wait for a close.
2. ELSE it's a closing bracket (the strings are only '(' and ')') so:
    * pop the index of the last seen open (or the -1 if this is the start)
    * IF the stack is empty, then we had no matching open for this close so:
        - append this index to be the new -1 for the next possible substring
    * ELSE the stack is not empty and the substring from stack[-1] to this bracket could be the LVP

This solution is O(n) time and O(n) space because it runs through each character and the stack will grow to at most n elements where every element was an open bracket

EDIT: I forgot to explain the -1 stack: when i = 0, the lvp calcaulation would be wrong if that turned out to be lvp because 0 - 0 = 0. Setting -1 makes the result 1 at the start index (0 - -1) 
"""

# I read up on the O(1) space optimisation, using two-pass scan to remove the need for the stack so I made this:
def longestValidParentheses_alt(self, s:str) -> int:
        # Function will take the string and what bracket to use, this could be decoupled for other stuff outside the scope of the question I guess?
        def work(s:str, bracket:str) -> int:
            l = r = 0
            lvp = 0
            for ch in s:
                if ch == bracket:
                    l += 1
                else:
                    r += 1
                if l == r:
                    lvp = max(lvp, l+r)
                elif r > l:
                    l = r = 0
            return lvp

        return max(work(s,'('), work(reversed(s), ')'))
# This is still O(n) time technically even though it does two passes ( because O(2n) = O(n) )