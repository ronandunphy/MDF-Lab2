import sys
import hashlib
from sha3 import sha3_256, sha3_512
import string

ans=True
while ans:
    
    print ("""
    Please choose one of the following options?
    
    1.Get Hash values of a String
    2.Get Hash values of a File
    3.Exit
    """)
    ans=raw_input(">")
    if ans=="1": 
      mystring = raw_input ('Please enter a string: ')
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

      print ("The string entered is: %s" % mystring)
      print ("SHA-1: " + hash_object1.hexdigest())
      print ("SHA-256: " + hash_object2.hexdigest())
      print ("SHA-512: " + hash_object3.hexdigest())
      print ("SHA-3(256): " + hash_object4.hexdigest())
      print ("SHA-3(512): " + hash_object5.hexdigest())
    elif ans=="2":
      inputFile = raw_input("Please enter the name of a file:")
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

      print ("The filename is: %s" % inputFile)
      print ("SHA-1: " + hash_object1_final)
      print ("SHA-256: " + hash_object2_final)
      print ("SHA-512: " + hash_object3_final)
      print ("SHA-3(256): " + hash_object4_final)
      print ("SHA-3(512): " + hash_object5_final) 
    elif ans=="3":
      sys.exit() 
    elif ans !="":
      print("\n Not a valid selection. Please try again.") 
