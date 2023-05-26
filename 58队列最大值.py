"""
难度:中等
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
"""

import queue
class MaxQueue:
    """
    思路: 使用额外的双端队列m表示最大值(第一个元素),
    在入队时, 将m队列中所有小于新值value 的元素弹出,使双端队列保持单调减
    """
    def __init__(self):
        
        self.s = queue.Queue()
        self.m = queue.deque() # max value 第一个值为最大值

    def max_value(self) -> int:
        if not self.m:
            return -1
        else:
            return self.m[0]


    def push_back(self, value: int) -> None:
        self.s.put(value)
        while self.max_value() != -1 and self.m[-1] < value:
            self.m.pop()
        self.m.append(value)



    def pop_front(self) -> int:
        if self.s.empty():
            return -1
        else:
            x = self.s.get()
            if x == self.max_value():
                self.m.popleft()
            return x