#essentially the same thing as what neetcode did, but instead of creating another class, this solution simply creates nested hashmap within Trie class. To determine end of the word, this solution uses "-" to store in hashmap

class Trie(object):

	def __init__(self):
		self.trie = {}


	def insert(self, word):
		t = self.trie
		for c in word:
			if c not in t: t[c] = {}
			t = t[c]
		t["-"] = True


	def search(self, word):
		t = self.trie
		for c in word:
			if c not in t: return False
			t = t[c]
		return "-" in t

	def startsWith(self, prefix):
		t = self.trie
		for c in prefix:
			if c not in t: return False
			t = t[c]
		return True