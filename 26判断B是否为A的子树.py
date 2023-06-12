"""
难度:中等
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构(左右相等)和节点值。

值会重复出现

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

    # 确认B树根节点在A的哪个方向(根节点,左子树,右子树)
    # 三种情况之一: B在A根节点上, B在A左子树, B在A右子树
    def isSub(a, b):
        if not a or not b:
            return False
        return recurse(a,b) or isSub(a.left, b) or isSub(a.right, b) 
        
    # 递归判断b树子结构是否为a树的子结构(值与方向一样)
    def recurse(a,b):
        if not b:
            return True
        if not a or a.val != b.val:
            return False
        return recurse(a.left, b.left) and recurse(a.right, b.right)
    return isSub(A,B)