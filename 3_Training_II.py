import hashlib
    
md5 = hashlib.md5("Ok, got it. Easy!".encode('utf-8')).hexdigest()

print(md5[0:5])