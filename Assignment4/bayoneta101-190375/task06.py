# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14FtrvhtMq0tkliJKhES4Iu2p1PxH3NBv

**Task 06: Modifying RDF(s)**
"""
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

# TO DO
# Visualize the results
g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g.triples((None,None,RDFS.Class)):
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# TO DO
# Visualize the results
g.add((ns.Researcher,RDFS.subClassOf,ns.Person))
for s, p, o in g.triples((ns.Researcher,None,None)):
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

# TO DO
# Visualize the results

rdfs = Namespace("https://www.w3.org/TR/rdf-schema/#")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

g.add((ns.JaneSmith, RDF.type, ns.Researcher))
g.add((ns.JaneSmith,vcard.FN,Literal("Jane Smith")))

for s, p, o in g.triples((ns.JaneSmith,None,None)):
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

# TO DO
# Visualize the results


g.add((ns.JaneSmith,vcard.Given,Literal("Jane")))
g.add((ns.JaneSmith,vcard.Family,Literal("Smith")))
g.add((ns.JaneSmith,vcard.FN,Literal("Jane Smith")))

for s, p, o in g.triples((ns.JaneSmith,None,None)):
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

# TO DO
# Visualize the results

g.add((ns.UPM,RDF.type,ns.University))
g.add((ns.JohnSmith,ns.WorksIn,ns.UPM))

for s, p, o in g.triples((ns.JohnSmith, None, None)):
  print(s,p,o)