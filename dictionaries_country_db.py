countrydb = {}

while True:
  print("1. Insert")
  print("2. Display all countries")
  print("3. Display all capitals")
  print("4. Get capital")
  print("5. Delete")

  choice = int(input("Enter yout choice : "))
  

  if choice == 1:
    country = input("enter the country : ")
    capitals = input("enter the capital : ")
    countrydb[country] = capitals

  elif choice == 2:
    print(countrydb.keys())

  elif choice == 3:
    print(countrydb.values())

  elif choice == 4:
    country = input("enter the country : ")
    print(countrydb.get(country))

  elif choice == 5:
    country = input("enter the country : ")
    del(countrydb[country])




  