"""
难度:简单
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
    # node1, node2 分别代表l1,l2 遍历指针, 
    # node1 第一次遇到小于node2 时才改变引用, prev_node_2(初始值None) 表示node2的前一个节点
    # prev_node_2
    # c1大于c2 并且c2 next == None: c2 -> c1
    # 结束时c2.next指向c1
    
    # 特殊情况
    if not l1:
        return l2
    elif not l2:
        return l1
    elif not l1 and not l2:
        return None
        
    node_1 = l1
    node_2 = l2
    prev_node_2 = None
    while node_1:
        tmp = node_1.next
        while node_2:
            # 当node_2比node_1大 对node_2的前一个节点插入node_1
            if node_1.val < node_2.val:
                if prev_node_2:
                    t = prev_node_2.next
                    prev_node_2.next = node_1
                    node_1.next = t
                    # 插入后 node_2的前一个节点变为node_1 
                    prev_node_2 = node_1
                else:
                    # 当node_2为第一个节点,直接将node_1.next变为node_2
                    # 变更后node_2不是第一个节点, prev_node_2 需要变更
                    # l2 的头指针变为node_1
                    node_1.next = node_2
                    prev_node_2 = node_1
                    l2 = node_1
                # node_1插入完成后退出,继续下一个node_1
                break
            else:
                # node_2 往前推进
                # 记录新的node_2前节点 prev_node_2
                prev_node_2 = node_2
                node_2 = node_2.next
        # 当node_2(l2) 遍历完毕马上退出
        # 结束时, prev_node_2为l2最后一个节点, node_1为l2最后一个节点或None
        if not node_2:
            break
        node_1 = tmp
    # 若prev_node_2为最后节点, 拼接剩余的node_1, 此时node_1.val > prev_node_2.val
    if not prev_node_2.next:
        prev_node_2.next = node_1
    return l2

def mergeTwoListsN(l1, l2):
    # 比较l1.val与l2.val , 使新指针cur 按大小顺序进行指向
    # 蛇皮走位
    
    cur, dump = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
           cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    
    cur.next = l1 if l1 else l2
    return dump.next

def mergeTwoListsRecurse(l1, l2):
    # 3.递归
    if l1 == None: return l2
    if l2 == None: return l1
    if l1.val <= l2.val:
        l1.next = mergeTwoListsRecurse(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoListsRecurse(l1, l2.next)
        return l2
        