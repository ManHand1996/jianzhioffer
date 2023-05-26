"""
难度: 困难
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

你可以假设 k 总是有效的，在输入数组 不为空 的情况下，1 ≤ k ≤ nums.length。
"""   
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
        # N*K
        # 滑动窗口个数: n - k + 1
        # (n - k + 1) * k/2 => n*k - k*k + k
        # 上一个滑动窗口最大值 max_idx (索引)
        # 滑动窗口起始: i, i+k
        
        # 最大值出现位置:
        # 1.滑动窗口重叠部分
        # 2.移动后窗口最后元素

        # 设上一个滑动窗口最大值索引为 max_idx
        # 判断当前窗口最大值位置, i, i+k 为窗口左右边界
        # 情况1: 在新窗口中 i <= max_idx <= i+k
        #      若 nums[max_idx] > nums[i+k] 最大值为 nums[max_idx] 
        #      若 nums[max_idx] <= nums[i+k] 最大值为 nums[i+k]
        # 情况2: 在新窗口左边界前一位
        #       若 nums[max_idx] <= nums[i+k] 最大值为 nums[i+k]
        #       若 nums[max_idx] > nums[i+k] 
        #  则需要将nums[i+k]与重复部分的最大值比较, 即需要比较上一个滑动窗口的第二(三四..)大的值直到找到符合的值.(额外存储?)
        #  滑动窗口存储升序的值? 
        #  单调栈记录当前滑动窗口的最大值, 降序
        # 空间换时间!       
        
        i = 0
        m = []
        deque = [] # 当前滑动窗口的降序值 ,deque[0] => 最大值
        n = len(nums)
        def deque_popleft(deque):
            re = []
            if len(deque) > 1:
                re = deque[1:]
            elif len(deque) == 1:
                re = []
            return re
        
        
        # 确保每个元素都入栈
        # 每个元素都作为滑动窗口的右边界
        for i, j in zip(range(1-k, n-k+1), range(n)):
            # 删除不在当前滑动窗口的 最大值 左边界
            if i > 0 and deque[0] == nums[i - 1]:
                deque = deque_popleft(deque)
            
            # 删除新值(最右边界值) 比 deque 内大的值
            # 从而保证, deque里是降序
            while deque and deque[-1] < nums[j]:
                deque.pop()

            deque.append(nums[j])
            if i >= 0:
                m.append(deque[0])
        return m

        