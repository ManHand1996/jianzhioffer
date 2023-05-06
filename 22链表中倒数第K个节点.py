"""
难度:简单
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

 

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
    
    # 自己想法:
    # 计算出链表有多少个节点n
    # 然后往前一定n-k
    
    if not head:
        return None
    # 正解: 双指针,错位前进
    # k:倒数k个, n链表长度,
    # 即需要从第n-k个开始
    # first先移动k位, first剩下需要的是n-k位才遍历完链表
    first = head
    last = head

    for _ in range(k):
        if not first: return
        first = first.next
    
    while first:
        first, last = first.next, last.next
    return last