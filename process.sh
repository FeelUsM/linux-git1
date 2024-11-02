#! /bin/bash

#wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh  > /dev/null 2>&1
#echo wget:$?

#sh Miniforge3-Linux-x86_64.sh -b -p $(pwd)/miniforge3  > /dev/null 2>&1
#echo mamba:$?
#sleep 1

#$(pwd)/miniforge3/bin/mamba install -y pandas       # > /dev/null 2>&1
#echo pandas:$?
#sleep 10

#echo matplotlib
#$(pwd)/miniforge3/bin/mamba install -y matplotlib   # > /dev/null 2>&1
#if $?; then
#	echo matplotlib:attempt 2
#	sleep 1
#	$(pwd)/miniforge3/bin/mamba install -y matplotlib   # > /dev/null 2>&1
#fi
#echo matplotlib:$?
#sleep 10

#echo sklearn:
#$(pwd)/miniforge3/bin/mamba install -y scikit-learn # > /dev/null 2>&1
#echo sklearn:$?
#sleep 10

#echo run:
/home/users/FeelUsM/miniforge3/bin/python Untitled.py $1 
#echo run:$?
