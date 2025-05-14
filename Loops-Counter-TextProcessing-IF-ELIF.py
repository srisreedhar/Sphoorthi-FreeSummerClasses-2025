Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# conditional iteration

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# add all the even numbers to a list, odd numbers to a seperate list

5/2
2.5
4/2
2.0

5%2
1
4%2
0

if 4%2 == 0:
    print("number is even")

    
number is even
if 5%2 == 0:
    print("number is even")

    

for num in numbers:
    if num%2 == 0:
        print("number is even",num)

        
number is even 0
number is even 2
number is even 4
number is even 6
number is even 8
number is even 10
number is even 12
number is even 14
number is even 16
number is even 18
number is even 20
number is even 22
number is even 24
number is even 26
number is even 28
number is even 30
number is even 32
number is even 34
number is even 36
number is even 38
number is even 40
number is even 42
number is even 44
number is even 46
number is even 48
number is even 50
number is even 52
number is even 54
number is even 56
number is even 58
number is even 60
number is even 62
number is even 64
number is even 66
number is even 68
number is even 70
number is even 72
number is even 74
number is even 76
number is even 78
number is even 80
number is even 82
number is even 84
number is even 86
number is even 88
number is even 90
number is even 92
number is even 94
number is even 96
number is even 98


even=[]
odd=[]

for num in numbers:
    if num%2 == 0:
        even.append(num)
    else:
        odd.append(num)

        
even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]


text = """Romeo.  Why,  such  is  love's  transgression. 
Griefs  of  mine  own  lie  heavy  in  my  breast, 
Which  thou  wilt  propagate,  to  have  it  prest 
With  more  of  thine ;  this  love  that  thou  hast  shown 
Doth  add  more  grief  to  too  much  of  mine  own. 
Love  is  a  smoke  rais'd  with  the  fume  of  sighs : 
Being  purg'd,  a  fire  sparkling  in  lovers'  eyes ; 
Being  vex'd,  a  sea  nourish'd  with  lovers'  tears ; 
What  is  it  else  ?  a  madness  most  discreet, 
A  choking  gall,  and  a  preserving  sweet. 
Farewell,  my  coz."""

text
"Romeo.  Why,  such  is  love's  transgression. \nGriefs  of  mine  own  lie  heavy  in  my  breast, \nWhich  thou  wilt  propagate,  to  have  it  prest \nWith  more  of  thine ;  this  love  that  thou  hast  shown \nDoth  add  more  grief  to  too  much  of  mine  own. \nLove  is  a  smoke  rais'd  with  the  fume  of  sighs : \nBeing  purg'd,  a  fire  sparkling  in  lovers'  eyes ; \nBeing  vex'd,  a  sea  nourish'd  with  lovers'  tears ; \nWhat  is  it  else  ?  a  madness  most  discreet, \nA  choking  gall,  and  a  preserving  sweet. \nFarewell,  my  coz."

# pull all the special characters in a list
# all the words with quote in one list


text.split()
['Romeo.', 'Why,', 'such', 'is', "love's", 'transgression.', 'Griefs', 'of', 'mine', 'own', 'lie', 'heavy', 'in', 'my', 'breast,', 'Which', 'thou', 'wilt', 'propagate,', 'to', 'have', 'it', 'prest', 'With', 'more', 'of', 'thine', ';', 'this', 'love', 'that', 'thou', 'hast', 'shown', 'Doth', 'add', 'more', 'grief', 'to', 'too', 'much', 'of', 'mine', 'own.', 'Love', 'is', 'a', 'smoke', "rais'd", 'with', 'the', 'fume', 'of', 'sighs', ':', 'Being', "purg'd,", 'a', 'fire', 'sparkling', 'in', "lovers'", 'eyes', ';', 'Being', "vex'd,", 'a', 'sea', "nourish'd", 'with', "lovers'", 'tears', ';', 'What', 'is', 'it', 'else', '?', 'a', 'madness', 'most', 'discreet,', 'A', 'choking', 'gall,', 'and', 'a', 'preserving', 'sweet.', 'Farewell,', 'my', 'coz.']



spl_chrs=[]
spl_words=[]


"nourish'd"
"nourish'd"

"'"  in "nourish'd"
True


# is not it a very great morning ?
# is't it a very great morning ?

'is not it a very great morning ?'
'is not it a very great morning ?'

'is't it a very great morning ?
SyntaxError: invalid syntax
"is't it a very great morning ?"
"is't it a very great morning ?"


spl_chrs=[]
spl_words=[]
SyntaxError: multiple statements found while compiling a single statement


spl_chrs=[]
spl_words=[]



for everyword in text.split():
    if everyword == ';':
        spl_chrs.append(everyword)
    elif everyword == ':':
        spl_chrs.append(everyword)
    elif everyword == '?':
        spl_chrs.append(everyword)
    elif everyword == '.':
        spl_chrs.append(everyword)
    elif "'" in everyword:
        spl_words.append(everyword)

        

spl_chrs
[';', ':', ';', ';', '?']

spl_words
["love's", "rais'd", "purg'd,", "lovers'", "vex'd,", "nourish'd", "lovers'"]




'?' in [';',':','?','.']
True
spl_chrs.clear()
spl_words.clear()

spl_chrs
[]
spl_words
[]


for everyword in text.split():
    if everyword in [';',':','?','.']:
        spl_chrs.append(everyword)
    elif "'" in everyword:
        spl_words.append(everyword)

        
spl_chrs
[';', ':', ';', ';', '?']
spl_words
["love's", "rais'd", "purg'd,", "lovers'", "vex'd,", "nourish'd", "lovers'"]




names = ['s400','s440','sri','apple','banana','amoxyline','bcomplex','satin']


# all the words starting with s should be in list and all the words starting with a should be in a list

names = ['s400','S440','Sri','apple','banana','Amoxyline','bcomplex','satin']




'sri'.startswith('s')
True

'sri'.endswith('s')
False

s=[]
a=[]

for name in names:
    if name.startswith('s'):
        s.append(name)
    elif name.startswith('a'):
        a.append(name)
    else:
        print("this name is exception",name)

        
this name is exception S440
this name is exception Sri
this name is exception banana
this name is exception Amoxyline
this name is exception bcomplex
s
['s400', 'satin']

a
['apple']


'Sri'.startswith('s')
False

'Sri'.lower().startswith('s')
True



s.clear()
a.clear()

for name in names:
    if name.lower().startswith('s'):
        s.append(name)
    elif name.lower().startswith('a'):
        a.append(name)
    else:
        print("this name is exception",name)

        
this name is exception banana
this name is exception bcomplex

s
['s400', 'S440', 'Sri', 'satin']
a
['apple', 'Amoxyline']





numbers = [1,1,1,1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,7,8,9]

numbers
[1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 9]

# how many 1's are there in the list



count=0
for each in [1,1,2,3,4]:
    print(count)

    
0
0
0
0
0


count
0

count = count+1
count
1

count = count+1
count
2

count = count+1

count
3


count = count+1
count
4



count=0
for each in [1,1,2,3,4]:
    count = count+1

    
count
5


for each in [1,1,2,3,4]:
    count = 0
    count = count+1

    
count
1


count=0
for each in [1,1,2,3,4]:
    if each == 1:
        count = count+1

        
count
2


numbers
[1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 9]

count_1 = 0

for everynum in numbers:
    if everynum == 1:
        count_1 = count_1 + 1

        
count_1
8



# find the sum of all the even numbers in the list below
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]



even_sum = 0
for everynum in numbers:
    print("checking condition for ",everynum)
    if everynum%2 == 0:
        print("even_sum total before adding ",everynum,"is ",even_sum)
        even_sum = even_sum + everynum
        print("even_sum total after adding ",everynum,"is ",even_sum)

        
checking condition for  0
even_sum total before adding  0 is  0
even_sum total after adding  0 is  0
checking condition for  1
checking condition for  2
even_sum total before adding  2 is  0
even_sum total after adding  2 is  2
checking condition for  3
checking condition for  4
even_sum total before adding  4 is  2
even_sum total after adding  4 is  6
checking condition for  5
checking condition for  6
even_sum total before adding  6 is  6
even_sum total after adding  6 is  12
checking condition for  7
checking condition for  8
even_sum total before adding  8 is  12
even_sum total after adding  8 is  20
checking condition for  9
checking condition for  10
even_sum total before adding  10 is  20
even_sum total after adding  10 is  30
checking condition for  11
checking condition for  12
even_sum total before adding  12 is  30
even_sum total after adding  12 is  42
checking condition for  13
checking condition for  14
even_sum total before adding  14 is  42
even_sum total after adding  14 is  56
checking condition for  15
checking condition for  16
even_sum total before adding  16 is  56
even_sum total after adding  16 is  72
checking condition for  17
checking condition for  18
even_sum total before adding  18 is  72
even_sum total after adding  18 is  90
checking condition for  19
checking condition for  20
even_sum total before adding  20 is  90
even_sum total after adding  20 is  110
checking condition for  21
checking condition for  22
even_sum total before adding  22 is  110
even_sum total after adding  22 is  132
checking condition for  23
checking condition for  24
even_sum total before adding  24 is  132
even_sum total after adding  24 is  156
checking condition for  25
checking condition for  26
even_sum total before adding  26 is  156
even_sum total after adding  26 is  182
checking condition for  27
checking condition for  28
even_sum total before adding  28 is  182
even_sum total after adding  28 is  210
checking condition for  29
checking condition for  30
even_sum total before adding  30 is  210
even_sum total after adding  30 is  240
checking condition for  31
checking condition for  32
even_sum total before adding  32 is  240
even_sum total after adding  32 is  272
checking condition for  33
checking condition for  34
even_sum total before adding  34 is  272
even_sum total after adding  34 is  306
checking condition for  35
checking condition for  36
even_sum total before adding  36 is  306
even_sum total after adding  36 is  342
checking condition for  37
checking condition for  38
even_sum total before adding  38 is  342
even_sum total after adding  38 is  380
checking condition for  39
checking condition for  40
even_sum total before adding  40 is  380
even_sum total after adding  40 is  420
checking condition for  41
checking condition for  42
even_sum total before adding  42 is  420
even_sum total after adding  42 is  462
checking condition for  43
checking condition for  44
even_sum total before adding  44 is  462
even_sum total after adding  44 is  506
checking condition for  45
checking condition for  46
even_sum total before adding  46 is  506
even_sum total after adding  46 is  552
checking condition for  47
checking condition for  48
even_sum total before adding  48 is  552
even_sum total after adding  48 is  600
checking condition for  49
checking condition for  50
even_sum total before adding  50 is  600
even_sum total after adding  50 is  650
checking condition for  51
checking condition for  52
even_sum total before adding  52 is  650
even_sum total after adding  52 is  702
checking condition for  53
checking condition for  54
even_sum total before adding  54 is  702
even_sum total after adding  54 is  756
checking condition for  55
checking condition for  56
even_sum total before adding  56 is  756
even_sum total after adding  56 is  812
checking condition for  57
checking condition for  58
even_sum total before adding  58 is  812
even_sum total after adding  58 is  870
checking condition for  59
checking condition for  60
even_sum total before adding  60 is  870
even_sum total after adding  60 is  930
checking condition for  61
checking condition for  62
even_sum total before adding  62 is  930
even_sum total after adding  62 is  992
checking condition for  63
checking condition for  64
even_sum total before adding  64 is  992
even_sum total after adding  64 is  1056
checking condition for  65
checking condition for  66
even_sum total before adding  66 is  1056
even_sum total after adding  66 is  1122
checking condition for  67
checking condition for  68
even_sum total before adding  68 is  1122
even_sum total after adding  68 is  1190
checking condition for  69
checking condition for  70
even_sum total before adding  70 is  1190
even_sum total after adding  70 is  1260
checking condition for  71
checking condition for  72
even_sum total before adding  72 is  1260
even_sum total after adding  72 is  1332
checking condition for  73
checking condition for  74
even_sum total before adding  74 is  1332
even_sum total after adding  74 is  1406
checking condition for  75
checking condition for  76
even_sum total before adding  76 is  1406
even_sum total after adding  76 is  1482
checking condition for  77
checking condition for  78
even_sum total before adding  78 is  1482
even_sum total after adding  78 is  1560
checking condition for  79
checking condition for  80
even_sum total before adding  80 is  1560
even_sum total after adding  80 is  1640
checking condition for  81
checking condition for  82
even_sum total before adding  82 is  1640
even_sum total after adding  82 is  1722
checking condition for  83
checking condition for  84
even_sum total before adding  84 is  1722
even_sum total after adding  84 is  1806
checking condition for  85
checking condition for  86
even_sum total before adding  86 is  1806
even_sum total after adding  86 is  1892
checking condition for  87
checking condition for  88
even_sum total before adding  88 is  1892
even_sum total after adding  88 is  1980
checking condition for  89
checking condition for  90
even_sum total before adding  90 is  1980
even_sum total after adding  90 is  2070
checking condition for  91
checking condition for  92
even_sum total before adding  92 is  2070
even_sum total after adding  92 is  2162
checking condition for  93
checking condition for  94
even_sum total before adding  94 is  2162
even_sum total after adding  94 is  2256
checking condition for  95
checking condition for  96
even_sum total before adding  96 is  2256
even_sum total after adding  96 is  2352
checking condition for  97
checking condition for  98
even_sum total before adding  98 is  2352
even_sum total after adding  98 is  2450
checking condition for  99


even_sum
2450

