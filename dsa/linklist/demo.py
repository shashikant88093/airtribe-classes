class Node:
    def __init__(self,val,node=None):
        self.val = val
        self.next = node



class ImplementLL:
    

    @staticmethod
    def printLL(head):
        temp = head

        while temp is not None:
            print("linklist",temp.val)
            temp = temp.next



node = ImplementLL.printLL(20)

print(node)
