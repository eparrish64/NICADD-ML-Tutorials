## Author: Elliot Parrish
## Date:4/24/2019

cd /xdata/$USER;
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh;
bash Anaconda3-2019.03-Linux-x86_64.sh;
cd /xdata/$USER/NICADD-ML-Tutorials;
conda create env create -f mlTutorials_gpu.yml;

export PYTHIA8=/xdata/epaarrish/mlhep2018/pythia8240;
export PYTHIA_INCLUDE=/xdata/eparrish/mlhep2018/pythia8240/include;
export PYTHIA_LIB=/xdata/eparrish/mlhep2018/pythia8240/lib;
export LD_LIBRARY_PATH=/xdata/eparrish/mlhep2018/lib:$LD_LIBRARY_PATH;