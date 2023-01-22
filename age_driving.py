driving = input("Have you been drive a car before? (yes/no) ")
if driving != "yes" and driving != "no":
    print("You can only type yes/no. ")
    raise SystemExit
age = input("How old are you? ")
age = int(age)
if driving == "yes":
    if age >= 18:
        print("You are pass. ")
    else :
        print("You can't drive a car below 18 yrs old. ")
elif driving == "no":
    if age >= 18:
        print("You should go apply a license. ")
    else:
        print("You should wait a few years to apply a license. ")
