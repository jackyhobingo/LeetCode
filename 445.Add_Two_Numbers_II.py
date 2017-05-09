# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        parent_list_l1 = []
        parent_list_l2 = []
        while l1:
            parent_list_l1.append(l1.val)
            l1 = l1.next
        while l2:
            parent_list_l2.append(l2.val)
            l2 = l2.next
        carry = 0
        ans = None
        while parent_list_l1 or parent_list_l2 or carry != 0:
            l1_val = parent_list_l1.pop() if parent_list_l1 else 0
            l2_val = parent_list_l2.pop() if parent_list_l2 else 0
            sum_ = carry + l1_val + l2_val
            carry = sum_ / 10
            temp_node = ListNode(sum_ % 10)
            temp_node.next = ans
            ans = temp_node
        return ans
