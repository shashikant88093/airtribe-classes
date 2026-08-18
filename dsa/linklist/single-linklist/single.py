class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    
def print_all(head):
    temp = head

    while temp is not None:
        print(temp.value)
        temp = temp.next
    print("None")



list_all = Node(10)
list_all.next = Node(20)
list_all.next.next = Node(30)

print_all(list_all)