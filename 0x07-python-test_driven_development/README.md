# 0x07. Python - Test-driven development

## Write tests for all functions in tests folder

### 0. Integers addition

Write a function that adds 2 integers.

### Prototype: def add_integer(a, b=98):
- a and b must be integers or floats, otherwise raise a TypeError exception	with the message a must be an integer or b must be an integer
- a and b must be first casted to integers if they are float
- Returns an integer: the addition of a and b
- You are not allowed to import any module

**0-main.py**

```
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
```
**Expected Output**

```
3
98
100
98
b must be an integer
a must be an integer
```

**Run tests**
 
`python3 -m doctest -v ./tests/0-add_integer.txt | tail -2`