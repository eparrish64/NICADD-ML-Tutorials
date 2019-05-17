#!/bin/bash

conda activate mlTutorials;

export PYTHIA8=/xdata/epaarrish/pythia8240;
export PYTHIA_INCLUDE=/xdata/eparrish/pythia8240/include;
export PYTHIA_LIB=/xdata/eparrish/pythia8240/lib;
export LD_LIBRARY_PATH=/xdata/eparrish/pythia8240/lib:$LD_LIBRARY_PATH;
