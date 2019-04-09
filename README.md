# OOPS Concept In Python

## Overview of OOPs Concept

 1. **Class :** A user-defined prototype for an object that defines a set of attributes that characterize any object of the class . The attributes are data members ( class variables and instance variable ) and methods.
 
 2. **Data member :** A class/instance variable that holds data associated with a class and its objects 
 
 3. **Instance variable :** A variable that is defined inside a method and belongs only to the current instance of a class 
 
 4. **Class variable :** Class variables are defined within a class but outside any of the class methods 
 
 6. **Instantiation :** The process of object creation is known as instantiation
 
 7. **Method :** A special kind of function that is defined in a class definition 
    ### Type of Methods
        * Instance Methods
        * Class Methods
        * Static Methods
 
 8. **Object :** A  instance of its class . An object comparises both datamembers and methods 

## Python Objects Oriented Concepts Explained with Examples

* Classes and Object
* Encapsulation
* Abstraction
* Inheritance
* Polymorphism

# Inheritance
* Creating a new class from existing class, so that the new classes will acquire all the features of the existing class

### Example

```
Class A:
	a = 1
	b = 2
	def method(cls):
		print cls.a
		print cls.b
class B:
	c = 3
	def method2(cls):
		print cls.c
```

# Polymorphism
>The word 'Polymorphism' came from two Greek words 'Poly' meaning 'many' and 'morphos' meaning 'forms'. Thus,Polymorphism represented the ability to assume several different forms. In Programming, if an object or method is exhibiting different behavior in different contexts,it is called Polymorphic nature

### Example - Below function is performing two different tasks,it said to exhibit polymorphism
```
#a function that exhibits polymorphism
def add(a,b):
	print a+b

#Call add() and pass integer	
add(5,10)
#Call add() and pass strings
add("Core","Python")
```


## Some important points

>**__init__()** --We can't declare variable in class,So we have written the variable inside a dunder method,i.e __init__(). This method is useful to initialize the variable. Hence, the name 'init'.



```
### Example
class Student(object):
	def __init__(self):
		self.name = 'Rishav'
		self.age = 25
		self.marks = 88
	def talk(self):
		print "Hi I am ",self.name
		print "My age is ",self.age
		print "My marks is ",self.marks
s1  = Student()
s1.talk()		
```