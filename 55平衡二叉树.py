"""
难度:简单
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(self, root: TreeNode) -> bool:
    # 遍同时历左右两分支,
    
    # self.left != None c_left +=1
    # self.right != None c_right += 1
    # 当self.left == None
    if not root:
        return True
    def count_deep(r):
        """
        递归, 从底到顶计算并返回每个节点的左右深度差,
        顺序(顶节点, 次顶节点.. 底节点)
        若左右深度差 <= 1 返回该节点的最大深度值
        否则返回 -1
        最后如果 返回值是-1 则说明该二叉树不是平衡二叉树
        """
        if r == None:
            return 0
        left = count_deep(r.left)
        # 子节点左树是否符合平衡二叉树判断, 如果为-1 则直接往上返回
        if left == -1:
            return -1
        # 子节点右树是否符合平衡二叉树判断
        right = count_deep(r.right)
        if right == -1:
            return -1
        m = max(left, right) + 1 # 当前节点的最大深度, 加1 表示该当前节点
        if abs(left - right) <= 1:
            return m
        else:
            return -1
    
    return count_deep(root) != -1