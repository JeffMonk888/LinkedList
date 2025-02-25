class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        cur  = self.head
        while cur.next!= None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next!= None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!= None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            return "Index out of bounds"
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1
    
    def erase(self, index):
        if index >= self.leng():
            return "Index out of bounds"
        cur_idx = 0
        cur_node = self.head
        while True:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                prev_node.next = cur_node.next
                return
            idx += 1

    

    


my_list  = LinkedList()

my_list.append("a")
my_list.append("b")
my_list.display()
my_list.get(1)
        

