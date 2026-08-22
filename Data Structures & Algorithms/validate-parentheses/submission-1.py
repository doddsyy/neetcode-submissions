class Solution:
    def isValid(self, s: str) -> bool:
        corr = {'{' : '}', '[': ']', '(':')'}
        stack = []
        for letter in s:
            if letter in '({[':
                stack.append(letter)
            elif not stack:
                return False
            elif letter != corr[stack.pop()]:
                return False
        return not stack
            



        