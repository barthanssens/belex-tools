class BelexPart(object):
	number = None
	body = None

	def number(self):
		return self.number

	def body(self):
		return body;

	def body_add(self, text):
		self.body = self.body + text

	def __init__(self, number):
		self.number = number
		self.body = ''
