"""
难度:中等
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 true，否则返回 false。
假设输入的数组的任意两个数字都互不相同。
"""

import collections
def verifyPostorder(self, postorder: list[int]) -> bool:
    # 后序遍历, 二叉搜索树
    if len(postorder) <= 1:
        return True
    """
    二叉搜索树的后序遍历list,最后一个必定是根节点root
    并且,满足左子树的所有值 < root, 右子树的所有值 > root
    所以顺序遍历list,将list[i]> root 放到right, list[i] < root 放到left,
    然后判断 left + right 是否与 该list顺序相等(除了根节点)
    如果不一样则list不满足后序遍历
    对left, right 子树,重复上述步骤,直到left,right剩余一个节点
    算法:
    后序遍历list最后一个值为root:  root = list.pop()
    辅助栈记录需要判断的根节点: queue.append(root)
    辅助映射: d[root] = list
    顺序遍历 p = d[root]
    如果 p[i] > root: right.append(p[i])
    否则: left.append(p[i])
    接着判断left + right 是否与 d[root] 顺序相同
    
    对left,right子树, 找出新的根节点,和映射d
    
    空间复杂度: O(4N)
    时间复杂度: O(logN*N)
    
    """
    
    queue = collections.deque()
    queue.append(postorder.pop())
    d = {queue[-1]:postorder}
    while queue:
        root = queue.popleft()
        left = []
        right = []
        for i in d[root]:
            if i > root: right.append(i)
            else: left.append(i)
        if left + right != d[root]:
            return False
        if len(left) > 1:
            queue.append(left.pop())
            d[queue[-1]] = left
        if len(right) > 1:
            queue.append(right.pop())
            d[queue[-1]] = right
    return True