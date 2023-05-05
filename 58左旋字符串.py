"""
难度:简单
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"
示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
 

限制：

1 <= k < s.length <= 10000
"""
def reverseLeftWords(self, s, n):
    """
    :type s: str
    :type n: int
    :rtype: str
    """
    # 1.python字符串切片
    # 空间复杂度O(N), 时间复杂度0(N)
    # return s[n:]+s[:n]

    # 2.遍历实现
    # list实现,通过取模获取下标
    # 空间复杂度O(N), 时间复杂度0(N)
    new_s = []
    for i in range(n , n + len(s)):
        new_s.append(s[i % len(s)])
    return ''.join(new_s)

    # 3.遍历实现
    # 空间复杂度O(N), 时间复杂度0(N)
    # 不使用Python内置方法, 最低效,需要申请n次内存分配
    # 因为字符串是不可变对象, 每次变更都会重新分配内存
    # new_s = ''
    # for i in range(n, n + len(s)):
    #     new_s += s[i % len(s)]
    # return new_s