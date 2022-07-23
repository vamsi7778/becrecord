class queue:
    def __init__(self,max):
        self.q=list()
        self.max=max
    def enque(self,ele):
        if(len(self.q)>=self.max):
            print("queue is full")
        else:
            self.q.append(ele)
            print(f"\n{ele} inserted successfully")
    def deque(self):
        if(len(self.q)<=0):
            print("no element to delete in queue")
        else:
            ele=self.q.pop(0)
            print(f"\n{ele} deleted successfully")
    def display(self):
        if(len(self.q)<=0):
            print("no element to delete in queue")
        else:
            for i in self.q:
                print(i,end=" ")
q1=queue(5)
q1.display()
q1.enque(56)
q1.display()
q1.enque("dairy fun")
q1.display()
q1.enque(18.9)
q1.enque('v')
q1.enque('vamsi')
q1.enque('vizag')
q1.enque('bapatla')
q1.display()
