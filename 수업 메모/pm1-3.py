5Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

a=5
b=7

a+b
12

a-b
-2

a*b
35

a/b
0.7142857142857143

a**b
78125

a = 3.14
b = 2.2

a+b
5.34

a-b
0.94

a*b
6.908000000000001

a/b
1.4272727272727272

a**b
12.394962744865618

a = (1,2,3)
b = (4,5)

a+b
(1, 2, 3, 4, 5)

a-b
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a-b
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
c = [7,8]
d=[0,1,2]

a+c
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a+c
TypeError: can only concatenate tuple (not "list") to tuple
c+d
[7, 8, 0, 1, 2]



a = "hello"
b = "world"

a+b
'helloworld'
a-b
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a-b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
a*b
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'str'
a/b
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a/b
TypeError: unsupported operand type(s) for /: 'str' and 'str'


a=123
b=world
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    b=world
NameError: name 'world' is not defined
b="world"
a+b
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
a=123
b="world"

a+b
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
del(b)
a = 123
a+b
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a+b
NameError: name 'b' is not defined
a-b
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a-b
NameError: name 'b' is not defined
a*b
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a*b
NameError: name 'b' is not defined
a/b
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a/b
NameError: name 'b' is not defined
a=123
print(a)
123
a="hello"
print(a)
hello
b="world"
a+b
'helloworld'



a="c/c++"
b="python"
a+b
'c/c++python'
a,b
('c/c++', 'python')
print(a,b)
c/c++ python
print(a+b)
c/c++python



a,b,c=(1,2,3)
print(a,b,c)
1 2 3
d=a+b, a-b, a+b+c
print(d)
(3, -1, 6)



a=0
b=1
for i in range(0, 100);
SyntaxError: invalid syntax
a=0
b=1
for i in range(0, 100):
    
SyntaxError: multiple statements found while compiling a single statement
a=0
b=1
for i in range(0, 100):
    c=a+b
    print(c)
    a=b
    b=c

    
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
121393
196418
317811
514229
832040
1346269
2178309
3524578
5702887
9227465
14930352
24157817
39088169
63245986
102334155
165580141
267914296
433494437
701408733
1134903170
1836311903
2971215073
4807526976
7778742049
12586269025
20365011074
32951280099
53316291173
86267571272
139583862445
225851433717
365435296162
591286729879
956722026041
1548008755920
2504730781961
4052739537881
6557470319842
10610209857723
17167680177565
27777890035288
44945570212853
72723460248141
117669030460994
190392490709135
308061521170129
498454011879264
806515533049393
1304969544928657
2111485077978050
3416454622906707
5527939700884757
8944394323791464
14472334024676221
23416728348467685
37889062373143906
61305790721611591
99194853094755497
160500643816367088
259695496911122585
420196140727489673
679891637638612258
1100087778366101931
1779979416004714189
2880067194370816120
4660046610375530309
7540113804746346429
12200160415121876738
19740274219868223167
31940434634990099905
51680708854858323072
83621143489848422977
135301852344706746049
218922995834555169026
354224848179261915075
573147844013817084101
>>> 
>>> 
>>> 
>>> #include<iostream>
>>> 
>>> using namespace std;
SyntaxError: invalid syntax
>>> 
>>> s
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> 
>>> 
