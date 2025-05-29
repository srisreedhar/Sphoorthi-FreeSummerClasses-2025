Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def interest(principle,time,rate):
    amount = (p*t*r)/100
    return amount


def junk(string,number):
    return string*number

def age(current_year,birth_year):
    age=current_year-birth_year
    return age

age(2025,2000)
25


age(2000,2025)
-25


age(birth_year=2000,current_year=2025)
25


# doc strings




def interest(principle,time,rate):
    """ <principle> is total loan amount
        <time> is tenure of the loan in years
        <rate> is rate of interest"""
    amount = (p*t*r)/100
    return amount



def interest(principle,time,rate=10):
    """ <principle> is total loan amount
        <time> is tenure of the loan in years
        <rate> is rate of interest defaulted to 10"""
    amount = (p*t*r)/100
    return amount

interest(100,2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    interest(100,2)
  File "<pyshell#29>", line 5, in interest
    amount = (p*t*r)/100
NameError: name 'p' is not defined



def interest(principle,time,rate=10):
    """ <principle> is total loan amount
        <time> is tenure of the loan in years
        <rate> is rate of interest defaulted to 10"""
    amount = (principle*time*rate)/100
    return amount

interest(100,2)
20.0


interest(time=3,principle=1000)
300.0




s=[1,0,2,9,4,8,5,8,6,7,1,0,2,6,6]

s
[1, 0, 2, 9, 4, 8, 5, 8, 6, 7, 1, 0, 2, 6, 6]
>>> 
>>> s.sort()
>>> s
[0, 0, 1, 1, 2, 2, 4, 5, 6, 6, 6, 7, 8, 8, 9]
>>> 
>>> 
>>> s=[1,0,2,9,4,8,5,8,6,7,1,0,2,6,6]
>>> s
[1, 0, 2, 9, 4, 8, 5, 8, 6, 7, 1, 0, 2, 6, 6]
>>> 
>>> s.sort(reverse=False)
>>> s
[0, 0, 1, 1, 2, 2, 4, 5, 6, 6, 6, 7, 8, 8, 9]
>>> 
>>> 
>>> 
>>> 
>>> s=[1,0,2,9,4,8,5,8,6,7,1,0,2,6,6]
>>> s
[1, 0, 2, 9, 4, 8, 5, 8, 6, 7, 1, 0, 2, 6, 6]


s.sort(reverse=True)
s
[9, 8, 8, 7, 6, 6, 6, 5, 4, 2, 2, 1, 1, 0, 0]





sum([1,2])
3

sum([1,2,3])
6

sum([1,2,3,4])
10

sum([1,2,3,4,5])
15

interest(100,3,9,10)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    interest(100,3,9,10)
TypeError: interest() takes from 2 to 3 positional arguments but 4 were given


