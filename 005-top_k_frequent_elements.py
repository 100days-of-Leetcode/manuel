'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
'''

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1

        sorted_items = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)

        top_k = []
        for i in range(k):
            top_k.append(sorted_items[i][0])

        return top_k