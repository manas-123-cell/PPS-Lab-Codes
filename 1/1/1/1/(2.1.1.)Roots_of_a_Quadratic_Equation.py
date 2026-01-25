a,b,c=map(float,input().split())
d=(b*b)-(4*a*c)
sqrd=d**0.5
root1=(-b+sqrd)/(2*a)
root2=(-b-sqrd)/(2*a)
if(d>0):
  print(f"root1 = {root1:.2f}")
  print(f"root2 = {root2:.2f}")
elif(d==0):
  print(f"root1 = root2 = {root1:.2f}")
else:
  print(f"root1 = {root1.real:.2f}+{root1.imag:.2f}i")
  print(f"root2 = {root2.real:.2f}{root2.imag:.2f}i")
