import string
import itertools
import hashlib

alphaNumericCharacters = []

for char in string.printable:
    if char.isalnum():
      alphaNumericCharacters.append(char)  

for candidate in itertools.permutations(alphaNumericCharacters, 3):
    
    md5 = hashlib.md5(candidate[0].encode('utf-8') + candidate[1].encode('utf-8') + candidate[2].encode('utf-8')).hexdigest()
    
    if md5.startswith("19acf8371f"):
        print(candidate[0] + candidate[1] + candidate[2])