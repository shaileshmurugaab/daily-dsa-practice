class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        arr= [""] * n
        for i in range(0,n):
            arr[indices[i]] = s[i]
        arr = "".join(arr)
        return arr


        