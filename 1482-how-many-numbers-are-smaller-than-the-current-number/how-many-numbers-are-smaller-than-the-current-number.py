class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0,len(nums)):
            sumi = 0
            for j in range(0,len(nums)):
                if i == j:
                    continue
                else:
                    if nums[j] < nums[i] and i != j:
                        sumi += 1
            arr.append(sumi)
        return arr
        