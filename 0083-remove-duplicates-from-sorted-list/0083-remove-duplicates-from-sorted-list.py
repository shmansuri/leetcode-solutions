# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        #Broute Force
        # temp = head
        # while temp:
        #     currentNode = temp.next
        #     preNode = temp
        #     while currentNode:
        #         if currentNode.val == temp.val:
        #             preNode.next = currentNode.next
        #             currentNode= currentNode.next
        #         else:
        #             preNode = currentNode
        #             currentNode = currentNode.next
            
        #     temp = temp.next
        # return head

    #optimize code
        existNode = set()
        temp = head
        currentNode = None
        while temp:
            if temp.val not in existNode:
                existNode.add(temp.val)
                currentNode = temp
                temp = temp.next
            else:
                currentNode.next = temp.next
                temp= currentNode.next
        
        return head
