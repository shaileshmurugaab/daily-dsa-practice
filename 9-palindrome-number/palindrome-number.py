class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        y = len(x)
        if x[0:y] == x[::-1]:
            return True
        else:
            return False