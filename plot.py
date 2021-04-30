# plotting each txt file with four probablity
from matplotlib import pyplot as plt
import numpy as np

def generator(path):
    with open(path, 'r') as f: # the variable name is on the right f
        f_content = f.read().splitlines()

    prob = []
    days = []
    for i in range(len(f_content)):
        if f_content[i] == '':
            day_start = i+1
            break;
        prob.append(int(f_content[i]))
    for j in range(day_start, len(f_content)):
        if f_content[j] != 'inf':
            days.append(int(f_content[j]))
    # print(days)


    # prob.sort(reverse = True)
    # print(days)
    return prob, days


def plot_prob():
    path = 'C:\\Users\wayne\Documents\py_space_new\gs4_p1.txt'
    prob1, days1 = generator(path)


    path = 'C:\\Users\wayne\Documents\py_space_new\gs4_p3.txt'
    prob3, days3 = generator(path)


    path = 'C:\\Users\wayne\Documents\py_space_new\gs4_p5.txt'
    prob5, days5 = generator(path)


    path = 'C:\\Users\wayne\Documents\py_space_new\gs4_p7.txt'
    prob7, days7 = generator(path)


    fig, ax = plt.subplots()
    plt.title('')
    plt.xlabel('Nodes')
    plt.ylabel('Infection Probablity in Percent (%)')
    x_axis = range(1024)

    plt.plot(x_axis, prob1, label='p1')
    plt.plot(x_axis, prob3, label='p3')
    plt.plot(x_axis, prob5, label='p5')
    plt.plot(x_axis, prob7, label='p7')

    plt.tight_layout()
    plt.legend(loc = 'upper right')
    plt.show()

    return None



# def calc_days(days_list):
#     maximum = max(days_list)
#     infect_list = [0]*(maximum+1)
#
#     for node in days_list:
#         infect_list[node] += 1
#
#     return infect_list

def plot_days():
    path = 'C:\\Users\wayne\Documents\py_space_new\gs4_p1.txt'
    prob1, days1 = generator(path)
    # day_infected1 = calc_days(days1)
    # print(days1)
    print(max(days1))

    path = 'C:\\Users\wayne\Documents\py_space_new\gs4_p3.txt'
    prob3, days3 = generator(path)
    print(max(days3))
    # day_infected3 = calc_days(days3)

    path = 'C:\\Users\wayne\Documents\py_space_new\gs4_p5.txt'
    prob5, days5 = generator(path)
    # print(days5)
    print(max(days5))
    # day_infected5 = calc_days(days5)

    path = 'C:\\Users\wayne\Documents\py_space_new\gs4_p7.txt'
    prob7, days7 = generator(path)
    print(max(days7))
    # day_infected7 = calc_days(days7)
    # bins = [0,2.5,5,7.5,10,12.5,15]
    bins = 25
    plt.hist(days5, bins = bins, color='skyblue', edgecolor='black', label='p5')
    plt.hist(days7, bins = bins, color='purple', edgecolor='black', label='p7')
    plt.title('Average Day of Infection')
    plt.xlabel('Day Infected')
    plt.ylabel('Number of Nodes')
    plt.legend(loc = 'upper right')
    plt.show()
    return None

plot_prob()

# plot_days()
