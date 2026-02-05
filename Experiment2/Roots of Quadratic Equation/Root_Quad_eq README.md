
## Problem Statement
Write a program to find the roots of a quadratic equation, given its coefficients a, b, and c. Use the quadratic formula: 
(-b+-root(b**2-4ac))/2a.

---

## Algorithm
1. Start.  
2. Read the coefficients a, b, and c.
3. Calculate the discriminant using:-
   𝐷=𝑏^2−4ac.
4. If D > 0
   Compute:-
            𝑥1=(−𝑏+root𝐷)/2a and 𝑥2=(−𝑏−root𝐷)/2𝑎
			Display two real and distinct roots.
5. Else if D = 0
   Compute:-
   			𝑥=−𝑏/2𝑎
			Display equal real roots.

6. Else (D < 0)
   Compute:-
   			Real part = −𝑏/2𝑎
   			Imaginary part = root(-𝐷)/2a	
			Display complex roots.

7. Stop.
---

## Flowchart
![Flowchart](Roots_Quad_eq.drawio.png)

---

## Execution
<p align="center">
  <img src="Roots_Quad_exe.png" width="900">
</p>


