known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi, my name is travis")
    name = input("What is your name?:  ").strip().capitalize()
    
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed ? (Y/N) :").lower()

        if remove == "y":
           known_users.remove(name)
           print("Name removed succesfully")
           
                  
    else:
      print("Hmm i dont think i have met you yet {}".format(name))
      add_me = input("Would you like to be addes to the system? : (Y/N)").strip().lower()
      if add_me == "y":
          known_users.append(name)
          print("New name added")
      elif add_me == "n":
          print("No problem")
