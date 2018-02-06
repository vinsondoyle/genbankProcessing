#! /usr/bin/env python

#USAGE: python reformatFasta.py NameOfInput(fasta - output from genbankProcess.py) NameOfOutputFile(fasta)

import sys

newFile = open(sys.argv[2], 'w')

with open(sys.argv[1], 'r') as f:
    for line in f:
        if line.startswith(">"):
            accession = line.split()[0]
            genus = line.split()[1]
            species = line.split()[2]
            newFile.write(accession + "." + genus + "." + species + "\n")
    else:
        newFile.write(line)

newFile.close()
