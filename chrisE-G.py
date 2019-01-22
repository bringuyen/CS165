import hashlib as hl
import copy
import sys
import time
salt = "hfT7jp2q"
magic = "$1$"
teamHash = "WWkD4idIBJxT6tLe/mPUG1"
base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
cbase64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
encodeSet = [11,4,10,5,3,9,15,2,8,14,1,7,13,0,6,12]
pw = ""

#initialize password queue
pwQueue = []
alpha = []
for i in range(97,123):
	if i == 101: #and i < 104:
		pwQueue.append(chr(i))
	alpha.append(chr(i))
	
#md5 crypt
def md5sum(pw):
	#Alternate Sum 2.
	newHash = hl.md5(pw+salt+pw)
	altSum = newHash.digest()
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
	while pwLen:
		inter.update(chr(0) if pwLen & 1 else pw[0])
		pwLen = pwLen >> 1	
	
	#brute force iteration
	intermediate = inter.digest()
	for i in range(1000):
		interI = hl.md5(pw if i & 1 else intermediate)
		if i % 3:
			interI.update(salt)
		if i % 7:
			interI.update(pw)
		interI.update(intermediate if i & 1 else pw)
		intermediate = interI.digest()
	
	orange = ""
	for i in encodeSet:
		orange += intermediate[i]
	iBS = "".join("{0:08b}".format(ord(x), 'd') for x in orange)
	toEncode = [int(iBS[:2],2)]
	bitLen = len(iBS)
	
	n = 6
	for j in [int(iBS[i:i+n],2) for i in range(2, len(iBS), n)]:
		toEncode.append(j)
	finalHash = ""
	for x in toEncode[::-1]:
		finalHash += cbase64[x]
	#print "{0}{1}${2}".format(magic,salt,finalHash)
	return finalHash
count = 0
check = 0
t0 = time.time()
pw = ""
pw0 = ""
pw1 = ""
pw2 = ""
pw3 = ""
pw4 = ""
for a in range(101,104):
	pw = chr(a)
	for b in range(97,123):
		pw0 = pw + chr(b)
		for c in range(97,123):
			pw1 = pw0 + chr(c)
			for d in range(97,123):
				pw2 = pw1 + chr(d)
				for e in range(97,123):
					pw3 = pw2 + chr(e)
                                        if md5sum(pw3) == teamHash:
					    print "PASSWORD: " + pw3
					    break
					for f in range(97,123):
						pw4 = pw3 + chr(f)
						if md5sum(pw4) == teamHash:
					                print "PASSWORD: " + pw4
							break
                        print pw4
t1 = time.time()
print "Password throughput: " + str((t1-t0)) + "sec"
		
