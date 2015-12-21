import re

documents = []

def to_file():
    out_f = open('cacm.xml', 'w')

    header = '<?xml version="1.0"  encoding="UTF-8"  ?>'
    root = '<catalog>'
    print>>out_f, header + '\n' + root + '\n'

    for doc in documents:
        print>>out_f, '\t' + doc.to_XML()

    print>>out_f, '</catalog>'

    out_f.close()

class Document():

    def __init__(self, id):
        self.children = {}
        self.id = id
        documents.append(self)

    def set_children(self, children):
        self.children = children

    def to_XML(self):
        node =  '<document id= \''+self.id+'\'>' 
        for v in self.children.itervalues():
            node = node + '\n' + '\t' + v.to_XML()
        node = node +'\n' + '\t' + '</document>'
        return node



class Title():

    def __init__(self, title):
        self.title = title.strip()

    def to_XML(self):
        return "<title>"+self.title+"</title>"


class Conference():

    def __init__(self, conf):
        self.conference = conf.strip()

    def to_XML(self):
        return "<conference>"+self.conference+"</conference>"


class Author():

    def __init__(self, authors):
        # sweet tits Batman, regex from hell, is matching the authors' name format. many a minute were spent here. fucking perl
        regex = re.compile('([a-z]+\,\s(?:[a-z][a-z]?\.(?:\s)*)+)', re.I)
        self.authors = [i.strip() for i in regex.findall(authors)]

    def to_XML(self):
        node = "<authors>"
        for au in self.authors:
            node = node + '\n\t<author>' + au +'</author>'
        node = node + '\n' + '\t' + '</authors>'
        return node

class Location():

    def __init__(self, location):
        self.location = location.strip()

    def to_XML(self):
        return "<location>"+self.location+"</location>"

class Citation():

    def __init__(self, cit):
        regex = re.compile('(?:\s)*\d+\s{1,4}\d+\s{1,4}\d+')
        self.citations = [c.strip() for c in regex.findall(cit)]

    def to_XML(self):
        node =  "<citations>"
        for c in self.citations:
            node = node + '\n' + '\t' + '<citation>' + c + '</citation>'
        node =  node + '\n' + '\t' + '</citations>'
        return node


class Keywords():

    def __init__(self, kw):
        self.keywords = kw.strip()

    def to_XML(self):
        return "<keywords>"+self.keywords+"</keywords>"

class Version():
    def __init__(self, v):
        self.version = v.strip()

    def to_XML(self):
        return "<version>"+self.version+"</version>"

class Abstract():

    def __init__(self, ab):
        ab = ab.strip().replace('<', '&lt;').replace('&', '&amp;')
        self.abstract = ab

    def to_XML(self):
        return "<abstract>"+self.abstract+"</abstract>"