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
            # programa pritaikyta nekryptiniams grafams (t.y. kiekvienai briaunai abi viršūnes viena kitai pridedamos prie kaimyninių viršūnių sąrašo)
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def hamiltonianPaths(graph, v, visited, path, n, list_of_paths):
    # jeigu rastas Hamiltono kelias tai jo viršūnių pavadinimai atkoduojami
    if len(path) == n:
        path_values = path.copy()
        path_values = [inverted_dict[i] for i in path_values]
        list_of_paths.append(path_values)
        return None

    for w in graph.adjList[v]:
        if not visited[w]:
            visited[w] = True
            path.append(w)
            hamiltonianPaths(graph, w, visited, path, n, list_of_paths)
            visited[w] = False
            path.pop()


def findHamiltonianPaths(graph, n, data):
    list_of_paths = [] # sąrašas saugoti rastiems Hamiltono keliams
    for start in data:
        path = [start]
        visited = [False] * n
        visited[start] = True
        hamiltonianPaths(graph, start, visited, path, n, list_of_paths)

    return list_of_paths

# Failo su duomenimis pavadinimas paduodamas paleidžiant programą iš komandinės eilutės
# Duomenys nuskaitomi tik proceso su rank == 0
# Užkoduosiu viršūnių pavadinimus nuo 0 iki n-1 taip siekdamas, kad nepriklausomai nuo tikrųjų viršūnių pavadinimų
    # kiekvienos viršūnes užkoduotas pavadinimas atitiktų jos indeksą sąraše
if rank == 0:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        edges = []
        values_dict = {}
        for row in reader:
            values = [int(i) for i in row]
            if values[0] not in values_dict.keys():
                values_dict[values[0]] = len(values_dict)
            if values[1] not in values_dict.keys():
                values_dict[values[1]] = len(values_dict)
            edges.append((values_dict[values[0]],values_dict[values[1]]))
            
    data = list(set([i for j in edges for i in j]))
    inverted_dict = {y:x for x,y in values_dict.items()} # sąrašas, skirtas atkoduoti atgal viršūnių pavadinimus
    n = max(data) + 1
    graph = Graph(edges, n) # sukuriamas grafo objektas

else:
    graph = None
    n = None
    inverted_dict = None


# grafas ir jo dydis perduodamas kitiems procesams
graph = comm.bcast(graph, root=0)
n = comm.bcast(n, root=0)
inverted_dict = comm.bcast(inverted_dict,root=0)


def split_data(data):
    # sukuriamas sąrašas, kurio elementai yra šąrašas viršūnių, pradėdamas nuo kurių kiekvienas procesas ieškos Hamiltono kelių
    n_items = int(len(data)/size)
    return_list = []
    for i in range(0, size-1):
        return_list.append(data[i*n_items:(i+1)*n_items])
    return_list.append(data[(size-1)*n_items:])
    return return_list


# surandamos unikalios viršūnės ir paruošiamos padalijimui
if rank == 0:
    data = split_data(data)
else:
    data = None


# Pradinės viršūnės padalijamos procesams
data = comm.scatter(data, root=0)

# kiekvienas procesas suranda Hamiltono kelius prasidedančius nuo
# pradinių viršūnių, kurias jis gavo
results_list = findHamiltonianPaths(graph, n, data)

# visų procesų gauti rezultatai surenkami į rank==0 procesą
results_list_full = comm.gather(results_list, root=0)


# procesas rank==0 bendrus rezultatus išveda į failą
if rank == 0:
    # visus gautus kelius išvesiu vienu kartu
    res = ""
    if max(results_list_full) != []: # jeigu yra netučių sąrašų
        for i in results_list_full: 
            if len(i) > 0: # jeigu tam tikras sąrašas nėra tuščias
                for j in i: # kiekvienam Hamiltono keliui tam tikrame sąraše
                    res = res+str(j)+"\n"
    else:
        res = "Hamiltono keliu grafe nera\n"
    print(res)
   
MPI.Finalize()
