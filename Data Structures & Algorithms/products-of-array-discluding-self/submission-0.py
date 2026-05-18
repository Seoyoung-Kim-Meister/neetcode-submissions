class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            ele = 1
            for j in range(len(nums)):
                if j != i:
                    ele = ele * nums[j]
            output.append(ele)
        return(output)            