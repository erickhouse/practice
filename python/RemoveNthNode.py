# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object): #1->2->3 2
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
       
        if head.next == None and n == 1:
            return None
      
        def remove(head):
            
            if head.next == None: 
                if n == 1:
                    return (1, None)
                return (1, head) 
            
            current, tail = remove(head.next) 
            
            if(current + 1 == n):
                return (current + 1, tail)
            else:
                head.next = tail
                return (current + 1, head)
            
            
        _, linkedList = remove(head)
        return linkedList



nodes = ListNode(1)
nodes.next = ListNode(2)

obj = Solution()

val = obj.removeNthFromEnd(nodes, 1)


