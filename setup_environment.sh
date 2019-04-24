#!/bin/bash

conda activate mlTutorials_gpu;
export PYTHIA8=/xdata/epaarrish/mlhep2018/pythia8240;
export PYTHIA_INCLUDE=/xdata/eparrish/mlhep2018/pythia8240/include;
export PYTHIA_LIB=/xdata/eparrish/mlhep2018/pythia8240/lib;
export LD_LIBRARY_PATH=/xdata/eparrish/mlhep2018/lib:$LD_LIBRARY_PATH;