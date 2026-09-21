class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res = []
        temp = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                res.append(temp)
                temp = 0
        res.append(temp)
        return max(res)

        