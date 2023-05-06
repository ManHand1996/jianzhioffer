"""
难度简单
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 

限制：

0 <= 节点个数 <= 5000
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(self, head: ListNode) -> ListNode:
    # 2. time:O(N), space:O(N)
    # 临时变量保持next,
    # node.next 指向 prev
    prev = None
    node = head
    while node:
        # l.append(head.val)
        tmp = node.next
        node.next = prev
        prev = node
        node = tmp
    return prev