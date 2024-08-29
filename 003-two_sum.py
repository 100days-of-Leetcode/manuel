'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap ={}

        for i,n in enumerate(nums):
            diff = target - n

            if diff in hashMap:
                return [hashMap[diff],i]

            hashMap[n] = i
