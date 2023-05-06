"""
难度:中等

写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。

 

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
"""

def strToInt(s):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    i = 0
    start_i = -1
    end_i = -1
    first_c = ''
    while i < len(s):
        if s[i] != ' ' and first_c == '':
            first_c = s[i]

            if first_c in '+-' or first_c.isdigit():
                start_i = i
                end_i = i
            else:
                return 0
        
        if first_c != '' and s[i] in '0123456789' and end_i + 1 == i:
            end_i = i
        i += 1
    
    if start_i == -1 or end_i == -1:
        return 0

    try:
        s_int = int(s[start_i:end_i+1])
        
        if s_int <= INT_MAX and s_int >= INT_MIN:
            res = s_int
        elif s_int > INT_MAX:
            res = INT_MAX
        else:
            res = INT_MIN
    except:
        res = 0
    return res


def strToIntDFA(s: str) -> int:
    """
    str转换整数
    1.忽略开头空格
    2.从第一个非空格字符开始 s
        2.1 s in (+/-) ,该符号作为其后尽可能多的连续整数的+-符号
        2.2 s isdigit , 其后的连续数字字符组合成整数
        2.3 (s not in '+-' and s is not a number) or str empty or str is all space
            break and return 0
    3.其他多余字符忽略: '  +12ffs +-' => +12
    4.当转换后的数值超过 [-2**31, 2**31-1]
    """
    # 2.有限状态自动机解法
    """
    字符状态Q:
    0.空字符
    1.第一个符号字符
    2.第一个数字字符
    3.数字字符
    
    合法字符状态:
    3
    
    关系:
    0 + blank => 0
    0 + sign => 1
    0 + digit => 2

    
    1 + digit => 3

    2 + digit => 3
    
    3 + digit => 3
    
    [{' ':0, 's': 1, 'd': 2}]
    [{'d': 3}]
    [{'d':3}]
    [{'d': 3}]
    
    """
    states = [
        {' ':0, 's': 1, 'd': 2},
        {'d': 3},
        {'d': 3},
        {'d': 3},
    ]
    MAX_INT = 2**31-1
    MIN_INT = -2**31
    p = 0
    i = 0
    t = ''
    start_i = -1
    end_i = -1
    res = 0
    while i < len(s):
        if s[i] == ' ':
            t = ' '
        elif s[i] in '+-':
            t = 's'
        elif s[i] in '0123456789':
            t = 'd'
        else:
            t = '?'
        p = states[p].get(t, -1)
        
        if p == -1:
            break
        
        if p in (1,2):
            start_i = i
            end_i = i
        elif p == 3:
            end_i = i
        i += 1
    new_s = s[start_i: end_i+1]
    if start_i == -1 or start_i == -1 or new_s in ['+', '-']:
        res = 0
    else:
        res = int(s[start_i: end_i+1])
        if res > MAX_INT:
            res = MAX_INT
        elif res < MIN_INT:
            res = MIN_INT
    return res


def strToIntBest(s: str) -> int:
    """
    (space)(+-)number(not number)
    
    找出第一个非空字符位置i
    如果第一个非空字符是符号, 并记录sign表示正负值, 设置i+=1
    从i开始遍历, 遇到非数字则退出循环
    数字从左至右即,当前位比上一位小10倍
    0-9字符转整数: int_c = ASCII(c) - ASCII('0')
    
    结果 res = 10 * res + int_c
    
    MAX_INT = 2**31 - 1  # 最大值 2147483647
    MIN_INT = -2**31 # 最小值 -2147483648
    bndry =  2**31 // 10 # 214748364 边界值, 当res
    
    res有范围限制,
    当上一个res > bndry, 
    当上一个res == bndry && int_c > 7 
    根据sign 返回最大或最小值,
    
    计算当前值: res = 10*res+ int_c
    
    最后返回: sign*res
    
    """
    MAX_INT = 2**31 - 1  # 最大值 2147483647
    MIN_INT = -2**31 # 最小值 -2147483648
    bndry =  2**31 // 10 # 214748364 边界值, 当res
    i = 0 # 第一个非空字符
    sign = 1 # 正负符号
    res = 0
    if not s:
        return 0
    
    # 跳过字符串前的空格字符
    while s[i] == ' ':
        i += 1
        if len(s) == i:
            return 0
    
    # 第一个非空字符是-
    if s[i] == '-':
        sign = -1
    
    # 第一个非空格,非符号
    if s[i] in '+-':
        i += 1
    
    
    while i < len(s):
        if s[i] not in '0123456789':
            break
        else:
            x =  (ord(s[i]) - ord('0'))
            if res > bndry or  (res == bndry and x > 7):
                return MAX_INT if sign == 1 else MIN_INT
            res = 10 * res + x
        i += 1
    return sign*res

        
    
if __name__ == '__main__':
    print(strToInt('    +2147483648'))