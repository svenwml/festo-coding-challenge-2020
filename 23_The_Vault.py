import string
import itertools
import hashlib

possibleParts = ["06", "0b", "O6", "Ob", "n0", "nO", "6u", "bu", "qg", "9g", "q9"]

for subset in itertools.permutations(possibleParts, 4):

    md5 = hashlib.md5(subset[0].encode('utf-8') + subset[1].encode('utf-8') + subset[2].encode('utf-8') + subset[3].encode('utf-8')).hexdigest()
    
    if md5.startswith("a84ba651fd122ef5"):    
        for digit in subset:
            print(digit, end='')