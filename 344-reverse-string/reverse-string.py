class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        temp1 = 0
        temp2 = 0
        while left <= right:
            temp1 = s[right]
            temp2 = s[left]
            s[left] = temp1
            s[right] = temp2
            left +=1
            right -= 1
        return s
        