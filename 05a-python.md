# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>**Tuples** are immutable sequences of elements.  They are like lists in that they are indexed by integers.  Tuples can be replaced/overwritten but the individual elements cannot be modified once a tuple is created.  They are often indicated by (), wheras lists are indicated by [].  Tuples will work as keys in dictionaries.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> While a list is an ordered collection of elements, a set is an unordered collection of unique elements.  Finding an element is faster in a set because it uses hash table indexing.  

***Set example***: finding the union and difference of 2 sets
```Python
>>>heroes={'luke','leia','han','lando','yoda','anakin'}
>>>villains={'emperor','anakin','jabba','lando'}
>>>confused=heroes & villains
>>>trustworthy=heroes-villains
```

***List example***: finding the union and difference of 2 lists

```Python
heroes=['luke','leia','han','lando','yoda','anakin']
villains=['emperor','anakin','jabba','lando']
confused, trustworthy=[], heroes
for hero in heroes:
  if hero in villains:
    confused.append(hero)
    trustworthy.remove(hero)
```
---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> **Lambda** allows functional programming, or passing functions as variables.  It can be used to quickly define a simple function.
**Example of using in the key argument to sorted:** The value of the key should be a function that takes a single argument and returns a key for sorting purposes.  

```Python
a={'red':650,'blue':475,'green':510,'yellow':570,'purple':400,'orange':590}
sorted(a, key=lambda color:a[color])
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare?  Also demonstrate set comprehensions and dictionary comprehensions.

> **List comprehensions** allow lists to be populated in a desired format using conditionals.  For example,

 ```Python
 eventriples=[x*3 for x in range(1,21) if x*3%2==0]
```

> gives a list of the even triples of 1-20.  

**Map equivalent**  

```Python
eventriples=[i for i in map(lamda x: 3*x, range(1,21)) if 3*i%2==0]
```

**Filter equivalent**  

```Python
eventriples=[3*i for i in filter(lambda x: x*3%2==0,range(1,21))]
```
Based on the above example, list comprehensions are more versatile because map and filter can only perform part of their functionality.  
**Set comprehensions**  
```Python
eventriples={x*3 for x in range(1,21) if x*3%2==0}
```

**Dictionary comprehensions**  
```Python
eventriples={x: x*3 for x in range(1,21) if x*3%2==0}
```


---
### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
