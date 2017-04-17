#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Reyno'

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = dict()
        for index,num in enumerate(nums):
            if num in hash_table:
                return [hash_table[num],index,]
            hash_table[target - num] = index
            
        
if __name__ == '__main__':
    nums = [3,2,4]
    s = Solution()
    print(s.twoSum(nums,6))