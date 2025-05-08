# ask the user to enter a number and tell us if the number is odd or even

# Data part

number = input("please enter a number : ")


# Logic Part

num = int(number)


if num%2 == 0:
    print("Entered number %s is Even"%(number))
else:
    print("Entered number %s is odd"%(number))
