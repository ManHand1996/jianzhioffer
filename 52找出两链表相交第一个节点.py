"""
难度:简单
(双指针)
输入两个链表，找出它们的第一个公共节点。

如下面的两个链表：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

注意:
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    """
    由数学公式推到算法:
    找出两链表第一个相交节点:
    a 链表A长度
    b 链表B长度
    c 公共节点长度(c >= 0)

    A各个节点与B的各个节点比较,找到相同节点退出
    通常来说是逐个比较: (for A for B. 嵌套循环) 时间复杂度O(M*N)
    但要求时间复杂度为O(n), 空间复杂度为O(1)
    由于有公共部分:
    所与A链表独有的节点长度为: a -c
    B链表独有的节点长度为: b - c
    遍历A然后遍历B长度为: a-c + b
    遍历B然后遍历A长度为: b-c + a
    所以时间复杂度最差为 O(a+b)

    循环终止条件: p_A == p_B (p_A,p_B 可以为None)
    每次循环p_A与p_B都往前移动一次(next)
    当p_A为None(到链表A尾部) 指向 链表B
    当p_B为None(到链表B尾部) 指向 链表A
    
    """
    p_A, p_B = headA, headB
    while p_A != p_B:
        p_A = p_A.next if p_A else headB
        p_B = p_B.next if p_B else headA
    return p_A
