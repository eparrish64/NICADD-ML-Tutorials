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

pip install cython;
source setup_environment.sh;
pip install git+https://github.com/maxim-borisyak/pythia-mill.git@master