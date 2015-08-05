#Ingenuity to Pathways

This program takes a ClueGo gene list and generates an edge file that contains edges to each one of the pathways it is a member of within the Ingenuity file. (it checks all aliases of the gene against the pathway file).

The edge weights are the -log(p-value) associated with that ingenuity pathway.

A node file is created for each gene and pathway, with weight of each node is equal to the number of edges it is a member of (its degree in graph-theory terminology).

The program takes CSV inputs (can be exported from the excel) and generates CSV files that can be imported into Gephi as node and edge tables. Input files must have the format of the attached samples. Output files generated are suitable for importing into any network visualisation software.

##Usage

The program can be run by giving the input files as arguments as follows (only tested on python 2.7):

```
python pathwaysToNetworks.py Example_Ingenuity_Pathways-Genes.csv Example_ClueGO_Genes-Pathways.csv
```