#내 풀이, O(n log n) 걸렸고 time capacity만 두고 보면 잘 짠 것 같다..!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        tmp = head
        val_list = []
        val_list.append(tmp.val)

        while tmp.next:
            val_list.append(tmp.next.val)
            tmp = tmp.next
        val_list.sort()

        node_list = []   
        for i in range(len(val_list)):
            node_list.append(ListNode(val_list[i]))
        
        result = node_list[0]
        tmp_node = result
        for i in range(len(node_list)-1):
            tmp_node.next = node_list[i+1] 
            tmp_node = tmp_node.next

        return result 
