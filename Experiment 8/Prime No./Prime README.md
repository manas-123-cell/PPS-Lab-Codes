
## Problem Statement
Write a Python program to print all prime numbers within a given range (inclusive of both start and end values).

---

## Algorithm
1.Start

2.Input the values start and stop.

3.Set found = False.

4.Repeat for each number num from start to stop.

5.Check if num > 1.

6.Repeat for i from 2 to √num.

7.Check condition:

 If num % i == 0 → break (number is not prime).

8.If no divisor is found, then:

 Print num

  Set found = True.

9.After the loop, check found.

10.If found == False → Print "No primes".

11.Stop

---

## Flowchart
![Flowchart](
Prime.drawio.png)

---

## Execution
<p align="center">
  <img src="Prime.png" width="900">
</p>

