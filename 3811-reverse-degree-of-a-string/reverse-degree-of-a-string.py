class Solution:
    def reverseDegree(self, s: str) -> int:
        arr = []
        t = 1
        s = [123- ord(char) for char in s]
        for i in range(0,len(s)):
            s[i] *= t
            t += 1
            arr.append(s[i])
        return sum(arr)
        