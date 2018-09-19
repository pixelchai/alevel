---
title: Class Notes
layout: post
---

# Computer Science Keywords

- mutable/immutable
- development cycle
- top down/cascading
- records - structs basically

# Extra

- constants may be used for conversion (conversion constants)
- naming conventions
- pointers

# Python Errors

### TypeError

Incorrect type

```python
a="sdhuisahd"
print(a+1)
```

```python
print(None*3)
```

### ZeroDivisionError

```python
print(1/0)
```

### SyntaxError

```python
print())
```

### KeyError

accessing a non-existent key in dictionary

```python
a={}
print(a['a'])
```

### UnicodeEncodeError

encoding error

```python
print('\x93'.encode('ascii'))
```

### NameError

when variable not defined

```python
print(a)
```

### AttributeError

when class does not have the attribute defined

```python
class NewType:
    pass
inst=NewType()
print(inst.a)
```



# User Defined Types

```python
class NewType:
    def __init__(self):
        self.a=2
inst=NewType()
inst.a=923
print(inst.a)
```

user defined types’ behaviour achieved with class instances

Here, the class ‘NewType’ is defined with attribute ‘a’ which is initialised to some value. Demonstration of instantiating that class and replacing attribute ‘a’ with some other variable + demonstration of attribute access.