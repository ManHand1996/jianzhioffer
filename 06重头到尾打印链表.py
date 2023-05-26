
"""
难度:简单
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def reversePrint(self, head: ListNode) -> list[int]:
        
        # l = []
        # 1.insert(0,val)
        # res = []
        # if not head:
        #     return l
        # while head.next:
        #     l.insert(0,head.val)
        #     head = head.next
        # l.insert(0,head.val)
        # return l
        
        # 2.递归
        if not head:
            return []
        else:
            
            return self.reversePrint(head.next) + [head.val]

        # 3.利用python list 特性[::-1]
        # while head:
        #     l.append(head.val)
        #     head = head.next
        # return l[::-1]