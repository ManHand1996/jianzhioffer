"""
难度:简单
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(self, root: TreeNode) -> bool:
    # 方法1: 先进行镜像得到mirror_root,然后递归判断镜像树与原树节点值是否一致
    # 时间:O(2logN) 空间:(2N) 
    def mirror(node, mirror_root):
        if not node:
            return None, None
        left, mirror_left = mirror(node.left, mirror_root)
        right, mirror_right = mirror(node.right, mirror_root)
        
        mirror_root = TreeNode(node.val)
        mirror_root.left = mirror_right
        mirror_root.right = mirror_left
        return node, mirror_root
    
    root, mirror_root = mirror(root, None)

    def recurese(a, b):
        if not a and not b:
            return True
        
        if (not a and b) or (not b and a):
            return False

        if a.val != b.val:
            return False
        
        left = recurese(a.left, b.left)
        right = recurese(a.right, b.right)
        return left and right

    # 方法2 ,镜像后的树与原树一样,则 必有:
    # 1.左树根节点与右树根节点相同
    # 2.左树的左则与右树的右则相同
    # 3.左树的右则与右树的左则相同
    # # 时间:O(logN) 空间:(N) 

    def recur(L,R):
        # 同时为空
        if not L and not R:
            return True
        if not L or not R or L.val != R.val:
            return False
        return recur(L.left, R.right) and recur(L.right, R.left)

        

    return recur(root.left, root.right) if root else True