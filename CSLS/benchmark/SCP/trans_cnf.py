import pandas as pd
import numpy as np
import math
import sys

def requests2params(filename):
    with open(filename, "r") as f:
        params = f.readline()
        params = params.strip('\n')
        params = params.split(' ')
        var_num = int(params[0])
        set_num = int(params[1])
        G = np.zeros((var_num, set_num))
        SAT = []
        #print("var_num: ", var_num)
        #print("set_num: ", set_num)

        cost = f.readline()
        cost = cost.strip('\n')
        cost = cost.split(' ')
        cost = list(map(int, cost))
        cost = np.array(cost)
        #print("cost: ", cost)

        counter = False
        index = 0
        for line in f.readlines():
            if not counter:
                counter = not counter
                continue
            else:
                line = line.strip('\n')
                line = line.split(' ')
                line = list(map(int, line))
                SAT.append([cost[index]] + line + [0])
                for i in range(len(line)):
                    G[index][line[i]-1] = 1
                counter = not counter
                index += 1
        
    h = np.ones(G.shape[0])
    #print(G.shape, cost.shape, h.shape)
    return var_num, set_num, SAT, G, cost, h

# Fix me!!!! Bugs here
def requests2paramsV2(filename):
    with open(filename, "r") as f:
        params = f.readline()
        params = params.strip('\n')
        params = params.split(' ')[1:-1]
        #print(params)
        var_num = int(params[0])
        set_num = int(params[1])
        G = np.zeros((var_num, set_num))
        SAT = []
        #print("var_num: ", var_num)
        #print("set_num: ", set_num)

        cost = f.readline()
        cost = cost.strip('\n')
        cost = cost.split(' ')[1:-1]
        cost = list(map(int, cost))
        cost_lines = math.ceil(set_num/len(cost) - 1)

        for i in range(cost_lines):
            cur_cost = f.readline()
            cur_cost = cur_cost.strip('\n')
            cur_cost = cur_cost.split(' ')[1:-1]
            cur_cost = list(map(int, cur_cost))
            cost = cost + cur_cost
        cost = np.array(cost)
        #print("cost: ", len(cost))

        counter = False
        index = 0
        for line in f.readlines():
            if not counter:
                counter = not counter
                continue
            else:
                line = line.strip('\n')
                line = line.split(' ')[1:-1]
                line = list(map(int, line))
                print(index)
                SAT.append([cost[index]] + line + [0])
                for i in range(len(line)):
                    G[index][line[i]-1] = 1
                counter = not counter
                index += 1
        
    h = np.ones(G.shape[0])
    #print(G.shape, cost.shape, h.shape)
    return var_num, set_num, SAT, G, cost, h

def requests2paramsV3(filename):
    f = open(filename,"r")
    input_string = f.read()
    f.close()
    #input_string = input_string.strip('\n')
    input_string = input_string.replace('\n', ' ')
    input_string = input_string.split(' ')
    output_string = [i for i in input_string if len(i) > 0]
    data_list = list(map(int, output_string))
    print(data_list)
    var_num = data_list.pop(0)
    set_num = data_list.pop(0)
    print("var_num: ", var_num)
    print("set_num: ", set_num)
    G = np.zeros((var_num, set_num))
    h = np.ones(G.shape[0])
    cost = []
    SAT = []

    for i in range(set_num):
        cost.append(data_list.pop(0))

    top = sum(cost) + 1

    for i in range(var_num):
        cover_num = data_list.pop(0)
        cur_cover_list = []
        for j in range(cover_num):
            cur_set = data_list.pop(0)
            cur_cover_list.append(cur_set)
            G[i][cur_set-1] = 1
        SAT.append([top] + cur_cover_list + [0])

    for i in range(set_num):
        SAT.append([cost[i]] + [-i] + [0])

    return var_num, set_num, SAT, G, cost, h, top


def requests2paramsV4(filename):
    f = open(filename,"r")
    input_string = f.read()
    f.close()
    #input_string = input_string.strip('\n')
    input_string = input_string.replace('\n', ' ')
    input_string = input_string.split(' ')
    output_string = [i for i in input_string if len(i) > 0]
    data_list = list(map(int, output_string))
    print(data_list)
    counter = 0
    var_num = data_list[counter]
    counter = 1
    set_num = data_list[counter]
    print("var_num: ", var_num)
    print("set_num: ", set_num)
    G = np.zeros((var_num, set_num))
    h = np.ones(G.shape[0])
    cost = []
    SAT = []

    for i in range(set_num):
        counter += 1
        cost.append(data_list[counter])

    top = sum(cost) + 1

    for i in range(var_num):
        counter += 1
        cover_num = data_list[counter]
        cur_cover_list = []
        for j in range(cover_num):
            counter += 1
            cur_set = data_list[counter]
            cur_cover_list.append(cur_set)
            G[i][cur_set-1] = 1
        SAT.append([top] + cur_cover_list + [0])

    for i in range(set_num):
        SAT.append([cost[i]] + [-i] + [0])

    return var_num, set_num, SAT, G, cost, h, top


filename = str(sys.argv[1])
in_file = filename + '.txt'
#requests2paramsV4(in_file)

var_num, set_num, SAT, G, cost, h, top = requests2paramsV4(in_file)
headline = [['c', filename], ['p', 'wcnf', set_num, set_num + var_num, top]]
data = headline + SAT
with open('SCP/' + filename + '.cnf','w') as f:
    for i in data:
        i = str(i).strip('[').strip(']').replace(',','').replace('\'','')+'\n'
        f.write(i)