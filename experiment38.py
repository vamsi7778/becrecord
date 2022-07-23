class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self,head):
        self.head=head
    def insertbegin(self,node):
        node.next=self.head
        self.head=node
        print(node.data,"inserted successfully in begining")
    def insertpos(self,node,pos):
        if pos==1:
            node.next=self.head.next
            self.head=node
        else:
            prev=self.head
            for i in range(1,pos-1):
                prev=prev.next
            node.next=prev.next
            prev.next=node
            print(node.data,"inserted successfully at %d positon"%pos)
    def insetend(self,node):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=node
        print(node.data,'inserted succcessfully at end')
    def display(self):
        temp=self.head
        if temp.data is None:
            print("list is empty")
        else:
            while temp.next is not None:
                print(temp.data,"-->",end=" ")
                temp=temp.next
            print(temp.data)
n1=node(20)
l1=linkedlist(n1)
l1.insertbegin(node(10))
l1.insetend(node(30))            
l1.insetend(node(40))            
l1.display()
l1.insertpos(node(22),1)
l1.display()            
l1.insertpos(node(21),3)
l1.display()            