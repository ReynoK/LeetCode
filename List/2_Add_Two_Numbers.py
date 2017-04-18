#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'reyno'

import itertools
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#class Solution(object):
#   def addTwoNumbers(self, l1, l2):
#       """
#       :type l1: ListNode
#       :type l2: ListNode
#       :rtype: ListNode
#       """
#       op1 = l1
#       op2 = l2
#       carry = 0
#       res_list_node = None
#       res_point = None
#       while op1 is None and op2 is None:
#           
#           if op1 is None and op2 is None:
#               break
#           else:
#               op1_val = 0 if op1 is None else op1.val
#               op2_val = 0 if op2 is None else op2.val
#               
#               res = (op1_val + op2_val + carry)%10
#               carry = (op1_val + op2_val + carry)/10
#               
#               list_node = ListNode(res)
#               
#               if res_list_node is None:
#                   res_list_node = list_node
#                   res_point = res_list_node
#               else:
#                   res_point.next = list_node
#                   res_point = res_point.next
#                   
#           op1 = op1.next if op1 is not None else None
#           op2 = op2.next if op2 is not None else None
#       if carry != 0:
#           res_point.next = ListNode(carry)
#           
#       return res_list_node

#class Solution(object):
#   def addTwoNumbers(self, l1, l2):
#       """
#       :type l1: ListNode
#       :type l2: ListNode
#       :rtype: ListNode
#       """
#       op1 = l1
#       op2 = l2
#       carry = 0
#       sum_ = 0
#       res_list_node = ListNode(None)
#       node_ptr = res_list_node
#       while op1 is not None or op2 is not None:
#           sum_ = carry
#           
#           if op1 is not None:
#               sum_ += op1.val
#               op1 = op1.next
#           
#           if op2 is not None:
#               sum_ += op2.val
#               op2 = op2.next
#               
#           carry = sum_ / 10
#           res = sum_ % 10
#
#           node_ptr.next = ListNode(res)
#           node_ptr = node_ptr.next
#
#       if carry != 0:
#           node_ptr.next = ListNode(carry)
#           
#       return res_list_node.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res_list_node = node_ptr = ListNode(None)
        # 需要注意最后一位相加可能需要进位
        while l1 or l2 or carry:    
            if l1:
                carry += l1.val
                l1 = l1.next
            
            if l2:
                carry += l2.val
                l2 = l2.next
                
            node_ptr.next = node_ptr = ListNode(carry % 10)
            carry = carry / 10
            
        return res_list_node.next
        
def make_list_node(list_):
    begin_list_node = None
    list_node_ptr = None
    for val in list_:
        if begin_list_node is None:
            begin_list_node = ListNode(val)
            list_node_ptr = begin_list_node
        else:
            list_node_ptr.next = ListNode(val)
            list_node_ptr = list_node_ptr.next
            
    return begin_list_node
            
def get_list_node_value(list_node):
    while list_node is not None:
        yield list_node.val
        list_node = list_node.next
        
def test_solution(list1, list2, expect):
    list_node_one = make_list_node(list1)
    list_node_two = make_list_node(list2)
    s = Solution()
    res = s.addTwoNumbers(list_node_one, list_node_two)
    res = list(get_list_node_value(res))
    
    for m,n in itertools.izip_longest(res,expect):
        assert m == n, str(res) + '!=' + str(expect)
        
if __name__ == "__main__":
    test_solution([2,4,3], [5,6,4], [7,0,8])
    test_solution([5], [5], [0,1])
                    
                    
        