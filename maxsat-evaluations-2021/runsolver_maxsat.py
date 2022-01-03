from os import system
import time
import sys
import os
import subprocess
import datetime
from functools import partial
from multiprocessing import Pool
from subprocess import STDOUT, check_output
import subprocess, threading

def RunSeedV3(seed, data_index, solver, dataname):
    runsolver_cmd = "./runsolver -w /dev/null -o" + "results/" + solver + "/" + dataname + "/" + str(data_index) + "_with_seed_" + str(seed) + ".out" + " -C 1000 --timestamp --use-pty "
    if solver == 'loandra':
        command = "./Loandra-2020/bin/loandra_static maxsat-benchmark/" + dataname + "/" + str(data_index)
    elif solver == 'open-wbo':
        command = "./TT-Open-WBO-Inc-21/bin/tt-open-wbo-inc_static maxsat-benchmark/" + dataname + "/" + str(data_index)
    elif solver == 'SATLike':
        command = "./satlike-c/bin/SATLike3.0-c maxsat-benchmark/" + dataname + "/" +str(data_index)
    elif solver == 'open-wbo-g':
        command = "./TT-Open-WBO-Inc-21/bin/open-wbo-g maxsat-benchmark/" + dataname + "/" + str(data_index)
    cmd = runsolver_cmd + command
    os.system(cmd)

if __name__ == '__main__':
    seed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rail = ['rail507.txt.standard.wcnf', 'rail516.txt.standard.wcnf', 'rail582.txt.standard.wcnf', 'rail2536.txt.standard.wcnf', 'rail2586.txt.standard.wcnf', 'rail4284.txt.standard.wcnf', 'rail4872.txt.standard.wcnf']
    scpc = ['scpclr10.wcnf', 'scpclr11.wcnf', 'scpclr12.wcnf', 'scpclr13.wcnf', 'scpcyc06.wcnf', 'scpcyc07.wcnf', 'scpcyc08.wcnf', 'scpcyc09.wcnf', 'scpcyc10.wcnf', 'scpcyc11.wcnf']
    sts = ['sts135.wcnf', 'sts243.wcnf', 'sts405.wcnf', 'sts729.wcnf']
    scp = ['scp41.wcnf', 'scp42.wcnf', 'scp43.wcnf', 'scp44.wcnf', 'scp45.wcnf', 'scp46.wcnf', 'scp47.wcnf', 'scp48.wcnf', 'scp49.wcnf', 'scp51.wcnf', 'scp52.wcnf', 'scp53.wcnf', 'scp54.wcnf', 'scp55.wcnf', 'scp56.wcnf', 
        'scp57.wcnf', 'scp58.wcnf', 'scp59.wcnf', 'scp61.wcnf', 'scp62.wcnf', 'scp63.wcnf', 'scp64.wcnf', 'scp65.wcnf', 'scp410.wcnf', 'scp510.wcnf', 'scpa1.wcnf', 'scpa2.wcnf', 'scpa3.wcnf', 'scpa4.wcnf', 'scpa5.wcnf', 
        'scpb1.wcnf', 'scpb2.wcnf', 'scpb3.wcnf', 'scpb4.wcnf', 'scpb5.wcnf', 'scpc1.wcnf', 'scpc2.wcnf', 'scpc3.wcnf', 'scpc4.wcnf', 'scpc5.wcnf', 'scpd1.wcnf', 'scpd2.wcnf', 'scpd3.wcnf', 'scpd4.wcnf', 'scpd5.wcnf',
        'scpe1.wcnf', 'scpe2.wcnf', 'scpe3.wcnf', 'scpe4.wcnf', 'scpe5.wcnf', 'scpnre1.wcnf', 'scpnre2.wcnf', 'scpnre3.wcnf', 'scpnre4.wcnf', 'scpnre5.wcnf', 'scpnrf1.wcnf', 'scpnrf2.wcnf', 'scpnrf3.wcnf', 'scpnrf4.wcnf', 'scpnrf5.wcnf',
        'scpnrg1.wcnf', 'scpnrg2.wcnf', 'scpnrg3.wcnf', 'scpnrg4.wcnf', 'scpnrg5.wcnf', 'scpnrh1.wcnf', 'scpnrh2.wcnf', 'scpnrh3.wcnf', 'scpnrh4.wcnf', 'scpnrh5.wcnf']

    solver = str(sys.argv[1])
    dataname = str(sys.argv[2])

    if dataname == 'STS':
        dataset = sts
    elif dataname == 'SCPC':
        dataset = scpc
    elif dataname == 'rail':
        dataset = rail
    elif dataname == 'SCP':
        dataset = scp

    for cur_index in dataset:
        partial_RunSeed = partial(RunSeedV3, data_index = cur_index, solver = solver, dataname = dataname)
        with Pool(10) as p:
            print(p.map(partial_RunSeed, seed))