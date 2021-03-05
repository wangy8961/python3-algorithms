"""
方法一：标准库 collections.OrderedDict

解题思路：
在 Python 语言中，有一种结合了哈希表与双向链表的数据结构 OrderedDict
在 Java 语言中，同样有类似的数据结构 LinkedHashMap

复杂度分析：
时间复杂度：对于 put 和 get 都是 O(1)。
空间复杂度：O(capacity)，因为哈希表和双向链表最多存储 capacity 个元素
"""
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.od = OrderedDict()  # 职责代理
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.od:  # 关键字 key 不存在于缓存中
            return -1

        self.od.move_to_end(key)  # 双向链表的最后一个节点表示最近被访问的缓存
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:  # 如果关键字已经存在
            self.od.move_to_end(key)  # 移动到双向链表的尾部
            self.od[key] = value  # 变更其数据值
        else:  # 如果关键字不存在
            # 当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间
            if len(self.od) >= self.capacity:
                self.od.popitem(last=False)  # 弹出双向链表的第一个节点
                # 或者：
                # oldest = next(iter(self.od))
                # del self.od[oldest]

            self.od[key] = value  # 插入


"""类继承与魔术方法
class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, /, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
            super().__setitem__(key, value)
        else:
            if len(self) >= self.maxsize:
                oldest = next(iter(self))
                del self[oldest]
            super().__setitem__(key, value)
"""
