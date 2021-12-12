#!/bin/bash
#SBATCH -p short
#SBATCH --ntasks=20
#SBATCH --output=results.%j.out
#SBATCH --error=results.%j.err


echo "started on $(date)"
echo -e "searching for hamiltonian paths in $1\n"
mpirun python3 hamilton.py "$1"
echo "ended on $(date)"