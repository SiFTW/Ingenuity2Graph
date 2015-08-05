#takes a file containing ingenuity pathways and a file containing a list of ClueGO genes and creates 2 files of node and edges for importing into graph software

import sys
import csv
from collections import defaultdict

def main (args):
    """Usage: pathwaysToNetworks.py IngenuityFile GeneListFile"""
    
    ingenuityFile=args[1]
    geneFile=args[2]
    pathway_dict = dict()
    pvalue_dict = dict()
    print 'opening '+ingenuityFile
    with open(ingenuityFile,'rU') as csvfile:
        listReader=csv.reader(csvfile,delimiter=",",dialect=csv.excel_tab)
        for row in listReader:
            if row[0] not in pathway_dict:
                pathway_dict[row[0]]=set()
                pvalue_dict[row[0]]=row[1]
            genesString=row[4]
            genesString.replace('/',',')
            genesInPathway=genesString.split(",")
            for gene in genesInPathway:
                pathway_dict[row[0]].add(gene)
    
    #for key in pathway_dict:
    #    print key,pathway_dict[key]
    edgesList=[["Source","Target","Type","Weight"]]
    nodeList=[["ID","Nodes","Weight"]]
    aliases=[]
    allNamesForGene=[]
    nodeDict=defaultdict(lambda: 0)
    with open(geneFile,'rU') as csvfile:
        listReader=csv.reader(csvfile,delimiter=",",dialect=csv.excel_tab)
        for row in listReader:
            
            aliases=row[3].replace("[","")
            aliases=aliases.replace("]","")
            aliases=aliases.split(",")
            allNamesForGene = [row[0]]+aliases
            
            for key in pathway_dict:
                if lists_overlap(allNamesForGene,pathway_dict[key]):
                    edgesList.append([key,row[0],'Undirected',pvalue_dict[key]])
                    nodeDict[key]+=1
                    nodeDict[row[0]]+=1

    for node in nodeDict.items():
        nodeList.append([node[0],node[0],node[1]])
    
    with open("outputEdgeList.csv","wb") as f:
        writer=csv.writer(f)
        writer.writerows(edgesList)
    with open("outputNodeList.csv","wb") as f:
        writer=csv.writer(f)
        writer.writerows(nodeList)

        
                                     
            
def lists_overlap(a,b):
    sb=set(b)
    sa=set(a)
    return any(e1 in sb for e1 in sa)

if __name__ == '__main__':
  main(sys.argv)
