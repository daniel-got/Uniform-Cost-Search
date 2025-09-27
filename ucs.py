import sys
from queue import PriorityQueue
import csv 

def make_adj_list(filename):
    graph = {}
    try : 
        with open(filename, 'r', newline= '')as file :
            reader = csv.reader(file,delimiter= ';')
            next(reader)

            for row in reader:
                if len(row)==3:
                    start,end,d= row
                    start,end = start.strip(), end.strip()
                    distance =int(d.strip())
                    graph.setdefault(start,[]).append((end,distance))
                    graph.setdefault(end,[]).append((start,distance))

    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return None
    except Exception as e:
        print(f"Terjadi error saat membaca file: {e}")
        return None
        
    return graph



    # file = open(filename, 'r')
    # for line in file :
    #     if'END OF INPUT' in line:
    #         return graph
    #
    #     start,end, d = line.split()
    #     graph.setdefault(start,[]).append((end,d))
    #     graph.setdefault(end,[]).append((start,d))

def ucs(graph,start,end):
    visited_vertex= set()
    path = [] 

    queue = PriorityQueue()
    queue.put((0,[start]))

    while queue:
        if queue.empty():
            print('Tidak ada rute!')
            return

        weight, path = queue.get()
        vertex = path[-1]
        if vertex not in visited_vertex:
            visited_vertex.add(vertex)
            if vertex==end:
                path.append(weight)
                return path

            for neighbor, distance in graph[vertex]:
                if neighbor not in visited_vertex:
                    new_weight = weight + int(distance)
                    temp = path [:]
                    temp.append(neighbor)
                    queue.put((new_weight, temp))
                    
def display_path(path):
    distance = path[-1]
    print('Jarak : '+ str(distance) + ' km')
    print('Rute : ')
    for i in range(len(path)-1):
        print(f"{path[i]}", end=" ")
        if(i != len(path)-2):
            print("->", end=" ")
        else:
            print()

def main():
    source = input("Asal : ")
    destination = input("Tujuan : ")
    print()

    graph = {}
    graph = make_adj_list('data.csv')
    if source not in graph.keys():
        print('Wilayah asal tidak ditemukan')
        sys.exit()  
    if destination not in graph.keys():
        print('Wilayah tujuan tidak ditemukan')
        sys.exit()

    path = []
    path = ucs(graph, source, destination)

    if path:
        display_path(path)

if __name__ == '__main__':
    main()

        
        

