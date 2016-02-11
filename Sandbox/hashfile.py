import sys
import hashlib
from sha3 import sha3_256, sha3_512
import string

inputFile = raw_input("Enter the name of the file:")
openedFile = open(inputFile)
readFile = openedFile.read()

hash_object1 = hashlib.sha1(readFile)
hash_object1_final = hash_object1.hexdigest()

hash_object2 = hashlib.sha256(readFile)
hash_object2_final = hash_object2.hexdigest()

hash_object3 = hashlib.sha512(readFile)
hash_object3_final = hash_object3.hexdigest()

hash_object4 = hashlib.sha3_256(readFile)
hash_object4_final = hash_object4.hexdigest()

hash_object5 = hashlib.sha3_512(readFile)
hash_object5_final = hash_object5.hexdigest()

print ("File Name: %s" % inputFile)
print ("SHA-1: " + hash_object1_final)
print ("SHA-256: " + hash_object2_final)
print ("SHA-512: " + hash_object3_final)
print ("SHA-3(256): " + hash_object4_final)
print ("SHA-3(512): " + hash_object5_final)
