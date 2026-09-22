class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        arr = []
        for char in s:
            char = char[::-1]
            arr.append(char)
        arr = " ".join(arr)
        return arr
