import sys
import random
from queue import Queue
import random
from matplotlib import pyplot as plt


def readGraph(input_file):
    with open(input_file, 'r') as f:
        raw = [line.split(',') for line in f.read().splitlines()]

    N = int(raw[0][0])
    sin = raw[1]
    s = []
    for st in sin:
        s.append(int(st))
    adj_list = []
    for line in raw[2:]:
        if line == ['-']:
            adj_list.append([])
        else:
            adj_list.append([int(index) for index in line])
    return N, s, adj_list

def writeOutput(output_file, prob_infect, avg_day):
    with open(output_file, 'w') as f:
        for i in prob_infect:
            f.write(str(i) + '\n')
        f.write('\n')
        for i in avg_day:
            f.write(str(i) + '\n')



def Run(input_file, output_file):
    N, s, adj_list = readGraph(input_file)
    prob_infect, avg_day =  model_outbreak(N, s, adj_list)
    writeOutput(output_file, prob_infect, avg_day)


def BFS(N, s, adj_list):
    level = ['x']*N


    # intialization
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



def model_outbreak(N, s, adj_list):

    prob_infect = [0]*N
    # the probability that each node gets infected after a run of the experiment
    avg_day = ['inf']*N
    # the average day of infection for each node
    # (you can write 'inf' for infinity if the node is never infected)
    # The code will write this information to a single text file.
    # If you do not name this file at the command prompt, it will be called 'outbreak_output.txt'.
    # The first N lines of the file will have the probability infected for each node.
    # Then there will be a single space.
    # Then the following N lines will have the avg_day_infected for each node.

    # first check if s is singular or multiple
    infection_counter = [0]*N

    p = 0.1 # infection probablity. Change this for different experiments
    for i in range(100):
        new_adj_list = gen_infect_graph(N,s,adj_list,p)
        level = BFS(N,s,new_adj_list)
        # print(level)
        for i in range(len(level)):
            infect_day = level[i]
            if infect_day != 'x':
                prob_infect[i] += 1
                if avg_day[i] == 'inf':
                    avg_day[i] = infect_day
                else:
                    avg_day[i] += infect_day
                infection_counter[i] += 1

    # print(avg_day)
    # print(infection_counter)
    for i in range(len(avg_day)):
        if avg_day[i] != 'inf':
            avg_day[i] = avg_day[i]//infection_counter[i]


    # prob and day for s is always 100% and 0 day
    if type(s) == list:
        for source in s:
            avg_day[source] = 0
            prob_infect[source] = 100
    else:
        avg_day[s] = 0
        prob_infect[s] = 1

    # prob_infect.sort(reverse=True)
    print(level)
    print(prob_infect)

    return prob_infect, avg_day


def gen_infect_graph(N, s, adj_list,p):
    dict = {}

    # initalizing a new Gi
    new_adj_list = []
    for i in range(N):
        row = []
        new_adj_list.append(row)

    # associating edges with a probablity as dict--(node, neighbor): p

    for i in range(len(adj_list)):
        for node in adj_list[i]:
            edge = (i, node)
            dict[edge] = p

    # random infect prob generator
    for k,v in dict.items():
        active = random.random()
        if active <= v:
            dict[k] = active
            new_adj_list[k[0]].append(k[1]) # only keep the ones infected

    # if s is a list (multiple sources)
    if type(s) == list:
        for source in range(len(s)):
            edge = ('x', source)
            dict[edge] = 1

    return new_adj_list


# N = 8
# s = [1,6]
# adj_list = [[1,2], [0,2,3,4], [0,1,4,6,7], [1,4], [1,2,3,5], [4], [2,7], [2,6]]
# # print(BFS(N,s,adj_list))
# print(gen_infect_graph(N,s,adj_list,p=0.1))
# prob, days = model_outbreak(N,s,adj_list)
# print(model_outbreak(N,s,adj_list))
# print(sorted(prob))




############################

# DO NOT CHANGE THIS PART!!

############################


# read command line arguments and then run

def main(args=[]):
    filenames = []

    #graph file
    if len(args)>0:
        filenames.append(args[0])
        input_file = filenames[0]
    else:
        print()
        print('ERROR: Please enter file names on the command line:')
        print('>> python outbreak.py graph_file.txt output_file.txt')
        print()
        return

    # output file
    if len(args)>1:
        filenames.append(args[1])
    else:
        filenames.append('outbreak_output.txt')
    output_file = filenames[1]

    Run(input_file, output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
