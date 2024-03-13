year = input("")
yearna = int(year)%4 #4
yearmo = int(year)%400 #400
yearx = int(year)%100 #100

if yearna == 0:
    if yearx == 0:
        if yearmo ==0:
            print("1")
        else:
            print("0")
    else:
        print("1")
else:
    print("0")