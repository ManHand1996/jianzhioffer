"""
难度:简单
从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。


示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
"""

def isStraight(self, nums: list[int]) -> bool:
    # 不成立条件:
    # 一: 含有重复数字
    # 二: 最大值与最小值之差 >= 5
    # 最大值为13 最小值为1 
    d = {}

    # 最大值与最小值(除了A,K) 相减超过5
    max_v = nums[0]
    min_v = nums[0]
    for num in nums:
        if num != 0:
            if max_v < num or max_v == 0:
                max_v = num
            if min_v > num or min_v == 0:
                min_v = num
            if num in d:
                return False
            d[num] = True
    
    if max_v - min_v >= 5:
        return False
    else:
        return True
