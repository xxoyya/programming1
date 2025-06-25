Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: C:/Users/sovel/OneDrive/바탕 화면/SSU/플밍1/pm0405.py ==================

=================== RESTART: C:/Users/sovel/OneDrive/바탕 화면/SSU/플밍1/pm0405.py ==================
a = 12345
b = a
c = a+4321
d = a+b
id(12345)
1899044467792
id(a)
1899044467952
id(b)
1899044467952
id(c)
1899044467824
id(d)
1899044462160
1899044462160
1899044462160

a = 1
b = 2.345
c = 7+5j
d = "Python is great language"
e = a, b, c, d
f = [a, b, c, d][:]
id(e)
1899050367504
id(a)
140721712941496
id(e[0])
140721712941496
id(c)
1899044467952
id(e[2])
1899044467952

from copy import copy
lst = [0, 3.14, "abcde"]
a, b, c = lst
d, e, f = copy(lst)
id(a)
140721712941464
id(lst[0])
140721712941464
ld(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    ld(c)
NameError: name 'ld' is not defined. Did you mean: 'd'?
NameError: name 'ld' is not defined. Did you mean: 'd'?
SyntaxError: invalid syntax
id(c)
1899050584848
id(lst[2])
1899050584848
id(d)
140721712941464
id(e)
1899044462544
id(f)
1899050584848

a = 1
b = 2
c = 3
d = a+b, b+c, c+a
id(a)
140721712941496
id(b)
140721712941528
id(c)
140721712941560
id(d[0])
140721712941560
id(d[1])
140721712941624
id(d[2])
140721712941592

a = 1
b = 2
c = 3
d = a, b, c
d = 1,2,3
e = a,b,c
f= d
d[0] == e[0]
True
d[0] is e[0]
True
d[0] != e[0]
False
f == d
True
f == e
True
f == e
True
f =d
f == d
True
f is d
True
f is e
False

a = 12345
b = 23456
c = 34567
d = 12345, 23456, 34567
e = a, b, c
f = d
f == d
True
f==e
True
f is d
True
f is e
False

a = 12345
b = 23456
c = 12345, 23456
d = a, b
e = (a==d[0])
f = (a is d[0])
e == f
True
e is f
True
g=(a != c[0])
h=(a is not c[0])
>>> g == h
False
>>> g is h
False

>>> a = 12345
>>> b = 0
>>> c=None
>>> b==c
False
>>> b is c
False
>>> b == False
True
>>> c == False
False
>>> type(b)
<class 'int'>
>>> type(c)
<class 'NoneType'>
>>> type(False)
<class 'bool'>

>>> a = {"id": 12345}
>>> a["id"]
12345
>>> a["name"]
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a["name"]
KeyError: 'name'
>>> a["name"]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a["name"]
KeyError: 'name'
>>> a.get("id")
12345
a.get("name")
\
a.get("name")
>>> a.get("name")
>>> print(a.get("name"))
None
>>> b={False:"false", None:"null"}
>>> b{
...     
SyntaxError: '{' was never closed
>>> b[False]
'false'
>>> b[None]
'null'
>>> c=[None, False, "False"]
>>> c[0]
>>> c[1]
False
>>> c[0]
>>> c[2]
'False'
