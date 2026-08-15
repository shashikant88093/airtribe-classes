class Node:
    def __init__(self,val,next_node=None):
        self.val=val
        self.next=next_node



class ImplementLL:
     head = None
     

     @staticmethod
     def addFront(num):
         node = Node(num)
         node.next = ImplementLL.head
         ImplementLL.head = node
    
     @staticmethod
     def addLast(num):
         node = Node(num)
         temp = ImplementLL.head

         while temp is not None:
             temp = node
              
      
         
     
     @staticmethod
     def sizeLL(head):
         temp = head
         c=0
         while temp is not None:
             c+=1
             temp = temp.next
         return c
             
     
     @staticmethod
     def printLL(head):
         temp = head
         while temp is not None:
             print(temp.val)
             head = temp.next
        