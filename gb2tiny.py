from Bio import SeqIO
from tinydb import TinyDB

def parse(filename, database):
  #create or open db file
  db = TinyDB(database)
  
  #Get all sequence records for the specified genbank file
  recs = [rec for rec in SeqIO.parse(filename, "genbank")]

  phage = db.table('phage')
  phage.insert({'organism': recs[0].annotations.get("organism","NOVALUE"), 'molecule_type':recs[0].annotations.get("molecule_type","NOVALUE"), 'accession':recs[0].annotations.get(["accessions"][0],"NOVALUE"), 'size':len(recs[0])})
  # print the CDS sequence feature summary information for each feature in each
  # sequence record
  genes = db.table('genes')
  feats = [feat for feat in recs[0].features if feat.type == "CDS"]
  for feat in feats:
    genes.insert({'location_start':str(feat.location.start), 'location_end':str(feat.location.end),'strand':str(feat.location.strand),'type':feat.type, 'gene':feat.qualifiers.get("gene","NOVALUE"), 'codon_start':feat.qualifiers.get("codon_start","NOVALUE"), 'locus_tag':feat.qualifiers.get("locus_tag","NOVALUE"), 'note':feat.qualifiers.get("note","NOVALUE"), 'product':feat.qualifiers.get("product","NOVALUE"), 'transl_table':feat.qualifiers.get("transl_table","NOVALUE"), 'translation':feat.qualifiers.get("translation","NOVALUE")})