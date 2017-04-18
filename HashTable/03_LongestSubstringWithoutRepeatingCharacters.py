#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Reyno'

class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     front,rear = 0,0
    #     max_sub_len = 0
    #     tag_map = dict()
    #     while rear < len(s):
    #         alpha = s[rear]
    #         if alpha in tag_map:
    #             len_ = rear - front
    #             max_sub_len = max_sub_len if max_sub_len > len_ else len_
    #             front = tag_map[alpha] + 1
    #             tag_map[alpha] = rear
    #         else:
    #             tag_map[alpha] = rear
    #         rear += 1
    #     len_ = rear - front
    #     max_sub_len = max_sub_len if max_sub_len > len_ else len_

    #     return max_sub_len

    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     start = 0
    #     max_sub_len = 0
    #     got_char = dict()
    #     for rear in xrange(len(s)):
    #         char = s[rear]
    #         if char in got_char and got_char[char] >= start:
    #             start = got_char[char] + 1
    #         else:
    #             max_sub_len = max(max_sub_len, rear - start + 1)
            
    #         got_char[char] = rear

    #     return max_sub_len

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Des:因为是寻找子字符串，因此首先想到需要使用前后两个指针，然后指针会向后移动，此时要考虑到当
        遇到相同字母时怎么变化指针的位置，此时想到怎么样才能快速的得到重复字母的位置，然后想到用
        hashtable记录字母出现的位置，当重复字母出现的时候，应该从相对应的前面重复字母(start之后的)
        的下一个位置重新开始寻找最大子字符串。时间复杂度为o(n)。
        """
        start = 0
        max_sub_len = 0
        got_char = dict()
        for rear,char in enumerate(s):
            if char in got_char and got_char[char] >= start:
                start = got_char[char] + 1
            else:
                max_sub_len = max(max_sub_len, rear - start + 1)
            
            got_char[char] = rear

        return max_sub_len

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(""))
    print(s.lengthOfLongestSubstring("c"))
    print(s.lengthOfLongestSubstring("ca"))
    print(s.lengthOfLongestSubstring("dvdf"))
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("tmmzuxt"))

