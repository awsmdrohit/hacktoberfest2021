# Python Program to Check Entered Year is Leap Year or Not

Year = int(input("ENTER A YEAR --> "))

if (Year % 4) == 0:
    if(Year % 100) == 0:
        if (Year % 400) == 0:
            print("{0} IS A LEAP YEAR".format(Year))
        else:
            print("{0} IS NOT A LEAP YEAR".format(Year))
    else:
        print("{0} IS A LEAP YEAR".format(Year))
else:
    print("{0} IS NOT A LEAP YEAR".format(Year))
