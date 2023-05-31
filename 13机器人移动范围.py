"""
难度:中
"""

def movingCount(self, m: int, n: int, k: int) -> int:
    """
    m行n列的方格
    行坐标i:  0,m-1
    列坐标j:  0,n-1
    s(i) 为i的数位之和
    1.当坐标位数之和 <= k时,
        机械人每次只移动一位,即坐标值增量为1,  ,坐标逢10进1,数位之和+1
        即当 i = 9时, s(i+1) = s(i) - 8
        否则 s(i+1) = s(i) + 1
        即当 (i+1) % 10 时, s(i+1) = s(i) - 8
        否则  s(i+1) = s(i) + 1
    2.符合条件1的坐标需要能够连接起来.
    
    递归
    BFS: 搜索每个坐标是否符合条件, 将每个坐标的右,下方作为下一次判断的条件
    DFS: 沿着当前坐标的某个方向进行搜索, 符合条件的坐标,
            返回 1+ 右方坐标的符合条件数 + 下方坐标符合条件数,
            从底往上返回.
    访问过的坐标(符合条件) 返回0
    不符合条件的坐标 返回0

    符合条件的解,使用队列表示,
    (i,j, si,sj) 分别表示行列坐标, 行坐标i数位之和, 列坐标j数位之和
    BFS 广度优先搜索
    拿出队列中的元素,判断坐标是否符合条件, 如果符合则入队,
    接着将该坐标的右,下坐标(从0,0开始, 只需要判断右方,和下方的坐标是否符合条件即可,然后递归判断),数位之和入队

    """ 
    
    # BFS: 递归 判断当前坐标符合条件后, 将右,下方的坐标作为下次判断的坐标
    queue, results = [(0,0,0,0)], set()    
    while queue:
        i,j,si,sj = queue.pop()
        if i < m and j < n and si + sj <= k and (i,j) not in results:
            results.add((i,j))
            queue.append((i+1, j, si - 8 if (i + 1)%10 == 0 else si + 1,sj))
            queue.append((i, j+1, si, sj - 8 if (j + 1)%10 == 0 else sj + 1))
        else:
            continue
    return len(results)

    # DFS: 递归从底往顶返回符合坐标数
    results = set()
    def dfs(i,j,si,sj):
        if i >= m or j >= n or si + sj > k or (i,j) in results:
            return 0
        results.add((i,j))
        return 1 + dfs(i+1, j, si + 1 if (i+1) % 10 else si - 8, sj) +  dfs(i, j+1, si, sj + 1 if (j + 1) % 10 else sj - 8)
    return len(results)