#!/bin/bash

#$ -cwd
#$ -j y
#$ -q all.q

#$ -t 1-2

source /mnt/nfs6/wikipedia.proj/gdalvenv/bin/activate
export LD_LIBRARY_PATH=/mnt/nfs6/wikipedia.proj/gdalvenv/lib:$LD_LIBRARY_PATH

python /mnt/nfs6/wikipedia.proj/osm/python/pointpoly_country.py $SGE_TASK_ID 100000