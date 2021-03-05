"""
方法一：Dict + 实现双向链表

解题思路：
自己实现带哨兵头节点的双向循环链表
首先使用哈希表进行定位，找出缓存项在双向循环链表中的位置，随后将其移动到双向循环链表的尾部，即可在 O(1) 的时间内完成 get 或者 put 操作

复杂度分析：
时间复杂度：对于 put 和 get 都是 O(1)。
空间复杂度：O(capacity)，因为哈希表和双向链表最多存储 capacity 个元素
"""


class ListNode:
    def __init__(self, key, value):
        self.key = key  # 缓存容量满了时，需要删除双向链表的第一个节点，此时还需要根据 key 去删除哈希表的键值对
        self.value = value
        self.next = None
        self.prev = None


class MyDoublyLinkedList:
    def __init__(self):
        """带头节点的双向循环链表"""
        self.root = ListNode(None, None)  # 哨兵(sentinel)头节点
        self.root.next = self.root
        self.root.prev = self.root

        self.size = 0

    def add_at_tail(self, e: ListNode) -> None:
        """在链表尾部添加节点"""
        # 标准的双向链表插入操作：在节点 p 后面插入节点 e
        tail = self.root.prev  # 最后一个节点

        e.prev = tail  # 口诀：先处理「前」，再处理「后」
        e.next = tail.next
        e.prev.next = e
        e.next.prev = e

        self.size += 1

    def remove(self, e: ListNode) -> ListNode:
        """删除指定节点"""
        # 标准的双向链表删除操作
        e.prev.next = e.next
        e.next.prev = e.prev
        e.next = None  # avoid memory leaks
        e.prev = None  # avoid memory leaks

        self.size -= 1

        return e

    def move_to_end(self, e: ListNode) -> None:
        """将指定节点移动到链表尾部"""
        if self.root.prev == e:
            return

        self.remove(e)
        self.add_at_tail(e)


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}  # 哈希表的键为缓存 key 的引用；值为 ListNode(key, value) 的引用
        self.list = MyDoublyLinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:  # 关键字 key 不存在于缓存中
            return -1

        node = self.map[key]
        self.list.move_to_end(node)  # 双向链表的最后一个节点表示最近被访问的缓存
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:  # 如果关键字已经存在
            node = self.map[key]
            node.value = value
            self.list.move_to_end(node)  # 移动到双向链表的尾部
        else:  # 如果关键字不存在
            # 当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间
            if self.list.size >= self.capacity:
                node = self.list.remove(self.list.root.next)  # 删除双向链表的第一个节点
                del self.map[node.key]  # 删除哈希表中对应的键值对

            # 创建新节点
            node = ListNode(key, value)
            self.map[key] = node
            self.list.add_at_tail(node)
