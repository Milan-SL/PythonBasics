weigh = float(input("weight(in kg):"))
gender = (input("gender(m/f):"))
if gender == "f":
    if weigh <= 48:
        print ("you are a flying weight female")
    elif weigh <= 55:
        print("you are a light weight female")
    elif weigh <= 63:
        print("you are a middle weight female")
    elif weigh >= 64:
        print("you are heavy weight female")
elif gender == "m":
    if weigh <= 55:
        print("you are flying weight male")
    elif weigh <= 66:
        print("you are a light weight male")
    elif weigh <= 84:
        print("you are a middle weight male")
    elif weigh >= 85:
        print("you are heavy weight male")