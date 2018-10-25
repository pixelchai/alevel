---
title: Structured Programming
layout: post
---

# Keywords

| Keyword              | Definition                                                   |
| -------------------- | ------------------------------------------------------------ |
| Syntax               | The rules that govern the tokens that make up a computer language. Can be defined using [EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form) |
| Selection            | Choosing actions to take (or statements to execute) based on criteria |
| Nesting              | When statements or expressions are inside the scope of other statements or expressions |
| Iteration            | Repeating a process, often with actions being taken in each step, and often with certain variables being incremented on each step |
| Definite Iteration   | Iteration whereby the number of times to be repeated is known prior to iteration. |
| Indefinite iteration | Iteration whereby the number of times to be repeated is dependent upon certain criteria being met |
| Loop                 | The actions of a process which repeats a certain number of times |
| Sequencing           | The order of the instructions within a program. If the instructions are executed in the wrong order, there may be undesired behaviour |

# Task 1

Here is some python code which demonstrates code which executes depending on certain conditions

```python
age=int(input("Age: "))
if age<16:
    print("You are too young to drive")
elif age>=16:
    print("You are old enough to ride a motorcycle")
elif age>=70:
    print("You need to requalify to drive a car")
else:
    print("You are able to drive in a license")
```

Not python, but many languages have `switch .. case` statements which can achieve the same functionality, but with different (cleaner in some cases) syntax.

In the example given above, rewriting as a `switch .. case` would be very verbose since you would have to hardcode every single case (that’s over 70 cases). Here is an example where rewriting as `switch .. case` actually is better:

```python
if x==5:
    # do specific thing
elif x==10:
    # do specific thing
elif x==13:
    # do specific thing
elif x==28:
    # do specific thing
elif x==234:
    # do specific thing
else:
    # do specific thing
```

This can be written in C# using a `switch .. case` statement like so:

```csharp
switch(x){
    case 5:
        // do specific thing
        break;
    case 10:
        // do specific thing
        break;
    case 13:
        // do specific thing
        break;
    case 28:
        // do specific thing
        break;
    case 234:
        // do specific thing
        break;
    default:
        // do specific thing
        break;
}
```

Its an alternative syntax - may be more intuitive or cleaner in some cases.