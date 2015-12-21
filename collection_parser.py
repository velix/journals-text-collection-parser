import os
from tags import *

#open file as string
fyle = open('cacm\\cacm.all').read()

handlers = ['.K', '.N', '.A', '.B', '.C', '.X', '.T', '.W']

stack = []
content = ''

lines = fyle.split('\n')

for line in lines:
    if line.startswith('.I'):
        if not (content == ''):
            stack.append(content)

        stack.append('.I')
        content = line.split(' ')[1]
    elif(line in handlers):
        stack.append(content)
        stack.append(line)
        content = ''
    else:
        content = content + ' ' + line

# to append the last content of the file
stack.append(content)
# up untill now handlers did not include .I
handlers.append('.I')
children = {}

while stack:
    content = stack.pop()
    handler = stack.pop()

    if handler in handlers:
        if handler == '.T':
            title = Title(content)
            children[1] = title
        elif handler == '.B':
            conference = Conference(content)
            children[3] = conference
        elif handler == '.A':
            author = Author(content)
            children[4] = author
        elif handler == '.N':
            location = Location(content)
            children[7] = location
        elif handler == '.X':
            citation = Citation(content)
            children[8] = citation
        elif handler == '.K':
            keywords = Keywords(content)
            children[5] = keywords
        elif handler == '.C':
            version = Version(content)
            children[6] = version
        elif handler == '.W':
            abstract = Abstract(content)
            children[2] = abstract
        elif handler == '.I':
            document = Document(content)
            document.set_children(children)
            document.to_XML()
            children = {}
        else:
            print "stack badly formatted"
            print "handler: "+handler
            print "content: "+content
            os.system("pause")
    else:
        print "found not handler"
        break

to_file()

