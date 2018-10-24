Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: n = 5

In [2]: while n > 0 :
   ...:     print(n)
   ...:     n = n - 1
   ...: print('Blastoff!')
   ...: print(n)
   ...:     
5
4
3
2
1
Blastoff!
0

In [3]: n = 0

In [4]: while n > 0 :
   ...:     print('Lather')
   ...:     print('Rinse')
   ...: print('Dry off!')
   ...:     
Dry off!

In [5]: while True:
   ...:     line = input('>')
   ...:     if line == 'done':
   ...:         break
   ...:     print(line)
   ...: print('Done!')
   ...:     
>hello there
hello there
>finished
finished
>done
Done!

In [6]: while True:
   ...:     line = input('>')
   ...:     if line == 'done':
   ...:         break
   ...:     print(line)
   ...: print('Done!')
   ...:     
>hello there
hello there
>finished
finished
>done
Done!

In [7]: while True:
   ...:     line = input('>')
   ...:     if line == 'done':
   ...:         break
   ...:     print(line)
   ...: print('Done!')
   ...:     
>hello there
hello there
>finished
finished
>done
Done!

In [8]: while True:
   ...:     line = input('>')
   ...:     if line[0] == '#':
   ...:         continue
   ...:     if line == 'done':
   ...:         break
   ...:     print(line)
   ...: print('Done!')
   ...:     
>hello there
hello there
># don't print this
>print this!
print this!
>done
Done!

In [9]: while True:
   ...:     line = input('>')
   ...:     if line[0] == '#':
   ...:         continue
   ...:     if line == 'done':
   ...:         break
   ...:     print(line)
   ...: print('Done!')
   ...:     
>hello there
hello there
># don't print this
>print this!
print this!
>done
Done!

In [10]: for i in [5, 4, 3, 2, 1]:
    ...:     print(i)
    ...: print('Blastoff!')
    ...:     
5
4
3
2
1
Blastoff!

In [11]: friends = ['Jospeh','Glenn','Sally']

In [12]: for friend is friends:
  File "<ipython-input-12-c17218532861>", line 1
    for friend is friends:
                ^
SyntaxError: invalid syntax


In [13]: for friend is friends :
  File "<ipython-input-13-bc8568bb3f4f>", line 1
    for friend is friends :
                ^
SyntaxError: invalid syntax


In [14]: for friend in friends :
    ...:     print('Happy New Year:',friend)
    ...: print('Done!')
    ...:     
Happy New Year: Jospeh
Happy New Year: Glenn
Happy New Year: Sally
Done!

In [15]: i = 5

In [16]: print(i)
5

In [17]: i = 4

In [18]: print(i)
4

In [19]: i = 3

In [20]: print(i)
3

In [21]: i = 2

In [22]: print(i)
2

In [23]: i = 1

In [24]: print(i)
1

In [25]: print('Before')
Before

In [26]: for thing in [9, 41, 12, 3, 74, 15]:
    ...:     print(thing)
    ...: print('After')
    ...:     
9
41
12
3
74
15
After

In [27]: largest_so_far = -1

In [28]: print('Before', largest_so_far)
Before -1

In [29]: for the_num in [9, 41, 12, 3, 74, 15]:
    ...:     if the_num > largest_so_far:
    ...:         largest_so_far = the_num
    ...:     print(largest_so_far, the_num)
    ...:         
9 9
41 41
41 12
41 3
74 74
74 15

In [30]: print('After', largest_so_far)
After 74

In [31]: zork = 0

In [32]: print('Before', zork)
Before 0

In [33]: for thing in [9, 41, 12, 3, 74, 15]:
    ...:     zork = zork + 1
    ...:     print(zork, thing)
    ...: print('After', zork)
    ...:     
1 9
2 41
3 12
4 3
5 74
6 15
After 6

In [34]: zork = 0

In [35]: print('Before', zork)
Before 0

In [36]: for thing in [9, 41, 12, 3, 74, 15]:
    ...:     zork = zork + thing
    ...:     print(zork, thing)
    ...: print('After', zork)
    ...:     
9 9
50 41
62 12
65 3
139 74
154 15
After 154

In [37]: count = 0

In [38]: sum = 0

In [39]: print('Before', count, sum)
Before 0 0

In [40]: for value in [9, 41, 12, 3, 74, 15]:
    ...:     count = count + 1
    ...:     sum = sum + value
    ...:     print(count, sum, value)
    ...: print('After', count, sum, sum / count)
    ...:     
1 9 9
2 50 41
3 62 12
4 65 3
5 139 74
6 154 15
After 6 154 25.666666666666668

In [41]: print('Before')
Before

In [42]: for value in [9, 41, 12, 3, 74, 15]:
    ...:     if value > 20:
    ...:         print('Large number', value)
    ...: print('After')
    ...:         
Large number 41
Large number 74
After

In [43]: found = False

In [44]: print('Before', found)
Before False

In [45]: for value in [9, 41, 12, 3, 74, 15]:
    ...:     if value == 3:
    ...:         found = True
    ...:     print(found, value)
    ...: print('After', found)
    ...:         
False 9
False 41
False 12
True 3
True 74
True 15
After True

In [46]: largest_so_far = -1

In [47]: print('Before', largest_so_far)
Before -1

In [48]: for the_num in [9, 41, 12, 3, 74, 15]:
    ...:     if the_num > largest_so_far:
    ...:         largest_so_far = the_num
    ...:     print(largest_so_far, the_num)
    ...:         
9 9
41 41
41 12
41 3
74 74
74 15

In [49]: print('After', largest_so_far)
After 74

In [50]: 

In [50]: smallest_so_far = -1

In [51]: print('Before', smallest_so_far)
Before -1

In [52]: for the_num in [9, 41, 12, 3, 74, 15]:
    ...:     if the_num < smallest_so_far:
    ...:         smallest_so_far = the_num
    ...:     print(smallest_so_far, the_num)
    ...:         
-1 9
-1 41
-1 12
-1 3
-1 74
-1 15

In [53]: print('After', smallest_so_far)
After -1

In [54]: smallest = None

In [55]: print('Before')
Before

In [56]: for value in [9, 41, 12, 3, 74, 15]:
    ...:     if smallest is None:
    ...:         smallest = value
    ...:     elif value < smallest:
    ...:         smallest = value
    ...:     print(smallest, value)
    ...: print('After', smallest)
    ...:             
9 9
9 41
9 12
3 3
3 74
3 15
After 3
