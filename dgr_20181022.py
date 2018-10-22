Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: def thing():
   ...:     print('Hello')
   ...:     print('Fun')
   ...:     

In [2]: thing()
Hello
Fun

In [3]: print('Zip')
Zip

In [4]: thing()
Hello
Fun

In [5]: big = max('Hello world')

In [6]: print(big)
w

In [7]: tiny = min('Hello world')

In [8]: print(tiny)
 

In [9]: big = max('Hello world')

In [10]: print(big)
w

In [11]: def max(inp):
    ...:     blah
    ...:     blah
    ...: for x in inp:
    ...:     blah
    ...:     blah
    ...:     
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-11-56dfb2eb93e7> in <module>()
      2     blah
      3     blah
----> 4 for x in inp:
      5     blah
      6     blah

NameError: name 'inp' is not defined

In [12]: print(float(99)/100)
0.99

In [13]: i = 42

In [14]: type(i)
Out[14]: int

In [15]: f = float(i)

In [16]: print(f)
42.0

In [17]: type(f)
Out[17]: float

In [18]: print(1 + 2 * float(3)/4 - 5)
-2.5

In [19]: 

In [19]: sval = '123'

In [20]: type(sval)
Out[20]: str

In [21]: print(sval + 1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-21-844c8fe77d11> in <module>()
----> 1 print(sval + 1)

TypeError: must be str, not int

In [22]: ival = int(sval)

In [23]: type(ival)
Out[23]: int

In [24]: print(ival + 1)
124

In [25]: nsv = 'hello bob'

In [26]: niv = int(nsv)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-26-023fdb204a1b> in <module>()
----> 1 niv = int(nsv)

ValueError: invalid literal for int() with base 10: 'hello bob'

In [27]: def print_lyrics():
    ...:     print("I'm a lumberjack, and I'm okay.")
    ...:     print('I sleep all night and I work all day.')
    ...:     

In [28]: x = 5

In [29]: print('Hello')
Hello

In [30]: def print_lyrics():
    ...:     print("I'm a lumberjack, and I'm okay.")
    ...:     print('I sleep all night and I work all day.')
    ...:     

In [31]: print('Yo')
Yo

In [32]: x = x + 2

In [33]: print(x)
7

In [34]: x = 5

In [35]: print('Hello')
Hello

In [36]: def print_lyrics():
    ...:     print("I'm a lumberjack, and I'm okay.")
    ...:     print('I sleep all night and I work all day.')
    ...:     

In [37]: print('Yo')
Yo

In [38]: print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.

In [39]: x = x + 2

In [40]: print(x)
7

In [41]: def greet(lang):
    ...:     if lang == 'es':
    ...:         print('Hola')
    ...:     elif lang == 'fr':
    ...:         print('Bonjour')
    ...:     else:
    ...:         print('Hello')
    ...:                 

In [42]: greet('en')
Hello

In [43]: greet('es')
Hola

In [44]: greet('fr')
Bonjour

In [45]: def greet():
    ...:     return "Hello"
    ...: 

In [46]: print(greet(), "Glenn")
Hello Glenn

In [47]: print(greet(), "Sally")
Hello Sally

In [48]: def greet(lang):
    ...:     if lang == 'es':
    ...:         return 'Hola'
    ...:     elif lang == 'fr':
    ...:         return 'Bonjour'
    ...:     else:
    ...:         return 'Hello'
    ...:     

In [49]: print(greet('en'),'Glenn')
Hello Glenn

In [50]: print(greet('es'),'Sally')
Hola Sally

In [51]: print(greet('fr'),'Michael')
Bonjour Michael

In [52]: big = max('Hello world')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-52-6ff389092c54> in <module>()
----> 1 big = max('Hello world')

<ipython-input-11-56dfb2eb93e7> in max(inp)
      1 def max(inp):
----> 2     blah
      3     blah
      4 for x in inp:
      5     blah

NameError: name 'blah' is not defined

In [53]: print(big)
w

In [54]: def max(inp):
    ...:     blah
    ...:     blah
    ...: for x in inp:
    ...:     blah
    ...:     blah
    ...: return 'w'
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-54-acd8615335de> in <module>()
      2     blah
      3     blah
----> 4 for x in inp:
      5     blah
      6     blah

NameError: name 'inp' is not defined

In [55]: def addtwo(a, b):
    ...:     added = a + b
    ...:     return added
    ...: 

In [56]: x = addtwo(3, 5)

In [57]: print(x)
8
