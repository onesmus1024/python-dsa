
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def  print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append(self,value):

        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            self.length +=1

    def pop(self):
        if self.head == None:
            print("The list is empty")
        previous = self.head
        temp = self.head

        while temp.next is not None:
            previous = temp
            temp = temp.next
        self.tail = previous
        self.tail.next = None
        self.length -=1

        if self.length == 0:
            self.head = None
            self.tail = None
        


            return temp.value











if __name__ == '__main__':

    towns_to_visit = LinkedList("Nyeri")
    print("New List")
    towns_to_visit.print_list()

    # Add a new town
    print("Add New Node")
    towns_to_visit.append("Nanyuki")

    # Get All Towns

    towns_to_visit.print_list()

    #Remove the last town
    print("Remove One Node")
    towns_to_visit.pop()
    towns_to_visit.pop()

    # Get towns
    towns_to_visit.print_list()
    
    



        
