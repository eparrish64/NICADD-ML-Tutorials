#!/bin/bash

## Author: Elliot Parrish
## Date:4/24/2019

cd /xdata/$USER;
echo "Downloading and installing Anaconda installation script, this will take some time";
echo "When asked, accept the user agreement";
echo "Be sure to change install location to /xdata/USERNAME/anaconda3";
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh &&
bash Miniconda3-latest-Linux-x86_65.sh && 
source ~/.bashrc &&
conda config --set auto_activate_base false;
cd -;
conda env create -f mlTutorials_gpu.yml &&

conda activate mlTutorials_gpu &&

pip install cython pydot &&
# source setup_environment.sh;
export PYTHIA8=/xdata/epaarrish/pythia8240 &&
export PYTHIA_INCLUDE=/xdata/eparrish/pythia8240/include &&
export PYTHIA_LIB=/xdata/eparrish/pythia8240/lib &&
export LD_LIBRARY_PATH=/xdata/eparrish/pythia8240/lib:$LD_LIBRARY_PATH &&
pip install git+https://github.com/maxim-borisyak/pythia-mill.git@master

# jupyter notebook --no-browser --port=NUMBER
# ssh -L localhost:PORT:localhost:PORT USERNAME@cms1.nicadd.niu.edu
