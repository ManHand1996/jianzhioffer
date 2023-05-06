"""
难度:中等
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
def copyRandomList(head: 'Node'):
    if not head:
        return []
    # 构建新旧节点映射关系
    node = head
    map_nodes = {}
    while node:
        map_nodes[node] = Node(node.val)
        node = node.next
    
    node = head
    while node:
        map_nodes[node].next = map_nodes.get(node.next)
        map_nodes[node].random = map_nodes.get(node.random)
        node = node.next
    return map_nodes[head]
    

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.random = head
    n = copyRandomList(head)
    while n:
        print(n.val)
        print(n.next)
        print(n.random)
        n = n.next