class Solution:
    def singleNumber(self, nums: List[int]) -> int: #type: ignore

        # array = not empty
        # each element = appears twice
        # target = single element

        # linear time complexity O(n)
        # constant space complexity O(1)
        
        result = 0
        for n in nums:
            result ^= n
        return result
    