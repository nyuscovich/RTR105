user@epk428-8:~$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 2
>>> x = 4
>>> print(x)
4
>>> print([1, 24, 76])
[1, 24, 76]
>>> print(['red', 'yellow', 'blue'])
['red', 'yellow', 'blue']
>>> print(['red', 24, 98.6])
['red', 24, 98.6]
>>> print([1, [5,6], 7])
[1, [5, 6], 7]
>>> print([])
[]
>>> for i in [5, 4, 3, 2, 1]:
...    print(i)
... print('Blastoff!')
  File "<stdin>", line 3
    print('Blastoff!')
        ^
SyntaxError: invalid syntax
>>> for i in [5, 4, 3, 2, 1]:
...    print(i)
... 
5
4
3
2
1
>>> print('Blastoff!')
Blastoff!
>>> friends = ['Joseph','Glenn','Sally']
>>> for friend in friends :
...    print('Happy New Year:', friend)
... 
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
>>> print('Done!')
Done!
>>> friends = ['Joseph','Glenn','Sally']
>>> print(friends[1])
Glenn
>>> fruit = 'Banana'
>>> fruit[0] = 'b'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> x = fruit.lower()
>>> print(x)
banana
>>> lotto = [2, 14, 26, 41, 63]
>>> print(lotto)
[2, 14, 26, 41, 63]
>>> lotto[2] = 28
>>> print(lotto)
[2, 14, 28, 41, 63]
>>> greet = 'Hello Bob'
>>> print(len(greet))
9
>>> x = [1, 2, 'joe', 99]
>>> print(len(x))
4
>>> print(range(4))
range(0, 4)
>>> friends = ['Joseph','Glenn','Sally']
>>> print(len(friends))
3
>>> print(range(len(friends)))
range(0, 3)
>>> friends = ['Joseph','Glenn','Sally']
>>> for friend in friends:
...    print('Happy New Year:', friend)
... 
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
>>> for i in range(len(friends)):
...    friend = friends[i]
...    print('Happy New Year:', friend)
... 
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
>>> friends = ['Joseph','Glenn','Sally']
>>> print(len(friends))
3
>>> print(range(len(friends)))
range(0, 3)
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
>>> print(a)
[1, 2, 3]
>>> t = [9, 41, 12, 3, 74, 15]
>>> t[1:3]
[41, 12]
>>> t[:4]
[9, 41, 12, 3]
>>> t[3:]
[3, 74, 15]
>>> t[:]
[9, 41, 12, 3, 74, 15]
>>> x = list()
>>> type(x)
<class 'list'>
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> stuff = list()
>>> stuff.append('book')
>>> stuff.append(99)
>>> print(stuff)
['book', 99]
>>> stuff.append('cookie')
>>> print(stuff)
['book', 99, 'cookie']
>>> some = [1, 9, 21, 10, 16]
>>> 9 in some
True
>>> 15 in some
False
>>> 20 not in some
True
>>> friends = ['Joseph','Glenn','Sally']
>>> friends.sort()
>>> print(friends)
['Glenn', 'Joseph', 'Sally']
>>> print(friends[1])
Joseph
>>> nums = [3, 41, 12, 9, 74, 15]
>>> print(len(nums))
6
>>> print(max(nums))
74
>>> print(min(nums))
3
>>> print(sum(nums))
154
>>> print(sum(nums)/len(nums))
25.666666666666668
>>> total = 0
>>> count = 0
>>> while True:
...   inp = input('Enter a number:')
...   if inp == 'done' : break
...   value = float(inp)
...   total = total + value
...   count = count + 1
... 
Enter a number:3
Enter a number:9
Enter a number:5
Enter a number:done
>>> average = total / count
>>> print('Average:', average)
Average: 5.666666666666667
>>> abc = 'With three words'
>>> stuff = abc.split()
>>> print(stuff)
['With', 'three', 'words']
>>> print(len(stuff))
3
>>> print(stuff[0])
With
>>> print(stuff)
['With', 'three', 'words']
>>> for w in stuff:
... print(w)
  File "<stdin>", line 2
    print(w)
        ^
IndentationError: expected an indented block
>>> print(stuff)
['With', 'three', 'words']
>>> for w in stuff:
...    print(w)
... 
With
three
words
>>> line = 'A lot       of spaces'
>>> etc = line.split()
>>> print(etc)
['A', 'lot', 'of', 'spaces']
>>> 
>>> line = 'first;second;third'
>>> thing = line.split()
>>> print(thing)
['first;second;third']
>>> print(len(thing))
1
>>> thing = line.split(';')
>>> print(thing)
['first', 'second', 'third']
>>> print(len(thing))
3
>>> exit()
user@epk428-8:~$ nano
user@epk428-8:~$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
...    line = line.rstrip()
...    if not line.startswith('From'): continue
...    words = line.split()
...    print(words[2])
... 
Sat
>>> line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
>>> words - line.split()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
>>> words = line.split()
>>> print(words)
['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
>>> words = line.split()
>>> email = words[1]
>>> 
>>> words = line.split()
>>> email = words[1]
>>> pieces = email.split('@')
>>> 
