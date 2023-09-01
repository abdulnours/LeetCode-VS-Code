class Solution:
    def majorityElement(self, nums: List[int]) -> int: #type: ignore
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        
        return candidate #type: ignore


                
'''
    My brute force way: T(n^2), S(1)

    for num1 in nums:
        count = 0
        for num2 in nums:
            if num1 == num2:
                count += 1
            if count > (len(nums)/2):
                return num1
'''

'''
    Dictionary way: T(n), S(n)

    from collections import defaultdict

    class Solution:
        def majorityElement(self, nums: List[int]) -> int:
            counts = defaultdict(int)
            majority_count = len(nums) // 2

            for num in nums:
                counts[num] += 1

                if counts[num] > majority_count:
                    return num

'''

'''
    Easy way: T(n log n), S(1)

    nums.sort()
    return nums[len(nums)//2]
'''

