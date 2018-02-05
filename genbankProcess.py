#! /usr/bin/env python

# This script is for processing genbank flat files. 
# Each record will be saved to a new
# file in fasta format. Only those sequences that are below a
# user-defined length will
# be saved to a new file (if save is entered as indicated below) or the
# record ids and sequence lengths
# will be printed to screen if "check" in entered when calling the script.
# USAGE: python genbankProcess.py NameOfInputFile(genbank)
# sequenceLengthCutoff "check"/"save" optional:NameOfOutputFile

import Bio
from Bio import SeqIO
import sys

if sys.argv[3].lower() == "save":
    input_file = sys.argv[1]
    lengthCutoff = int(sys.argv[2])
    view = sys.argv[3]
    output_file = sys.argv[4]
else:
    input_file = sys.argv[1]
    lengthCutoff = int(sys.argv[2])
    view = sys.argv[3]

if view.lower() == "save":
    file = open(input_file, 'rU')
    output = open(output_file, "w")
    for record in SeqIO.parse(file, "genbank"):
        if len(record.seq) < lengthCutoff:
            SeqIO.write(record, output, "fasta")
else:
    file = open(input_file, 'rU')
    # output = open(output_file, "w")
    for record in SeqIO.parse(file, "genbank"):
        if len(record.seq) > lengthCutoff:
            print len(record.seq)
            print record.id
