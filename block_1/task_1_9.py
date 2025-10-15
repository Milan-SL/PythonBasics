user = input("Write username:")

while True:
    pswd = input("Write a Password with at least 8 letters:")
    if len(pswd) < 8 :  print(f"Password is too short try again")
    else : 
        print("Password is good")    
        break