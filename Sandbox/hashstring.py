import sys
import hashlib
from sha3 import sha3_256, sha3_512
import string
mystring = raw_input ('Enter String to hash: ')
hash_object1 = hashlib.sha1(mystring.encode())
hash_object2 = hashlib.sha256(mystring.encode())
hash_object3 = hashlib.sha512(mystring.encode())
hash_object4 = hashlib.sha3_256(mystring.encode())
hash_object5 = hashlib.sha3_512(mystring.encode())
print ("SHA-1:" + hash_object1.hexdigest())
print ("SHA-256:" + hash_object2.hexdigest())
print ("SHA-512:" + hash_object3.hexdigest())
print ("SHA-3(256):" + hash_object4.hexdigest())
print ("SHA-3(512):" + hash_object5.hexdigest())
