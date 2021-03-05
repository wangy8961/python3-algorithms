"""
方法五: 堆 heapq 模块

解题思路：
假设每个链表的最长的长度是 n，方法四是一次性将 k 个有序链表的 kn 个节点构建一个巨大的小顶堆，堆化过程效率低

我们只维护当前每个链表没有被合并的元素的最前面一个，构建 k 个元素的小顶堆，每次弹出顶堆元素
有两个问题：
1. 无法直接使用 LeetCode 提供的 ListNode 类实例对象构建小顶堆，因为该对象不支持大小比较操作，而你又没办法修改 ListNode 类定义，添加重载 __lt__ 和 __eq__ 魔术方法
2. 如果使用 ListNode 实例对象的 val 值来构建小顶堆，那么弹出堆顶元素后，不知道它属于哪个原链表，也就无法把它的下一个节点值加入堆。另外，使用 val 又像方法四那样需要新建全部节点，弊端太多

我们只需新建一个 HeapNode 类，能保存 ListNode 实例对象并支持大小比较即可

注意: 这里我们需要为合并后新链表创建一个哨兵头节点，这样可以极大的简化 tail.next 判断逻辑，否则就需要判断新链表是否是空链表的特殊情况('NoneType' object has no attribute 'next')

1. 读取 lists 中 k 个有序链表的第一个节点，分别创建为 HeapNode 类的实例对象
2. 构建小顶堆
3. 为合并后新链表创建哨兵(sentinel)头节点 root，它的 val 值随意。并且使用 tail 指针表示合并后新链表的「最后一个节点」
4. 弹出堆顶的 HeapNode 实例，用 tail 指向它的 node 属性表示的链表节点。然后向后移动 tail 指针，始终表示新链表的「最后一个节点」
5. 如果步骤 4 中的实例 node 属性表示的链表节点还有下一个节点，创建为 HeapNode 类的实例对象，然后加入小顶堆，重新进行堆化
6. 重复步骤 4 - 5，直到堆为空
7. 返回哨兵头节点的 next 指针即可


复杂度分析：
时间复杂度：考虑堆中元素不超过 k 个，那么插入和删除的时间代价为 O(logk)，这里最多有 kn 个节点，对于每个节点都被插入和删除各一次，故总的时间代价即渐进时间复杂度为 O(kn * logk)
空间复杂度：堆中元素不超过 k 个，故渐进空间复杂度为 O(k)。
"""
import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
    def __init__(self, node: ListNode = None):
        self.val = node.val
        self.node = node

    # 重载小于比较
    def __lt__(self, other):
        return self.val < other.val

    # 重载等于比较
    def __eq__(self, other):
        return self.val == other.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 读取 lists 中 k 个有序链表的第一个节点，创建为 HeapNode 类的实例对象(对象中引用了链表节点，不存在新建操作，内存消耗小)
        # h = []
        # for node in lists:
        #     if node:  # 排除 [[]] 或 [[], [1,3], [2,6]] 这种情况，此时 node = []
        #         h.append(HeapNode(node))
        h = [HeapNode(node) for node in lists if node]

        # 构建最多 k 个元素的小顶堆
        heapq.heapify(h)

        # 构建结果链表
        root = ListNode(None)  # 哨兵(sentinel)头节点
        tail = root  # 表示合并后新链表的「最后一个节点」

        while h:  # 直到堆为空
            v = heapq.heappop(h)  # 弹出堆顶元素，会进行一次重新堆化

            tail.next = v.node  # tail 指向 v.node 节点
            tail = tail.next  # tail 指针后移

            if v.node.next is not None:
                heapq.heappush(h, HeapNode(v.node.next))  # 又会进行一次重新堆化

        return root.next
