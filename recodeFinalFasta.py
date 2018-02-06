#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Rename sequences in fasta file by replacing genbank accession number with species and isolate code so that individual gene files can readily be combined into a concatenated alignment')
parser.add_argument('-f', '--fastaFile', required=True, nargs=1, help='required: specify the fasta file you want to edit')
parser.add_argument('-t', '--locusTable', required=True, nargs=1, help='required: specify the table with the old codes and new codes. MAKE SURE THE TABLE HAS UNIX LINE ENDINGS AND IS COMMA DELIMITED. IF YOU OPENED IT IN EXCEL TO EDIT, IT PROBABLY DOES NOT HAVE UNIX LINE ENDINGS. OPEN IN TEXTWRANGLER OR OTHER TO SET ENDINGS TO UNIX. ')
parser.add_argument('-o', '--output', required=True, nargs=1, help='required: specify the output file name ex: its.final.fasta')
parser.add_argument('-p', '--previousNameColumnNumber', required=True, nargs=1, help='required: specify the column number containing the old name. Remember to count from 0')
parser.add_argument('-n', '--newNameColumnNumber', required=True, nargs=1, help='required: specify the column number containing the new name. Remember to count from 0')
args = parser.parse_args()

fasta = open(args.fastaFile[0], 'r')
fastaData = fasta.read()
fasta.close()

with open(args.locusTable[0]) as codes:
    count = 0
    codes.readline()  # to skip header line
    for line in codes:
        oldCode = line.strip().split(",")[int(args.previousNameColumnNumber[0])]
        newCode = line.strip().split(",")[int(args.newNameColumnNumber[0])]
        oldCode = oldCode
        newCode = newCode
        if oldCode in fastaData:
            fastaData = fastaData.replace(oldCode, newCode)
            count += 1
            print oldCode + "  " + newCode
    print str(count) + " codes replaced in " + str(args.fastaFile[0])

fastaNew = open(args.output[0], 'w')
fastaNew.write(fastaData)
fastaNew.close()
