#!/bin/bash

## Author: Elliot Parrish
## Date:4/24/2019

cd /xdata/$USER;
echo "Downloading Anaconda installation script";
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh;
echo "Installing Anaconda, be patient, this will take some time";
echo "When asked, accept the user agreement";
echo "Be sure to change install location to /xdata/USERNAME/anaconda3";
bash Anaconda3-2019.03-Linux-x86_64.sh;
source ~/.bashrc;
conda config --set auto_activate_base false;
# source ~/.bashrc;
cd /xdata/$USER/NICADD-ML-Tutorials;
conda env create -f mlTutorials_gpu.yml;
conda activate mlTutorials_gpu;

pip install cython pydot;
# source setup_environment.sh;
export PYTHIA8=/xdata/epaarrish/mlhep2018/pythia8240;
export PYTHIA_INCLUDE=/xdata/eparrish/mlhep2018/pythia8240/include;
export PYTHIA_LIB=/xdata/eparrish/mlhep2018/pythia8240/lib;
export LD_LIBRARY_PATH=/xdata/eparrish/mlhep2018/lib:$LD_LIBRARY_PATH;
pip install git+https://github.com/maxim-borisyak/pythia-mill.git@master

# ssh -L localhost:1999:localhost:1999 eparrish@cms1.nicadd.niu.edu