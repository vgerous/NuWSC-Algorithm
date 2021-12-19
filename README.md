# CSLS
- Paper name


## 1. Set up
####1. Set a conda virtual environment
```bash
conda create -n CSLS python=3.7 anaconda --yes
```

####2. Clone the repository
```bash
git clone https://github.com/vgerous/CSLS-Algorithm.git
```

####3. Install required packages
```bash
conda activate CSLS
conda install --file requirements.txt
```


## 2. Run Competitors
####1. Max-SAT solvers
All Max-SAT solvers can be run in the file **maxsat-evaluations-2021/runsolver_maxsat.py**

##### Example (Run loandra on rail benchmark)
```bash
python maxsat-evaluations-2021/runsolver_maxsat.py loandra rail
```

####1. SCP solvers
All SCP solvers can be run in the file **set-cover-competitors/runsolver_scp.py**

##### Example (Run domsat on rail benchmark)
```bash
python set-cover-competitors/runsolver_scp.py domsat rail
```

## 2. Run CSLS

CSLS algorithm can be run in the file **CSLS/run_mysolver.py**

##### Example (Run CSLS on rail benchmark)
```bash
python CSLS/run_mysolver.py rail
```
