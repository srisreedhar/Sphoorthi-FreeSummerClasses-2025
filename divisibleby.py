# find the sum/total of all the even numbers,
# find the product of all the even numbers
# find the sum & product of all the odd numbers 
# odd numbers, 
# numbers divisible by 3, 
# numbers divisible by 4, 
# numbers divisible by 5 
# and numbers divible by 10
# find number of values respectively in even & odd


numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

sum_even = 0
sum_odd = 0
product_odd = 1
product_even = 1

even_total = 0
odd_total = 0

div_3 = []
div_4 = []
div_5 = []

# find the sum/total of all the even numbers,
# find the product of all the even numbers
# find the sum & product of all the odd numbers 

for num in numbers:
    if num%2 == 0:
        sum_even = sum_even+num
        even_total = even_total + 1
        product_even = product_even * num
    else:
        sum_odd = sum_odd + num 
        odd_total = odd_total + 1
        product_odd = product_odd * num


# numbers divisible by 3,4,5

for everynum in numbers:
    if everynum%3 == 0:
        div_3.append(everynum)
    elif everynum%4 == 0:
        div_4.append(everynum)
    elif everynum%5 == 0:
        div_5.append(everynum)


print("sum of all the even is :",sum_even,"\n","sum of all the odd is :",sum_odd,"product of even ",product_odd,"product of even ",product_even,'\n\n\n',"divisible by 3",div_3,"\n","divisible by 4 ",div_4, "divisble by 5 ",div_5)
