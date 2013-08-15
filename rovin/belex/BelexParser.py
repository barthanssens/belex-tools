from HTMLParser import HTMLParser
from rovin.belex.BelexParts import BelexPart

class BelexParser(HTMLParser):
	articles = []
	article = None
	tag = None

	def all_articles(self):
		return self.articles

	def handle_starttag(self, tag, attrs):
		self.tag = tag
		if tag == 'a':
			attrs = dict(attrs)
			if ('name' in attrs) and (attrs['name'].startswith('Art.')):
				number = attrs['name'].replace('Art.', '')
				self.article = BelexPart(number)
				self.articles.append(self.article)

	def handle_endtag(self, tag):
		self.tag = None
		if tag == 'table':
			self.article = None

	def handle_data(self, data):
		if self.article:
			if self.tag != 'a':
				data = data.lstrip('.')
				data = data.replace('\n', ' ')
				data = data.replace('  ', ' ')
				data = data.strip()
				self.article.body_add(data)
