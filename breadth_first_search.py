import sys
from queue import Queue


def readGraph(input_file):
    with open(input_file, 'r') as f:
        raw = [line.split(',') for line in f.read().splitlines()]

    N = int(raw[0][0])
    s = int(raw[1][0])
    adj_list = []
    for line in raw[2:]:
        if line == ['-']:
            adj_list.append([])
        else:
            adj_list.append([int(index) for index in line])
    return N, s, adj_list

def writeOutput(output_file, level):
    with open(output_file, 'w') as f:
        for i in level:
            f.write(str(i) + '\n')



def Run(input_file, output_file):
    N, s, adj_list = readGraph(input_file)
    level =   BFS(N, s, adj_list)
    writeOutput(output_file, level)



def  BFS(N, s, adj_list):

    level = ['x']*N

    discovered = [False]*N # initialize a boolean array
    Q = Queue(maxsize = N) # initliaze a Queue

    # single source case
    if type(s) == list:
        for source in s:
            level[source] = 0
            discovered[source] = True
            Q.put(source)
    else:
        level[s] = 0
        discovered[s] = True
        Q.put(s)


    # BFS
    while not Q.empty():
        node = Q.get()
        for neighbor in adj_list[node]:
            if discovered[neighbor] == False:
                discovered[neighbor] = True
                Q.put(neighbor)
                level[neighbor] = level[node] + 1

    return level





def main(args=[]):
    Run('input', 'output')


if __name__ == "__main__":
    main(sys.argv[1:])
