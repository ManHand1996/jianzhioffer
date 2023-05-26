
"""
难度:简单
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 

限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    """
    nums为递增数组
    nums[i] + nums[j] == target:退出
    必然: nums[i] < target, nums[j] < target
    移动i,j
    j -=1: 
        当target < nums[j] +  nums[i] 时, 表示j过大
        当target < nums[j] 时, 比目标值大
    i += 1:
        target > nums[j] + nums[i] 

    退出条件: i < j 或 nums[i] + nums[i] == target


    """
    i = 0 # 小
    j = len(nums) - 1 # 大
    while i < j:
        if nums[j] > target or target - nums[i] < nums[j]:
            j -= 1
        else:
            i += 1 
        
        if nums[i] + nums[j] == target:
            return [nums[i],nums[j]]
    
    # 耗时与自己的想法一样,但这种解法更清晰
    # 2.先计算 s = nums[i] + nums[j]
    # 升序数组,必然 nums[j] > nums[i], i,j 表示数组头尾指针
    # s > target: 表示过大, 需要 j -= 1 (减少s只有移动j)
    # s < target: 表示国小, 需要 i += 1 (增大s只有移动i)
    while i < j:
        s = nums[i] + nums[j]
        if s > target:
            j -= 1
        elif s < target:
            i += 1
        else:
            return [nums[i], nums[j]]
