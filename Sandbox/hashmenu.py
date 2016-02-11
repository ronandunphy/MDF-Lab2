ans=True
while ans:
    print ("""
    1.Get the Hash values of a String
    2.Get the Hash values of a File
    3.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1": 
      print("\n String hash: xxx") 
    elif ans=="2":
      print("\n File hash: xxx") 
    elif ans=="3":
      print("\n Press Return to Exit.") 
    elif ans !="":
      print("\n Not Valid Choice Try again") 
