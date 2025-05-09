Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 5>6
False
>>> 6>7
False
>>> 
>>> 
>>> False and False
False
>>> 
>>> (5>6) and (6>5)
False
>>> 
>>> 
>>> (5>6) and (16>5)
False
>>> 
>>> 
>>> (65>6) and (6>51)
False
>>> 
>>> 
(65>6) and (66>51)
True


(65>6) and (66>51) and (55>1) and (64 >3) and (72 > 1) and (5 <4)
False


(65>6) and (66>51) and (55>1) and (64 >3) and (72 > 1) and (5 <42)
True


False or False
False

False or False or False or False or False or False or True
True


if (65>6) and (66>51) and (55>1) and (64 >3) and (72 > 1) and (5 <42):
    print("Executed becasue the final reulst is TRUE")

    
Executed becasue the final reulst is TRUE



if (65>6) and (66>51) and (55>1) and (64 >3) and (72 > 1) and (5 <4):
    print("Executed becasue the final reulst is TRUE")

    

