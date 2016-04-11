from bibpy import *

data = clear_comments(open("bibtex.bib", 'r').read())
bib = Parser(data)
bib.parse()
data = bib.json()
print data