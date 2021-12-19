from os import system
import time
import os
import sys
import subprocess
import datetime
from functools import partial
from multiprocessing import Pool
from collections import deque 

seed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dataset_names = ['rail', 'SCPC', 'SCP', 'STS']
rail_scp = ['rail507.txt.standard.txt', 'rail516.txt.standard.txt', 'rail582.txt.standard.txt', 'rail2536.txt.standard.txt', 'rail2586.txt.standard.txt', 'rail4284.txt.standard.txt', 'rail4872.txt.standard.txt']
scpc_scp = ['scpclr10.txt', 'scpclr11.txt', 'scpclr12.txt', 'scpclr13.txt', 'scpcyc06.txt', 'scpcyc07.txt', 'scpcyc08.txt', 'scpcyc09.txt', 'scpcyc10.txt', 'scpcyc11.txt']
sts_scp = ['sts135.txt', 'sts243.txt', 'sts405.txt', 'sts729.txt']
scp_scp = ['scp41.txt', 'scp42.txt', 'scp43.txt', 'scp44.txt', 'scp45.txt', 'scp46.txt', 'scp47.txt', 'scp48.txt', 'scp49.txt', 'scp51.txt', 'scp52.txt', 'scp53.txt', 'scp54.txt', 'scp55.txt', 'scp56.txt', 
            'scp57.txt', 'scp58.txt', 'scp59.txt', 'scp61.txt', 'scp62.txt', 'scp63.txt', 'scp64.txt', 'scp65.txt', 'scp410.txt', 'scp510.txt', 'scpa1.txt', 'scpa2.txt', 'scpa3.txt', 'scpa4.txt', 'scpa5.txt', 
            'scpb1.txt', 'scpb2.txt', 'scpb3.txt', 'scpb4.txt', 'scpb5.txt', 'scpc1.txt', 'scpc2.txt', 'scpc3.txt', 'scpc4.txt', 'scpc5.txt', 'scpd1.txt', 'scpd2.txt', 'scpd3.txt', 'scpd4.txt', 'scpd5.txt',
            'scpe1.txt', 'scpe2.txt', 'scpe3.txt', 'scpe4.txt', 'scpe5.txt', 'scpnre1.txt', 'scpnre2.txt', 'scpnre3.txt', 'scpnre4.txt', 'scpnre5.txt', 'scpnrf1.txt', 'scpnrf2.txt', 'scpnrf3.txt', 'scpnrf4.txt', 'scpnrf5.txt',
            'scpnrg1.txt', 'scpnrg2.txt', 'scpnrg3.txt', 'scpnrg4.txt', 'scpnrg5.txt', 'scpnrh1.txt', 'scpnrh2.txt', 'scpnrh3.txt', 'scpnrh4.txt', 'scpnrh5.txt']

def RunSeed(seed, data_index, dataset_name, w1, w2, w3):
    command = "./CSLS/CSLS " + dataset_name + '/' + str(data_index) + " 1000 " + str(seed) + " " + str(w1) + " " + str(w2) + " " + str(w3) + " > CSLS_results/" + dataset_name + '/' + str(data_index) + "_with_seed_" + str(seed) + '.out'
    os.system(command)

if __name__ == '__main__':

    dataset_name = str(sys.argv[1])

    if dataset_name == 'rail':
        x1 = 4
        x2 = 35
        x3 = 0.22270177087309927
    elif dataset_name == 'STS':
        x1 = 75
        x2 = 4
        x3 = 0.06961626680064559
    elif dataset_name == 'SCPC' or dataset_name == 'SCP':
        x1 = 92
        x2 = 7
        x3 = 0.40209043209858153

    if dataset_name == 'rail':
        dataset = rail_scp
    elif dataset_name == 'SCP':
        dataset = scp_scp
    elif dataset_name == 'SCPC':
        dataset = scpc_scp
    elif dataset_name == 'STS':
        dataset = sts_scp

    for cur_index in dataset:
        partial_RunSeed = partial(RunSeed, data_index = cur_index, dataset_name = dataset_name, w1 = x1, w2 = x2, w3 = x3)
        with Pool(10) as p:
            p.map(partial_RunSeed, seed)