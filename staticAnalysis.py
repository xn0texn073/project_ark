import hashlib as s

class StaticAnalysis:
	def __init__(self):
		print "__init__ start"

	def genSHA256(self,filename):
		self.filename = filename
		print "filename is :%s" % (self.filename)
		digestResult = s.sha256(self.filename).hexdigest()

		return digestResult

test = StaticAnalysis()
str = test.genSHA256("this is teststring")
print "SHA256 : %s" % str
