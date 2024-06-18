class Node:
    def __init__(self , value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self,value):
        new_node = Node(value)
        if not self.head:
            self.head=new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next=new_node
            
    def to_number(self):
        num_str=''
        current=self.head
        while current:
            num_str +=str(current.value)
            current=current.next
        return int(num_str)
        
    def from_number(self,number):
        self.head=None
        for char in str(abs(number)):
            self.insert(int(char))
            
    def print_list(self):
        current = self.head
        while current:
            print(current.value,end=' ')
            current = current.next
        print()
        
    def add(self, other):
        result = self.to_number()+other.to_number()
        result_list=LinkedList()
        result_list.from_number(result)
        return result_list
        
    def subtract(self,other):
        result=self.to_number() - other.to_number()
        result_list = LinkedList()
        if result <0:
            print("-",end='')
        result_list.from_number(result)
        return result_list
    
    def multiply(self,other):
        result = self.to_number()*other.to_number()
        result_list = LinkedList()
        result_list.from_number(result)
        return result_list
        
if __name__ == "__main__":
    num1 = LinkedList()
    num1.from_number(9999)
    num2 = LinkedList()
    num2.from_number(1000)
    
    print("Number 1: ",end='')
    num1.print_list()
    print("Number 2:", end='')
    num2.print_list()
    
    result_add =num1.add(num2)
    print("Addition Result: ",end='')
    result_add.print_list()
    
    result_sub =num1.subtract(num2)
    print("Subtraction Result: ",end='')
    if result_sub.to_number() <0:
        print("-", end='')
    result_sub.print_list()
    
    result_mul=num1.multiply(num2)
    print("Multiplication Result: ",end='')
    result_mul.print_list()