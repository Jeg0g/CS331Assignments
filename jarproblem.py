class Queue:

    class Node:

        def __init__(self,d=None,n=None):
            self.data=d
            self.next=n

    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def enqueue(self, item):
        if self.length==0:
            self.tail=self.head=Queue.Node(item)
        else:
            self.tail.next=Queue.Node(item)
            self.tail=self.tail.next
        self.length+=1

    def dequeue(self):
        assert self.length!=0
        val=self.head.data
        self.head=self.head.next
        self.length-=1
        return val

class SinglyLinkedList:
    class Node:

        def __init__(self,d=None,n=None):
            self.data=d
            self.next=n
        
    def __init__(self):
        self.tail=self.head=None
        self.length=0

    def __contains__(self, item):
        ptr=self.head
        for i in range(self.length):
            if ptr.data==item:
                return True
        return False

    def append(self, item):
        if self.length==0:
            self.tail=self.head=SinglyLinkedList.Node(item)
        else:
            self.tail.next=SinglyLinkedList.Node(item)
            self.tail=self.tail.next
        self.length+=1

    def __repr__(self):
        if self.length==0:
            return "[]"
        str="["
        ptr=self.head
        for i in range(self.length-1):
            str+=ptr.data+","
            ptr=ptr.next
        str+=ptr.data+"]"
        return str

class Graph:
    
    def __init__(self):
        self.edges={}

    def addVertex(self, vertex):
        if not vertex in self.edges:
            self.edges[vertex]=SinglyLinkedList()

    def addEdge(self, v1, v2):
        assert v1 in self.edges
        if not v2 in self.edges[v1]:
            self.edges[v1].append(v2)

def jars(one,two,three,target):
    g=Graph()
    g.addVertex((0,0,0))
    for i in range(9):
        g.addVertex()