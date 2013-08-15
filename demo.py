from rovin.belex.BelexParser import BelexParser
from urllib import FancyURLopener
from os import path

url = "http://www.ejustice.just.fgov.be/cgi_loi/loi_a1.pl?language=nl&table_name=wet&la=N&cn=1994021730&&caller=list&N&fromtab=wet"
filename = "constitution-nl.html"

if not path.isfile(filename):
	print "Downloading", url
	downloader = FancyURLopener()
	downloader.retrieve(url, filename)

f = open(filename, 'r')
html = f.read()

parser = BelexParser()
parser.feed(html)
for article in parser.all_articles():
	print " <<<< "
	print article.number
	print "BODY:" + article.body
	print " >>>> "
