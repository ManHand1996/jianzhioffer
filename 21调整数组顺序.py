"""
难度:简单
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
 

提示：

0 <= nums.length <= 50000
0 <= nums[i] <= 10000
"""
def exchange(nums: list[int]) -> list[int]:
    """
    解题思路:
    题意是将数组调整成奇数在前,偶数在后
    利用双指针,一头i(奇数),一尾j(偶数)开始遍历
    nums[i] 为奇数跳过,直到找到偶数
    nums[j] 为偶数跳过,知道找到奇数,
    当 nums[i] 为偶数 并且 nums[j]为奇数,则进行交换
    当 i > j 时跳出循环(此时,i,j已经遍历完自己部分)
    
    """
    if len(nums) < 2:
        return nums
    
    i = 0 # 头指针
    j = len(nums) - 1 # 尾指针
    while i < j:
        
        if nums[i] % 2 == 0 and nums[j] % 2 != 0:
            nums[i], nums[j] = nums[j], nums[i]
        if nums[i] % 2 != 0:
            i += 1
        if nums[j] % 2 == 0:
            j -= 1
    return nums
    # 2.遍历后使用额外空间存放, 时间O(N), 空间 O(N)
    # l1 = []
    # l2 = []
    # while i < len(nums):
    #     if nums[i] % 2 == 0:
    #         l2.append(nums[i])
    #     else:
    #         l1.append(nums[i])
    #     i+=1
    # return l1+l2
