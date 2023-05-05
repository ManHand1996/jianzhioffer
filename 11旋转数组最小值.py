"""
难度:简单
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，
并按上述情形进行了一次旋转。请返回旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。  

注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

 

示例 1：

输入：numbers = [3,4,5,1,2]
输出：1
示例 2：

输入：numbers = [2,2,2,0,1]
输出：0
 

提示：

n == numbers.length
1 <= n <= 5000
-5000 <= numbers[i] <= 5000
numbers 原来是一个升序排序的数组，并进行了 1 至 n 次旋转

解题思路:
找出最小值: 搜索该数组的一个最小值
最常用的方法:遍历所有,但也是最低效的.
根据条件: 升序排序的数组, 经过旋转(从头n个元素移动到尾部),
得出: 无论如何旋转,该数组都是由最多两个子数组合并.
寻找最小值也就是寻找旋转点
使用二分法是最常用和最有效的搜索方法.
其目的是减少对原数组的元素遍历.
通过比较端点与中间值减少搜索范围
最右端点 > 中间值,则旋转点在中间值与最左端点的闭区间
最右端点 < 中间值,则旋转点在中间值后一位与最右端点的闭区间
最右端点 = 中间值, 则最右端点往前移动一位

https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solutions/102826/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
"""

def minArray(self, numbers):
    """
    :type numbers: List[int]
    :rtype: int
    """
    # 遍历所有
    # min = numbers[0]
    # for i in numbers:
    #     if min >= i:
    #         min = i
    # return min
    """
    最优解:二分法
    设m为中间下标, i,j 分别为数组的头尾下标
    由于输入数组是升序排序数组经过旋转(最开始的若干个元素移动到数组最后位置)后的结果
    即:输入数组为最多两个有序的子数组合并
    所以有:
    m = (i + j)/2
    numbers[m] > numbers[j]: 旋转点(最小值)在m的右边 [m+1, j]
    numbers[m] < numbers[j]: 旋转点(最小值)在m的左边 [i,m]
    numbers[m] == numbers[j]: j = j -1 往前移动一位
    退出条件: i == j
    i ,j = 0, len(numbers)-1
    """
    i, j = 0, len(numbers) - 1
    while i != j:
        mid = (i + j)/2
        if numbers[mid] > numbers[j]:
            i = mid + 1
        elif numbers[mid] < numbers[j]:
            j = mid
        else:
            j -= 1

    return numbers[i]

d = {}
