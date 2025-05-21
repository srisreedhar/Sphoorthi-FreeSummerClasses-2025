Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
listt =[]
>>> listt
[]
>>> 
>>> numbers = list()
>>> numbers
[]
>>> num_tuple = tuple()
>>> num_tuple
()
>>> 
>>> num_dict = dict()
>>> num_dict
{}
>>> 
>>> len('111111111')
9
>>> dir(1)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


type(dir(1))
<class 'list'>
open()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    open()
TypeError: open() missing required argument 'file' (pos 1)


text = open("D:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow\samplefile.txt")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    text = open("D:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow\samplefile.txt")
OSError: [Errno 22] Invalid argument: 'D:\\SphoorthiFreeClasses\\python\thisisatestfoldericreatednow\\samplefile.txt'

print("\n\n\n\n\n\n\n")








print("an apple\t\t\ta day")
an apple			a day



text = open("D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    text = open("D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt'


text = open("D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    text = open("D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt'

filepath="D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt.txt"

text=open(filepath)
text
<_io.TextIOWrapper name='D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt.txt' mode='r' encoding='cp1252'>


type(text)
<class '_io.TextIOWrapper'>

text.read()
'hei\nWhat a beautiful morning this is !!\n'
content=text.read()



content
''


text=open(filepath)
content=text.read()
content
'hei\nWhat a beautiful morning this is !!\n'

text
<_io.TextIOWrapper name='D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt.txt' mode='r' encoding='cp1252'>
text.close()
text
<_io.TextIOWrapper name='D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt.txt' mode='r' encoding='cp1252'>



text=open(filepath,'r')
text
<_io.TextIOWrapper name='D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt.txt' mode='r' encoding='cp1252'>

content=text.read()
content
'hei\nWhat a beautiful morning this is !!\n'
text.close()
text
<_io.TextIOWrapper name='D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt.txt' mode='r' encoding='cp1252'>



# write operation

text=open(filepath,'w')
text
<_io.TextIOWrapper name='D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt.txt' mode='w' encoding='cp1252'>

text.close()



text=open(filepath,'w')
text.write("Have a great day ahead")
22
len("Have a great day ahead")
22
text.close()



text=open(filepath,'w')
text.close()


text=open(filepath,'w')
text.write("Have a great day ahead")
22
text.close()



# appending new lines
text=open(filepath,'a')
text
<_io.TextIOWrapper name='D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt.txt' mode='a' encoding='cp1252'>
text.write("\n\neat well & sleep well")
23
text.close()

text = open("D:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow\samplefile.txt")
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    text = open("D:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow\samplefile.txt")
OSError: [Errno 22] Invalid argument: 'D:\\SphoorthiFreeClasses\\python\thisisatestfoldericreatednow\\samplefile.txt'




text = open(r"D:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow\samplefile.txt")
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    text = open(r"D:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow\samplefile.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'D:\\SphoorthiFreeClasses\\python\\thisisatestfoldericreatednow\\samplefile.txt'
text = open(r"D:\SphoorthiFreeClasses\python\thisisatestfoldericreatednow\samplefile.txt.txt")
text.close()



