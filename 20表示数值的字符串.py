"""
难度:中等
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

数值（按顺序）可以分成以下几个部分：

若干空格
一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
若干空格
小数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分数值列举如下：

["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
部分非数值列举如下：

["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]


示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false
示例 4：

输入：s = "    .1  "
输出：true
 

提示：

1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。
"""
import re
def isNumberRe(s):
    # (+/-) 小数/整数 (e(+/-)整数)
    # 小数:  .123  123.  123.231
    # 整数: 124
    # ([0-9])?\.[0-9]+|[0-9]+\.([0-9])?
    # ([0-9])?\.([0-9])?
    # ((e|E)[0-9]+)?
    # p = re.compile()
    # ((e|E)(\+|-)?[0-9]+)?
    print(re.fullmatch(r'\s*(\+|-)?((\.)?[0-9]+|[0-9]+\.([0-9]+)?)((e|E)(\+|-)?[0-9]+)?\s*', s))


def isNumber(s):
    
    dot_idx_list = []
    sign_idx = -1  # 开始idx
    e_sign_idx = -1 # 
    e_idx = len(s)  # eE idx
    dot_idx = -1
    prev_charset_idx = -1
    last_charset_idx = len(s)
    float_con = False  # 小数条件
    int_con = False  # 整数条件
    e_con = False  # eE 条件
    
    # 
    # 需要先处理字符串前后空格:
    # 前空格范围: 第一次出现空格到第一次碰到字符集'+-.0123456789eE' index
    # 后空格范围: 最后一次出现的字符集'+-.0123456789eE' index
    # 按照规则将字符串分成三部分
    # 符合部分  数字部分 e部分
    # (+/-) 小数/整数 (e(+/-)整数)
    # 找出符合index, 小数点index, 'eE' index 'eE'整数符号index
    for i in range(len(s)):
        if s[i] not in '+-.0123456789eE ':
            return False
        else:
            if prev_charset_idx == -1 and s[i] != ' ':
                prev_charset_idx = i
            if s[i] != ' ':
                last_charset_idx = i 

            if s[i] in '+-' and e_idx < len(s):
                e_sign_idx = i
            elif s[i] in '+-' and sign_idx == -1:
                sign_idx = i
            elif s[i] in 'eE' and e_idx == len(s):
                e_idx = i
            elif s[i] == '.':
                dot_idx_list.append(i)
                dot_idx = i
    
    prev_charset_idx = 0 if prev_charset_idx == -1 else prev_charset_idx
    new_s = s[prev_charset_idx:last_charset_idx+1]
    
    if prev_charset_idx > -1:
        sign_idx = sign_idx - prev_charset_idx if sign_idx > -1 else -1
        e_sign_idx = e_sign_idx - prev_charset_idx if e_sign_idx > -1 else -1
        e_idx = e_idx - prev_charset_idx if e_idx < len(s) else len(new_s)
        dot_idx = dot_idx - prev_charset_idx if dot_idx > -1 else -1

    sign_con = (sign_idx == 0 or sign_idx == -1)  # 符号条件
    if dot_idx > -1:
        # 小数
        # 小数点 前判断是否数字
        c4 = sign_con and new_s[sign_idx+1:dot_idx].isdigit() and sign_idx+1 < len(new_s)
        # 小数后 前判断是否数字
        c5 = new_s[dot_idx+1:e_idx].isdigit() and dot_idx+1 < len(new_s) # 
        c3 = c4 and c5 # . 前后都数字
        c1 = c4 and (new_s[dot_idx+1:] == '' or new_s[dot_idx+1:e_idx+1] in 'eE') # 只有.前有数字, 则.后一个字符只能是e/E或''
        c2 = c5 and (new_s[sign_idx+1:dot_idx] in '+-' or new_s[:dot_idx] == '')   # # 只有.后有数字, 则.前只能是符合+/-或''
        
        float_con = c1 or c2 or c3
        if len(dot_idx_list) > 1:
            float_con = False 
    else:
        # 整数
        int_con = new_s[sign_idx+1:e_idx].isdigit() and sign_con
    if e_idx < len(new_s):
        e_con = (e_idx + 1 < len(new_s) and new_s[e_idx+1:].isdigit()) or ( e_sign_idx+1 < len(new_s) and e_idx+1 == e_sign_idx and new_s[e_sign_idx+1:].isdigit() )
    else:
        e_con = True
    
    return (float_con or int_con) and e_con


def isNumberDFA(s):
    """
    DFA: 确定有限状态自动机 算法
    根据条件有以下状态集合Q:
    字符串读取从左到右顺序
    0.开始的空格
    1.幂符号前的正负号
    2.小数点前的数字 (小数条件1: 至少一位数字后跟小数点, 整数条件)
    3.小数点后的数字 (小数条件2: 小数点后各至少一位数字)
    4.当小数点前为空格时，小数点后的数字 (小数条件2: 小数点后各至少一位数字)
    5.幂符号
    6.幂符号后的正负号
    7.幂符号后的数字
    8.结尾的空格
    
    字符串遍历后合法的结束状态集合W:
    
    2: 例子: '2' ' 2'  
    3: 例子: ' 2.' ' 2.2' ' .2'
    7: 例子: ' 22e+12' ' 1e2'
    8: 例子 '2e+1 '
    
    函数F 遍历该字符串,对字符串进行状态转移, 结束后判断字符串的状态是否在集合W中,是则该字符串合法(return True),反之(return False)
    转换函数根据集合Q描述的有向图(状态之间转换关系)
    0 + blank => 0
    0 + sign => 1
    0 + digit => 2
    0 + dot => 4
    
    1 + digit => 2
    1 + dot => 4 (中间状态)
    
    2 + blank => 8
    2 + digit => 2
    2 + dot => 3
    2 + e => 5
    
    3 + blank => 8
    3 + digit => 3
    3 + e => 5
    
    
    4 + digit => 3
    
    5 + sign => 6
    5 + digit => 7
    
    6 + digit => 7
    
    7 + digit => 7
    7 + blank => 8
    
    8 + blank => 8
    
    按照规则记录状态集合:
    使用索引表示状态值
    states[i] => list: 记录从那个状态开始
    sattes[i][key] => dict: 表示从状态i遇到字符类型会转换成哪种状态
    
    遍历字符串,
    每个字符串可以分成一下几类:
    c == ' ' or c == '.' => t = c 表示自身为健值
    c in '+-' => t = 's' 表示符号
    c in 'eE' => t = 'e' 幂符号
    其他字符 c = '?'
    
    p = 0: 初始状态
    
    """
    states = [
            {' ':0, 's': 1, 'd':2, '.': 4},
            {'d':2, '.': 4},
            {' ':8, 'd':2, '.': 3, 'e': 5},
            {' ':8, 'd':3, 'e': 5},
            {'d':3,},
            {'s': 6, 'd': 7},
            {'d': 7},
            {' ': 8, 'd': 7},
            {' ': 8}
        ]

    true_states = [2,3,7,8]
    p = 0 # start state
    t = ''
    for c in s:
        
        if c == ' ' or c == '.':
            t = c
        elif c.isdigit():
            t = 'd'
        elif c in '+-':
            t = 's'
        elif c in 'eE':
            t = 'e'
        else:
            t = '?'
        
        p = states[p].get(t, -1)
        if p == -1:
            return False
    return p in true_states
    
    
    
    
        
    
    
    
if __name__ == '__main__':
    res = isNumberDFA('-1.e49046 ')
    print(f'res:{res}')