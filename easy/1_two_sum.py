'''
    url: https://leetcode.com/problems/two-sum/
    difficulty: easy
    runtime of solution: O(n)
'''

def twoSum(nums, target):
    # construct such that
    # x + num_lookup[x] = target
    num_lookup = {}

    for i, num in enumerate(nums):
        if num in num_lookup:
            return [i, nums.index(num_lookup[num])]
        else:
            num_lookup[target - num] = num