#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import codecs
import commands


file_location = "p3wordcount.txt"
file_encoding = commands.getoutput('file -b --mime-encoding %s' % file_location)
inputfile = codecs.open(file_location, "r", file_encoding)
outputfile = codecs.open("p3topten.txt", "wb", "utf-8")

class Node(object):
    def __init__(node, name, count):
        node.name = name
        node.count = count

ArList = []
token = []


for line in inputfile:
    token = re.split(' |\\n|\t', line)
    ArList.append(Node(token[0], int(token[1])))
#for x in ArList:
    #outputfile.write(x.name+" "+x.count+"\n")  #test read input correctly or not
    #this gets the node and the count into the ArList.


top = 0
i = 0
j = 0
while i < 10:
    top = 0
    j = 0
    index = -1
    for nod in ArList:
        if (nod.count > top):
            top = nod.count
            index = j
        j+=1
    outputfile.write(ArList[index].name+"\n")
    ArList[index].count = -1
    
    i+=1





