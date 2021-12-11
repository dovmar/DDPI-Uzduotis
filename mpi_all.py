from mpi4py import MPI
import csv
import sys

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for i in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 

 
    
def hamiltonianPaths(graph, v, visited, path, n):
    if len(path) == n:
        return path
 
    for w in graph.adjList[v]:
        if not visited[w]:
            visited[w] = True
            path.append(w)
            res = hamiltonianPaths(graph, w, visited, path, n)
          
            if res is not None:
                return res
            
            visited[w] = False
            path.pop()
 
    

    
def findHamiltonianPaths(graph, n,data):
    res_list = []
    
    for start in data:         
        path = [start]
        visited = [False] * n
        visited[start] = True
        res =  hamiltonianPaths(graph, start, visited, path, n)
        if res is not None:
            res_list.append(res)

    return res_list



if rank==0:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        edges = []
        for row in reader:
            edges.append(tuple([int(i)-1 for i in row]))

    
    n = max([max(i) for i in edges]) + 1
    graph = Graph(edges, n)
    
else:
    graph = None
    n = None
    

graph = comm.bcast(graph, root=0)
n = comm.bcast(n, root=0)
    

def split_data(data):
    n_items = int(len(data)/size)
    ret_list = []
    for i in range(0,size-1):
        ret_list.append(data[i*n_items:(i+1)*n_items])
    ret_list.append(data[(size-1)*n_items:])
    return ret_list
    
if rank == 0:
     data = list(set([i for j in edges for i in j]))
     data = split_data(data)
else:
     data = None



data = comm.scatter(data, root=0)

res_list = findHamiltonianPaths(graph, n,data)

res_list_full = comm.gather(res_list,root=0)
    

if rank == 0:
    with open("res_full","w") as file:
        for i in res_list_full:
            if len(i) > 0:
                for j in i:
                    file.write(str(j)+"\n")
                
                