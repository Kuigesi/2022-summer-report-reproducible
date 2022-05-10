# Reproducible Experiment

To reproduce the evaluation presented in the 2022 summer semester report paper:

First, login to the cuda server `bigdata2.cs.purdue.edu`, make sure you have access to this server

```bash
ssh username@bigdata2.cs.purdue.edu
```
Then, source the environment script

```bash
source /scratch1/gao606/env.sh
```
Then, clone the code from github, and enter the repo directory

```bash
git clone https://github.com/Kuigesi/2022-summer-report-reproducible.git
cd 2022-summer-report-reproducible
```

Run
```bash
bash ./runtest.sh
```
This will produce the following files:
- `./table.pdf`, which is the table of the path number and running time of KLEE/POSIX, GenSym/POSIX and GenSym/FS for different number of symbolic inputs.


- `./figure.pdf`, which is the figure plot of the running time of KLEE/POSIX, GenSym/POSIX and GenSym/FS for different number of symbolic inputs.

To check out the generated figures, the pdf file should be transfered to your local computer.