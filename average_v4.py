# wap that calculates the average of 6 subject marks

# define 6 subject marks

maths = input("Enter your maths marks     :")
maths = int(maths)

science = input("Enter your science marks     :")
science = int(science)

telugu = input("Enter your telugu marks     :")
telugu = int(telugu)

hindi = input("Enter your hindi marks     :")
hindi = int(hindi)

english = input("Enter your english marks     :")
english = int(english)

social = input("Enter your social marks     :")
social = int(social)

# create new variables with modified values 



total = maths+ telugu + hindi + social + science + english



avg = total/6

print(avg)
