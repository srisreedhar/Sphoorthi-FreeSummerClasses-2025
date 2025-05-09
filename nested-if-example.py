# find if a number is greater than x or lesser than x or equal to x
# x & number can be any integers


# Data part

num1 = input("Enter number one for comparison :")
num2 = input("Enter number two for comparison :")


# Logic

num1 = int(num1)
num2 = int(num2)


if num1 > num2:
    print(num1,"is greater than ",num2)
elif num1 < num2:
    print(num2,"is greater than ",num1)
elif num1 == num2:
    print(num1,"is equal to ",num2)
else:
    print("what number have you entered? ")