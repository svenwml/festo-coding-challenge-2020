import string
import itertools
import hashlib

for subset in itertools.permutations(string.digits, 6):
        
    numberEnd = ('3','0','0','6','3','1')
    wholeNumber = subset + numberEnd
    wholeNumberBytes = b""
    
    for i in range(12):
        wholeNumberBytes = wholeNumberBytes + wholeNumber[i].encode('utf-8')
    
    md5 = hashlib.md5(wholeNumberBytes).hexdigest()
    
    if md5.startswith("351635d71448baca"):
        for digit in wholeNumber:
            print(digit, end='')