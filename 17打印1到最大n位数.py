"""
难度: 简单
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 

说明：

用返回一个整数列表来代替打印
n 为正整数
"""

def printNumbers(n: int) -> list[int]:
    
    return list(range(1, 10**n))





class Solution:
    def printNumbers(self, n: int) -> list[int]:
        self.count = 0
        def dfs(x):
            self.count += 1
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(s)
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1
        
        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        print('printNumbers use count:', self.count)
        return ','.join(res)
    
    def printNumbers2(self, n: int) -> str:
        """
        全排列组合:
        从高位开始固定, 递归获取组合数字
        n = 2:
        0[0-9]
        1[0-9]
        2[0-9]
        ..
        9[0-9]
        
        存在问题:
        1.有前导0
        2.从0开始, 要求从1开始
        """
        def dfs(x, num):
            if x == n: # 终止条件：已固定完所有位
                # 消除前缀0, 遇到第一个非0数字退出
                start = 0
                while start < len(num):
                    if num[start] == '0':
                        start += 1
                    else:
                        break
                # 从1开始
                if start < len(num):
                    res.append(''.join(num[start:])) # 拼接 num 并添加至 res 尾部
                return
            for i in range(10): # 遍历 0 - 9
                num[x] = str(i) # 固定第 x 位为 i
                dfs(x+1, num) # 开启固定第 x + 1 位
        res = [] # 数字字符串列表
        dfs(0, ['0']*n) # 开启全排列递归
        return ','.join(res)  # 拼接所有数字字符串，使用逗号隔开，并返回

if __name__ == '__main__':
    
    s = Solution()
    # s.printNumbers(3)
    print(s.printNumbers2(3))