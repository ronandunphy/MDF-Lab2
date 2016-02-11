import hashlib
mystring = raw_input ('Enter String to hash: ')
# Assumes the default UTF-8
hash_object1 = hashlib.sha1(mystring.encode())
hash_object2 = hashlib.sha256(mystring.encode())
hash_object3 = hashlib.sha512(mystring.encode())
hash_object4 = hashlib.sha512(mystring.encode())
print ("SHA-1:" + hash_object1.hexdigest())
print ("SHA-256:" + hash_object2.hexdigest())
print ("SHA-512:" + hash_object3.hexdigest())
print ("SHA-3:" + hash_object4.hexdigest())
