"""
难度:简单
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:

输入：s = "abaccdeff"
输出：'b'
示例 2:

输入：s = "" 
输出：' '
 

限制：

0 <= s 的长度 <= 50000
"""
def firstUniqChar(s):
    """
    :type s: str
    :rtype: str
    """
    # 第一个
    # 唯一字符
    i = 0
    d = {}
    while i < len(s):
        d[s[i]] = not s[i] in d
    
    for c in s:
        if d[c]: return c
    return ' '
    
    
if __name__ == '__main__':
    firstUniqChar('aaba')