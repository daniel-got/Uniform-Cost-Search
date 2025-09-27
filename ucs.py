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



def ucs(graph,start,end): 
    visited_vertex= set() #berisi simpul dikunjungi
    path = [] #path menuju simpul

    queue = PriorityQueue() #queue Priority
    queue.put((0,[start])) #simpul awal dan cost 0

    while queue: 
        if queue.empty(): #priority kosong (tidak ada data)
            print('Tidak ada rute!')
            return

        weight, path = queue.get() #ambil simpul ekspan (cabang)
        vertex = path[-1] 
        if vertex not in visited_vertex:
            visited_vertex.add(vertex) #tandai simpul sudah dikunjungi
            if vertex==end: #loop berakhir ketika simpul tujuan ditemukan<D-Space>
                path.append(weight)
                return path
            #jarak ke simpul tetangga (cabang)
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
    #assign tujuan langsung Cilegon ke Banyuwangi karena sesuai soal
    #uncomment line berikut jika ingin memilih asal dan tujuan berbeda
    #source = input("Masukkan asal : ")
    #destination = input("Masukkan tujuan : ")
    source = "Cilegon"
    destination = "Banyuwangi"
    print(source + " Ke " +destination)

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

        
        

