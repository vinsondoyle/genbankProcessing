Genbank Processing
=====================
Many phylogenetic analyses build on previous work published by others. Sometimes we use data from this work that is held in repositories such as [Dryad](http://datadryad.org/) or [TreeBase](treebase.org), but there are also times when we want the untrimmed and unaligned sequences and thus download them from sequence databases such as [GenBank](http://www.ncbi.nlm.nih.gov/genbank/). Authors are required, hopefully, to report the GenBank accession numbers somewhere in the manuscript. We can use those accession numbers, such as [JX145197](http://www.ncbi.nlm.nih.gov/nuccore/JX145197.1), to find the referenced sequences and view them in several formats (fasta, genbank [.gb], asn). Fasta format is the most directly usable for phylogenetic studies because alignment programs will take a multi-fasta file (single file containing multiple fasta formatted sequences) and align the bases as an assessment of homology. However, the metadata associated with these sequences is lost once you convert them to fasta format, such as the journal, authors, and gene features. You can always look them up again, but I find that it is convenient to have these files available in the directory where I keep my data files for a particular project.

The scripts in this repository are meant to facilitate conversion from GenBank (.gb) flat file format to fasta and subsequently reformat the fasta files depending on your preferences. They are simple and probably duplicated elsewhere.


Detailed Usage to be added
=====================
Read the usage info at the beginning of each script for instructions.
