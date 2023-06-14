
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: TreeNode, target: int) -> list[list[int]]:
    """
    递归遍历每个节点,
    递归过程中,将s路径和与目标值target进行比较,如果相等则添加到结果res
    """
    if not root:
        return []

    res = []
    def recurse(node, path):
        
        if not node.left and not node.right:
            if sum(path) == target:
                res.append(path)
                return path
            return
        if node.left: recurse(node.left, path+[node.left.val]) 
        if node.right: recurse(node.right, path+[node.right.val]) 
        return

    recurse(root, [root.val])
    return res

def pathSum2(root: TreeNode, target: int) -> list[list[int]]:
    """
    递归遍历每个节点, 将当前节点值添加到path中,
    然后减去当前节点值,target -= node.val
    target为0 并且当前node 为叶子节点,则将path添加到res中
    最后往上层返回时,将path弹出: 到根节点时会清空path
    """
    res, path = [], []
    def recurse(node, s):
        if not node:
            return
        path.append(node.val)
        s -= node.val
        if s == 0 and not node.left and not node.right:
            # 只有一个值的时候
            res.append(list(path))
        recurse(node.left, s) 
        recurse(node.right, s)
        path.pop()

    recurse(root, target)
    
    return res