import hashlib as hl
import copy
import sys
salt = "hfT7jp2q"
magic = "$1$"
passwrd = "abcdef"
print hl.md5("hello").hexdigest()
help = ""
for i in range(3):
	help += "a"

pw = ""
pwQueue = []
alpha = []
for i in range(97,123):
	pwQueue.append(chr(i))
	alpha.append(chr(i))
	

def md5sum(pw):
	print "password: " + pw
	print "Alternate sum to hash: " + pw + salt + pw
	
	#Alternate Sum 2.
	newHash = hl.md5(pw+salt+pw)
	altSum = newHash.digest()
	print "Alternate sum hash digest: " + altSum
	print "Alternate sum hash hex digest: " + ":".join("{:02x}".format(ord(c)) for c in altSum)
	print "length of Alternate Sum: " + str(len(altSum))
	pwLen = len(pw)
	#intermediate 3.1-3.3
	inter = hl.md5(pw+magic+salt)
	#intermediate 4.
	
	if len(altSum) >= pwLen:
		inter.update(altSum[:pwLen])
	else:
		i = len(pw)
		while i>0:
			inter.update(altSum[:i])
			i-=16
			
	#intermediate 5
	bitString = "{0:b}".format(pwLen)
	print bitString
	for i in bitString[::-1]:
		if i == '0':
			inter.update('\0')
		else:
			inter.update(pw[0])
			
	
	intermediate = inter.digest()
	interHex = inter.hexdigest()
	print "Intermediate 0: " + intermediate
	print "Intermediate 0 hex: " + ":".join("{:02x}".format(ord(c)) for c in intermediate)
	#intermediate i cal
	for i in range(100):
		interI = hl.md5(pw if i & 1 else intermediate)
		if i % 3:
			interI.update(salt)
		if i % 7:
			interI.update(pw)
		interI.update(intermediate if i & 1 else pw)
		intermediate = interI.digest()
		interHex = interI.hexdigest()
		
	print "Intermediate 100: " + intermediate
	print "Intermediate 100 hex: " + ":".join("{:02x}".format(ord(c)) for c in intermediate)

md5sum(passwrd)
		
