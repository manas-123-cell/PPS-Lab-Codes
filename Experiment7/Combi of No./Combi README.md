
## Problem Statement
Write a Python program to accept three digits and print all possible 3-digit combinations that can be formed using those three digits. Each digit should be used exactly once in each combination.

---

## Algorithm
1. Start
2. Input three values a, b, c.
3. Store them in a list:
      digits = [a, b, c]
4. Initialize loop variable i from 0 to 2.
5. Inside that, initialize loop variable j from 0 to 2.
6. Inside that, initialize loop variable k from 0 to 2.
7. Check condition:
    if (i ≠ j AND i ≠ k AND j ≠ k)
       If true → Print
          digits[i] + digits[j] + digits[k]
8. Repeat until all loops finish.
9. Stop
---

## Flowchart
![Flowchart](
Combi.drawio.png)

---

## Execution
<p align="center">
  <img src="Combi.png" width="900">
</p>


