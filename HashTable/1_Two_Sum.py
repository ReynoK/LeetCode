#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Reyno'

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        O(n)方法，只需遍历一次列表，利用hash表存值和对应的index，利用两个值和为target，
        可以同时获取两者的值，在通过值来获取两个所对应的index。
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