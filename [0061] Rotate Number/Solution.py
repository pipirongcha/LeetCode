# 내 풀이, O(n^2)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        list_len = 1
        tmp = head
        while tmp.next != None:
            tmp = tmp.next
            list_len += 1
        
        k = k % list_len

        
        if k == 0 or k == list_len:
            return head

        while k != 0:
            tmp_node = ListNode(0)
            tmp_node.next = head
            head = tmp_node
            current = head
            while current.next.next != None:
                current = current.next
            head.val = current.next.val
            current.next = None
            k -= 1
        
        return head

# 아래는 O(n) 풀이, 원형 리스트를 만들어 문제를 해결한 뒤, 마지막에 tail -> head 연결을 끊어줌

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        list_len = 1
        tail = head
        while tail.next:
            tail = tail.next
            list_len += 1

        k = k % list_len
        if k == 0:
            return head

        tail.next = head

        steps_to_new_head = list_len - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        new_tail.next = None

        return new_head