"""
难度:简单
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。


"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(self, root: TreeNode) -> list[list[int]]:
    # 先序遍历(深度优先``)
    # results = []
    # level = 0
    # def recurse(node, level):
    #     if not node:
    #         return None
    #     if len(results) == level:
    #         results.append([])
    #     results[level].append(node.val)
    #     left = recurse(node.left, level+1)
    #     right = recurse(node.right, level+1)
        
    #     return node
    # recurse(root, 0)
    # return results

    # 广度优先
    import collections
    if not root: return []
    results = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        tmp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        results.append(tmp)
    return results