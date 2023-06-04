"""
难度:中等
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

示例 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
示例 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

限制：

0 <= 节点个数 <= 5000
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
    """
        preorder:前序遍历:[3,9,20,15,7]
        inorder:中序遍历:[9,3,15,20,7]
        前序遍历: 确认根节点root
        中序遍历: 根据前序遍历的root知道根节点左,右子树数量
        对左右子树递归
        root = 3  preorder[0] inorder[1]
        left = [9] 
            root = 9 preorder[1] inorder[0]
            left = []
            right = []
        right = [15,20,7]
            root = 20 preorder[2] inorder[3]
            left = [15]
                root = 15 preorder[3] inorder[2]
                left = []
                right = []
            right = [7]
                root = 7 preorder[4] inorder[4]
                left = []
                right = []
        
        left,right=0,0 表示左右子树范围
        i: preorder,根节点索引
        dic: 根节点在inorder索引
        当前节点为: preorder[i]
        j = dic[preorder[i]]
        
        inorder左子树范围: [left, j-1]
        inorder右子树范围:[j+1, right]
        下一个根节点(左): i+1
        下一个根节点(右): i+1+j-left  # 左子树数量(j-left) + 当前根节点索引(i)+1
    """
    s = len(preorder)
    if s == 0:
        return None
    dic, preorder = {}, preorder
    def recurse(root, left, right):
        if left > right:
            # 没有找到
            return None
        node = TreeNode(preorder[root])
        i = dic[preorder[root]]  # 根节点inorder中的索引, i刚好可以表示根节点左子树节点数量
        node.left = recurse(root+1, left, i-1)  # root+1, preorder中根节点左数作为新的root
        node.right = recurse(i-left+root+1, i+1 ,right)  # root + i 左子树数量+1, 剩下的是右子树
        return node
    
    for i in range(s):
        dic[inorder[i]] = i
        
    return recurse(0,0, s-1)