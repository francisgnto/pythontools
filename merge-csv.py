#!/usr/bin/env python
# Usage: this script merges all csv's found in the csv folder. files must contain the same number of columns.
import io
import os
import sys
import pandas as pd

pieces = []
for infile in os.listdir('csv/'):
    infile = 'csv/' + infile
    print(infile)
    pieces.append(infile)

combined_csv = pd.concat( [ pd.read_csv(f) for f in pieces ] )
f = open('out.csv', 'w')
out = combined_csv.to_csv( index=False )
f.write(out)
f.close()
