import hashlib import md5
import itertools, string
from multiprocessing as Pool

salt = hfT7jp2q$WWkD4idIBJxT6tLe
hash = mPUG1:16653:0:99999:7:::
string pw;

# generate password
for a in range(26):
    pw += a
    for b in range(26):
        pw += b
        for c in range(26):
                pw += c
                for d in range(26):
                    pw += d
                    for e in range(26):
                        pw += e
                        for f in range(26):
                            pw += f
                            pwhash = md5(pw).digest() #return byte representation

# compute Alternate sum, md5(password + salt + password)
md5(password + string + password)

#compute intermediate sum

def main():
    