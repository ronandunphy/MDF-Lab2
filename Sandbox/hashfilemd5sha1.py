import hashlib

inputFile = raw_input("Enter the name of the file:")
openedFile = open(inputFile)
readFile = openedFile.read()

hash_object1 = hashlib.sha1(readFile)
hash_object1_final = hash_object1.hexdigest()

hash_object2 = hashlib.sha256(readFile)
hash_object2_final = hash_object2.hexdigest()

hash_object3 = hashlib.sha512(readFile)
hash_object3_final = hash_object3.hexdigest()

hash_object4 = hashlib.sha1(readFile)
hash_object4_final = hash_object4.hexdigest()

hash_object5 = hashlib.sha1(readFile)
hash_object5_final = hash_object5.hexdigest()

print ("File Name: %s" % inputFile)
print ("SHA-1: %r" % hash_object1_final)
print ("SHA-256: %r" % hash_object2_final)
print ("SHA-512: %r" % hash_object3_final)
print ("SHA-3(256): %r" % hash_object4_final)
print ("SHA-3(512): %r" % hash_object5_final)
