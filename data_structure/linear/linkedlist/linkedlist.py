
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
        return True

    def pop(self):
        if self.head == None:
            print("The list is empty")
            return 
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
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head == None:
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        if self.head == None:
            print("The list is empty")
            return 
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1

        if self.length == 0:
            self.tail = None

        return temp.value

    def get(self,index):
        if index < 0 or index >= self.length:
            return 
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False
    

    def insert(self,index,value):
        if index <0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    def remove(self,index):
        if index < 0 or index>self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after 



        
            
            
            
        











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
    towns_to_visit.pop()
 

    # Get towns
    towns_to_visit.print_list()

    #prepend town
    print("Prepend")
    towns_to_visit.prepend("Kiambu")
    towns_to_visit.print_list()

    
    
    



        
