Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> a = 10
>>> b = 1.56
>>> a * a
100
>>> b*b
2.4336
>>> type(a)
<type 'int'>
>>> type(b)
<type 'float'>
>>> c = 'A'
>>> c*c

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c*c
TypeError: can't multiply sequence by non-int of type 'str'
>>> type(c)
<type 'str'>
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print(__builtins__.__doc___)

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(__builtins__.__doc___)
AttributeError: 'module' object has no attribute '__doc___'
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> 
