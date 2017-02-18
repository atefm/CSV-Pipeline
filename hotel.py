import re

class Hotel:

	def __init__(self, row):
		self.name = row[0]
		self.address = row[1]
		self.stars = int(row[2])
		self.contact = row[3]
		self.phone = row[4]
		self.uri = row[5]
		
	def name_has_valid_utf8_encoding(self):
		return self.is_utf8(self.name)
		
	def stars_are_valid(self):
		return self.stars >= 0 and self.stars <= 5

	def url_is_valid(self):
		searchFor = ["http?://...", "www", ".com", "https://..."]
		pattern = '|'.join(map(re.escape,searchFor))
		return (re.search(pattern, self.uri))

	def is_utf8(self, string):
		try:
			string.decode('utf-8')
			return True
		except UnicodeError:
			return False
		
	def data_is_valid(self):
		return self.name_has_valid_utf8_encoding() and self.stars_are_valid() and self.url_is_valid()
			
