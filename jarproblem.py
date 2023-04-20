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
        if self.length==0:
            self.tail=None
        return val
    
    def __len__(self):
        return self.length

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
        strr="["
        ptr=self.head
        for i in range(self.length-1):
            strr+=str(ptr.data)+","
            ptr=ptr.next
        strr+=str(ptr.data)+"]"
        return strr

class Vertex:

    def __init__(self):
        self.edgelist=SinglyLinkedList()
        #color, 0=White, 1=Grey, 2=Black
        self.color=0
        self.d=999999999999999999999999
        self.pi=None

    def __iter__(self):
        ptr=self.edgelist.head
        while ptr!=None:
            yield ptr.data
            ptr=ptr.next

    def append(self,item):
        self.edgelist.append(item)

    def __repr__(self):
        return repr(self.edgelist)

class Graph:
    
    def __init__(self):
        self.edges={}

    def addVertex(self, vertex):
        if not vertex in self.edges:
            self.edges[vertex]=Vertex()

    def addEdge(self, v1, v2):
        assert v1 in self.edges
        if not v2 in self.edges[v1]:
            self.edges[v1].append(v2)

    def __contains__(self, item):
        return item in self.edges
    
    def __repr__(self):
        return repr(self.edges)
    
    def __getitem__(self,item):
        return self.edges[item]

def addAllVerticies(one,two,three,starting,g):
    if starting in g:
        return
    g.addVertex(starting)

    addAllVerticies(one,two,three,(one,starting[1],starting[2]),g)
    g.addEdge(starting,(one,starting[1],starting[2]))
    addAllVerticies(one,two,three,(starting[0],two,starting[2]),g)
    g.addEdge(starting,(starting[0],two,starting[2]))
    addAllVerticies(one,two,three,(starting[0],starting[1],three),g)
    g.addEdge(starting,(starting[0],starting[1],three))

    addAllVerticies(one,two,three,(0,starting[1],starting[2]),g)
    g.addEdge(starting,(0,starting[1],starting[2]))
    addAllVerticies(one,two,three,(starting[0],0,starting[2]),g)
    g.addEdge(starting,(starting[0],0,starting[2]))
    addAllVerticies(one,two,three,(starting[0],starting[1],0),g)
    g.addEdge(starting,(starting[0],starting[1],0))
    # addAllVerticies(one,two,three,(starting[0],starting[1],starting[2]),g)
    # g.addEdge(starting,(starting[0],starting[1],starting[2]))
    
    vols=fill(starting[0],starting[1],two)
    addAllVerticies(one,two,three,(vols[0],vols[1],starting[2]),g)
    g.addEdge(starting,(vols[0],vols[1],starting[2]))
    vols=fill(starting[0],starting[2],three)
    addAllVerticies(one,two,three,(vols[0],starting[1],vols[1]),g)
    g.addEdge(starting,(vols[0],starting[1],vols[1]))

    vols=fill(starting[1],starting[2],three)
    addAllVerticies(one,two,three,(starting[0],vols[0],vols[1]),g)
    g.addEdge(starting,(starting[0],vols[0],vols[1]))
    vols=fill(starting[1],starting[0],one)
    addAllVerticies(one,two,three,(vols[1],vols[0],starting[2]),g)
    g.addEdge(starting,(vols[1],vols[0],starting[2]))

    vols=fill(starting[2],starting[0],one)
    addAllVerticies(one,two,three,(vols[1],starting[1],vols[0]),g)
    g.addEdge(starting,(vols[1],starting[1],vols[0]))
    vols=fill(starting[2],starting[1],two)
    addAllVerticies(one,two,three,(starting[0],vols[1],vols[0]),g)
    g.addEdge(starting,(starting[0],vols[1],vols[0]))

def fill(c1,c2,vol):
    if c1+c2<=vol:
        c2+=c1
        c1=0
    else:
        diff=vol-c2
        c2=vol
        c1-=diff
    return (c1,c2)

def BFS(g,s,target):
    found=None
    breakVar=False
    g[s].color=1
    g[s].d=0
    q=Queue()
    q.enqueue(s)
    count=0
    while len(q)>0:
        u=q.dequeue()
        for v in g[u]:
            if g[v].color==0:
                g[v].color=1
                g[v].d=g[u].d+1
                g[v].pi=u
                if v[0]==target or v[1]==target or v[2]==target:
                    found=v
                    breakVar=True
                    break
                q.enqueue(v)
        if breakVar:
            break
        g[u].color=2
        count+=1
    if found==None:
        return "No Solutions"
    path=[None]*(g[found].d+1)
    i=g[found].d
    while found!=None:
        path[i]=found
        found=g[found].pi
        i-=1
    return path

def jars(one,two,three):
    g=Graph()
    addAllVerticies(one,two,three,(0,0,0),g)
    return g

jarss=[None]*3
for i in range(3):
    jarss[i]=input(f"Please enter the size of jar {i+1}: ")
target=input("Please enter target: ")
def solve(one, two, three, target):
    if target>one and target>two and target>three:
        return "No Solutions"
    else:
        return BFS(jars(one,two,three),(0,0,0),target)
print(solve(int(jarss[0]),int(jarss[1]),int(jarss[2]),int(target)))
