class Node:
    def __init__(self,val,next_node =None):
        self.val = val
        self.next_node = next_node
        


class implentedLL:


    staticmethod
    def reverList(head):
        curr = head
        prev = None

        while curr is not None:
            future = curr.next
            curr.next =prev
            prev = curr
            curr = future