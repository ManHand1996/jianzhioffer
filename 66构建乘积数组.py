"""
难度: 中等
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 
即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
 

提示：

所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
"""
def constructArr(a: list[int]) -> list[int]:
    # 每一个新数组B的值都是 (n-1)个A元素的乘积(不能使用除法)
    # import functools
    # l = []
    # i = 0
    # m = {}
    # while i < len(a):
        
    #     if not m.get(a[i], None):
    #         left = a[:i]
    #         right = a[i+1:]
    #         # n * n-1 次
    #         m[a[i]] = functools.reduce(lambda x,y :x*y,left+right)
    #     l.append(m[a[i]])
    #     i += 1
    # return l

    # 以A[i]为界划分左右两部分
    # 第一次遍历:计算所有A[i]元素左部分乘积记为B[i]
    # 第二次遍历: 倒序计算所有A[i]元素右部分乘积记为tmp, 将 tmp * B[i] 得到目标值(剩余元素乘积)
    
    # 从前往后计算左部分乘积(跳过第一个开始), 此时b[0]已经计算好
    b, tmp = [1] * len(a), 1
    
    for i in range(1, len(a)):
        b[i] = b[i-1] * a[i-1]

    # 从后往前计算右部分乘积(跳过最后一个开始) 此时b[n-1]已经计算好
    for i in range(len(a) -2,-1,-1):
        tmp = tmp * a[i+1]
        b[i] = tmp * b[i]
    return b