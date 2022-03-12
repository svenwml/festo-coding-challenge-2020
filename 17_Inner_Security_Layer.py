import string
import itertools
import hashlib

charactersAllowed = string.ascii_lowercase + string.ascii_uppercase + string.digits

for subset in itertools.permutations(charactersAllowed, 2):

    numberBegin = ('s','Q','y','W')
    numberEnd = ('3', 'w')

    wholeNumber = numberBegin + subset + numberEnd
    
    wholeNumberBytes = b""

    for i in range(8):
        wholeNumberBytes = wholeNumberBytes + wholeNumber[i].encode('utf-8')
	
    md5 = hashlib.md5(wholeNumberBytes).hexdigest()

    if md5.startswith("002a8a8b23d03e70"):    
        for digit in wholeNumber:
            print(digit, end='')