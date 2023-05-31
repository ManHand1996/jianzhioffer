"""
难度:简单
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    递归寻找p,q最近公共节点:
    1.p,q 在root两则
    2.p == root, q在p左/右
    3.q == root p在q左/右
    
    递归退出条件:
    1.root 为空
    2.root == p 或 root == q 返回 root

    递归寻找root的左右两则情况
    left = root.left
    right = root.right

    left, right 有以下情况 (能判断说明root是普通节点):
    1.left and right 为 空, 直接返回None, 左右都为空, 则说明不在root(当前节点子树)子树当中
    2.left and right 都不为空, 说明p,q在root两则, root为最近公共节点
    3.left == None, right != None, p/q一定在right的子树中(或者right就是p/q)
    4. right == None, left != None , p/q 一定在left子树中(或者left就是p/q)
    """
    p_l = []
    q_l = []
    def recurse(node):
        if not node or node.val == p.val or node.val == q.val:
            return node
        left = recurse(node.left)
        right = recurse(node.right)
        if not left and not right:
            return None
        elif not left:
            return right
        elif not right:
            return left
        else:
            return node

    return recurse(root)