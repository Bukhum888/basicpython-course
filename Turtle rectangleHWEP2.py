Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> def Rectangle():
...     for i in range (4):
...         tao.forward(100)
...         tao.left(90)
... 
...         
>>> def Go(x,y):
...     tao.penup()
...     tao.goto(x,y)
...     tao.pendown()
... 
...     
>>> Go (200,200)
>>> Rectangle()
>>> Go (-200,-200)
>>> Rectangle()
>>> Go (300+200)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    Go (300+200)
TypeError: Go() missing 1 required positional argument: 'y'
>>> Go (300,300)
>>> Go (-300,200)
>>> def Circle ():
...     for i in range (10)
...     
SyntaxError: incomplete input
>>> def Circle ():
...     for i in range(10):
...         tao.circle(50)
...         tao.left(36)
... 
...         
>>> Circle()
>>> Go (100,100)
>>> Circle()
