# wap that calculates the average of 6 subject marks

# define 6 subject marks

maths = input("Enter your maths marks     :")
science = input("Enter your science marks     :")
telugu = input("Enter your telugu marks     :")
hindi = input("Enter your hindi marks     :")
english = input("Enter your english marks     :")
social = input("Enter your social marks     :")

# create new variables with modified values 


maths_n = int(maths)
science_n = int(science)
social_n = int(social)
hindi_n = int(hindi)
telugu_n = int(telugu)
english_n = int(english)

total = maths_n + telugu_n + hindi_n + social_n + science_n + english_n



avg = total/6

print(avg)
