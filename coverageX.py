from difflib import SequenceMatcher
from tinydb import TinyDB
from colorama import *

def compareGenes(genes1,genes2):
  maxsim = 0
  gene1max = ""
  gene2max = ""
  for gene1 in genes1:
      for gene2 in genes2:
        simlarity = similar(gene1["translation"][0], gene2["translation"][0]) * 100
        
        if(simlarity > maxsim):
          maxsim = simlarity
          gene1max = gene1["locus_tag"][0]
          gene2max = gene2["locus_tag"][0]
      
      printFunc(gene1max, gene2max, maxsim)
      maxsim = 0
      
def makeDB(gene1max, gene2max, maxsim):
  db = TinyDB("Similarities.json")
  db.table('genes')
  db.insert({"gene1":gene1max, "gene2":gene2max, "simperc":maxsim})
  
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def printFunc(gene1max,gene2max,maxsim):
  if maxsim < 25:
    print Fore.RED + "Gene " + str(gene1max) + " is " + str(maxsim) + "% similar to gene " + str(gene2max)
  elif maxsim > 25 and maxsim < 75:
    print Fore.YELLOW + "Gene " + str(gene1max) + " is " + str(maxsim) + "% similar to gene " + str(gene2max)
  else:
    print Fore.GREEN + "Gene " + str(gene1max) + " is " + str(maxsim) + "% similar to gene " + str(gene2max)

def compare(a, b):
  init(autoreset=True)
  
  db1 = TinyDB(a)
  db2 = TinyDB(b)
  
  genes1 = db1.table('genes')
  genes2 = db2.table('genes')
  
  print "The first genome is " + str(len(genes1)) + " genes long."
  print "The second genome is " + str(len(genes2)) + " genes long."
  
  if len(genes1) > len(genes2):
    compareGenes(genes1, genes2)
    
  else:
    compareGenes(genes2, genes1)