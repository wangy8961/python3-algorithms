from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return repr(self.val)


class Solution:
    def arr_to_list(self, arr: List[int]) -> ListNode:
        """从数组新建链表"""
        root = ListNode(None)  # 哨兵(sentinel)头节点
        tail = root  # 表示合并后新链表的「最后一个节点」
        for i in arr:
            node = ListNode(i)
            tail.next = node
            tail = tail.next
        return root.next

    def print_list(self, head: ListNode) -> str:
        """遍历链表"""
        cur = head
        while cur:
            print(cur.val, '->', end=' ')
            cur = cur.next
        print('∅')

    def get_last_node(self, head: ListNode) -> ListNode:
        """返回最后一个节点"""
        if not head:
            return head

        cur = head
        while cur.next:
            cur = cur.next
        return cur

    def get_middle_node(self, head: ListNode) -> ListNode:
        """获取中间节点
        (1) 如果有两个中间节点，则返回第二个中间节点
        此时，快指针可以前进的条件是：当前快指针和当前快指针的下一个节点都非空
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        (2) 如果有两个中间节点，则返回第一个中间节点
        此时，快指针可以前进的条件是：当前快指针的下一个节点和当前快指针的下下一个节点都非空
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        """
        if not head:
            return head

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_lists(self, l1: ListNode, l2: ListNode):
        """依次从 l1 和 l2 中取一个节点构建新链表(头指针为 l1)
        注意：只适用于 l1 的节点个数等于 l2 的节点个数，或者 l1 比 l2 多一个节点的情况
        """
        while l1 and l2:
            temp = l1.next
            l1.next = l2
            l1 = temp

            temp = l2.next
            l2.next = l1
            l2 = temp

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """合并两个链表，无论 l1 和 l2 的节点个数是多少"""
        root = ListNode(None)  # 哨兵(sentinel)头节点
        tail = root  # 表示合并后新链表的「最后一个节点」，依次从 l1 和 l2 中取一个节点构建新链表

        while l1 and l2:
            tail.next = l1
            l1 = l1.next
            tail = tail.next

            tail.next = l2
            l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return root.next

    def merge_two_sorted_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """合并两个有序链表"""
        root = ListNode(None)  # 哨兵(sentinel)头节点
        tail = root  # 表示合并后新链表的「最后一个节点」

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1  # tail 指向 l1 所在的节点
                l1 = l1.next  # l1 指针后移
            else:
                tail.next = l2  # tail 指向 l2 所在的节点
                l2 = l2.next  # l2 指针后移

            tail = tail.next  # tail 指针后移

        tail.next = l1 or l2
        return root.next

    def reverse(self, head: ListNode) -> ListNode:
        """反转链表"""
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

    def swap_pairs(self, head: ListNode) -> ListNode:
        """两两交换链表中的节点"""
        root = ListNode(None)  # 哨兵(sentinel)头节点
        root.next = head  # 头节点指向原链表的第一个节点

        cur = root
        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next

            # cur -> node1 -> node2 -> x 变成 cur -> node2 -> node1 -> x
            x = node2.next
            node1.next = x
            node2.next = node1
            cur.next = node2

            cur = cur.next.next

        return root.next

    def reorder_list(self, head: ListNode) -> None:
        """重排(折叠)链表

        给定链表 1->2->3->4, 重新排列为 1->4->2->3.
        给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
        """
        if not head:
            return head

        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        i, j = 0, len(arr) - 1
        while i < j:
            arr[i].next = arr[j]
            i += 1
            if i == j:
                break

            arr[j].next = arr[i]
            j -= 1

        arr[i].next = None


if __name__ == "__main__":
    print('-' * 20)
    s = Solution()

    # arr = []
    # arr = [1]
    # arr = [1, 2]
    arr = [1, 2, 3, 4, 5]
    head = s.arr_to_list(arr)
    print('The initial list: ')
    s.print_list(head)
    print('-' * 20)

    print('Last node: ', s.get_last_node(head))
    print('-' * 20)

    print('Middle node: ', s.get_middle_node(head))
    print('-' * 20)

    l1 = s.arr_to_list([1, 2, 3])
    l2 = s.arr_to_list([5, 4, 6, 7, 8])
    s.merge_lists(l1, l2)
    s.print_list(l1)
    print('-' * 20)

    l1 = s.arr_to_list([1, 2, 3])
    l2 = s.arr_to_list([5, 4, 6, 7, 8])
    new_head = s.merge_two_lists(l1, l2)
    s.print_list(new_head)
    print('-' * 20)

    # print('After reverse: ')
    # s.print_list(s.reverse(head))
    # print('-' * 20)

    # print('After swap pairs: ')
    # s.print_list(s.swap_pairs(head))
    # print('-' * 20)

    print('After reorder: ')
    s.reorder_list(head)
    s.print_list(head)
    print('-' * 20)
