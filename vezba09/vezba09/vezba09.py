import sys
from enum import Enum	
import math

global time
global h

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d1 = None, d2 = None, l = None, i = None, f = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.color = c
        self.p = p
        self.d1 = d1
        self.d2 = d2
        self.l = list()
        self.i = i
        self.f = f

class Data:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255	

def print_vertex(vertex_list):        
    for k in vertex_list:
        print("*", k.i)
        for n in k.l:
            print("---> ", n.i)

def breadth_first_search(G,s):
    for u in G:
        u.color = VertexColor.WHITE
        u.d2 = math.inf
        u.p = None
    s.color = VertexColor.GRAY
    s.d2 = 0
    s.p = None
    Q = list()
    Q.append(s)
    while len(Q) is not 0:
        u = Q.pop(0)
        for v in u.l:
            if v.color == VertexColor.WHITE:
                v.color = VertexColor.GRAY
                v.d2 = u.d2 + 1
                v.p = u
                Q.append(v)
        u.color = VertexColor.BLACK

def print_parth(G,s,v):
    if v == s:
        print(s.i)
    elif v.p == None:
        print("No path from", s, "to", v, "exists")
    else:
        print_parth(G,s,v.p)
        print(v.i, v.d2)	
        
def depth_first_search(G):
    global time
    for u in G:
        u.color = VertexColor.WHITE
        u.p = None
    time = 0
    for u in G:
        if u.color == VertexColor.WHITE:
            dfs_visit(G,u)
    
def dfs_visit(G,u):
    global h
    global time
    
    time = time + 1
    u.d2 = time
    u.color = VertexColor.GRAY
    for v in u.l:
        if v.color == VertexColor.WHITE:
            v.p = u 
            dfs_visit(G,v)

    u.color = VertexColor.BLACK
    time = time + 1
    u.f = time
    h.append(u)                                 # for topological sort
     
if __name__ == "__main__":
    #u = Vertex(c=VertexColor.WHITE, d1=1, d2=22)
    #v = Vertex(c=VertexColor.GRAY, p=u, d1=33, d2=4)

    vertex_list_bfs = list()
    vertex_list_dfs = list()        

    A = Vertex()
    A.i = 'A'
    B = Vertex()
    B.i = 'B'
    C = Vertex()
    C.i = 'C'
    D = Vertex()
    D.i = 'D'
    E = Vertex()
    E.i = 'E'
    F = Vertex()
    F.i = 'F'
    G = Vertex()
    G.i = 'G'
    H = Vertex()
    H.i = 'H'

    print("\n----------------------------BFS:\n")
    # for BFS
    A.l.append(B)
    A.l.append(E)
    vertex_list_bfs.append(A)

    B.l.append(A)
    B.l.append(F)
    vertex_list_bfs.append(B)

    C.l.append(F)
    C.l.append(G)
    C.l.append(D)
    vertex_list_bfs.append(C)

    D.l.append(C)
    D.l.append(G)
    D.l.append(H)
    vertex_list_bfs.append(D)

    E.l.append(A)
    vertex_list_bfs.append(E)

    F.l.append(B)
    F.l.append(C)
    F.l.append(G)
    vertex_list_bfs.append(F)

    G.l.append(F)
    G.l.append(C)
    G.l.append(D)
    G.l.append(H)
    vertex_list_bfs.append(G)

    H.l.append(D)
    H.l.append(G)
    vertex_list_bfs.append(H)
    
    print_vertex(vertex_list_bfs)
    breadth_first_search(vertex_list_bfs, B)
    print_parth(vertex_list_bfs, B, H)


    A = Vertex()
    A.i = 'A'
    B = Vertex()
    B.i = 'B'
    C = Vertex()
    C.i = 'C'
    D = Vertex()
    D.i = 'D'
    E = Vertex()
    E.i = 'E'
    F = Vertex()
    F.i = 'F'
    G = Vertex()
    G.i = 'G'
    H = Vertex()
    H.i = 'H'

    print("\n----------------------------DFS:\n")
    # for DFS
    A.l.append(B)
    A.l.append(C)
    vertex_list_dfs.append(A)

    B.l.append(D)
    vertex_list_dfs.append(B)

    C.l.append(B)
    vertex_list_dfs.append(C)

    D.l.append(C)
    vertex_list_dfs.append(D)

    E.l.append(D)
    E.l.append(F)
    vertex_list_dfs.append(E)

    F.l.append(F)
    vertex_list_dfs.append(F)

    global h    
    h = list()
    print_vertex(vertex_list_dfs)
    print("\n")
    depth_first_search(vertex_list_dfs)
    h = h[::-1]
    for i in h:
        print(i.i, "-->", i.d2, i.f)
    