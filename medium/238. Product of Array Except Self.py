class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_with_dummy = [1] + nums + [1]
        i = 1
        output = []
        while i < len(nums)+1:
            n = 1
            for j in range(0, i):
                n = n * nums_with_dummy[j]
            for k in range(i + 1, len(nums_with_dummy)):
                n = n * nums_with_dummy[k]
            i += 1
            output.append(n)
        return output
