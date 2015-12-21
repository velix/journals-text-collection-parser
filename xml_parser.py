from lxml import etree
from bs4 import BeautifulSoup
import operator

# validate xml using xsd
schema_doc = etree.parse('cacm.xsd')
schema = etree.XMLSchema(schema_doc)

parser = etree.XMLParser(recover = True, schema = schema)
doc = etree.parse('cacm.xml', parser)

# parse xml with BeautifulSoup
fyle = open('cacm.xml')
soup = BeautifulSoup(fyle, 'lxml-xml')

# collection of unique elements to hold words 
# keys will be the words and values the counts of them
words = {}

for string in soup.stripped_strings:
    for word in string.split():
        word = word.strip('(){}[]$%.,')
        if word in words:
            words[word] = words[word] + 1
        else:
            words[word] = 1

# sort in descending order
sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse = True)

with open("word_collection.txt", "w") as out_fyle:
    # write to file
    out_fyle.write('\n'.join('{}, {}'.format(x[0], x[1]) for x in sorted_words))
