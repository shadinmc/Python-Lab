"""Aim:Plot the following functions using python
  1.y=x
  2.y=x^2+1
  3.y=x^3+5
  4.y=sin(x)
  5.y=e^x"""


import matplotlib.pyplot as plt
import numpy as np
def function_1(x):
return x
def function_2(x):
return x**2+1
def function_3(x):
return x**3+5
def function_4(x):
return np.sin(x)
def function_5(x):
return np.exp(x)
def menu():
print("Select a function to plot:")
print("1. y=x")
print("2.x=y^2+1")
print("3.x=y^3+5")
print("4. y=sin(x)")
print("5. y=e^x")
print("6. Enter '0' to quit")
while True:
menu()
choice=int(input("Enter your choice"))
if choice==0:
break
if choice==1:
x=np.linspace(-10,10,1000)
y=function_1(x)
plt.plot(x,y)
plt.title("y=x")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["y=x"])

plt.show()
elif choice==2:
y=np.linspace(-10,10,1000)
x=function_2(x)
plt.plot(x,y)
plt.title("x=y^2+1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["x=y^2+1"])
plt.show()
elif choice==3:
y=np.linspace(-10,10,1000)
x=function_3(x)
plt.plot(x,y)
plt.title("x=y^3+5")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["x=y^3+5"])
plt.show()
elif choice==4:
x=np.linspace(-10,10,1000)
y=function_4(x)
plt.plot(x,y)
plt.title("y=sin(x)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["y=sin(x)"])
plt.show()
elif choice==5:
x=np.linspace(-10,10,1000)
y=function_5(x)
plt.plot(x,y)
plt.title("y=e^x")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(["y=e^x"])
plt.show()
elif choice==6:
print("Exited succesfully..... :) ")
else:
print("Invalid choice")
