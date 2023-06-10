calculator.py
def operation(x,y):
	x=0
	while(x==0):
		case=int(input("enter 1 for additon\nenter 2 for subtraction\n enter 3 for multiplication\n enter 4 for division\n enter 5 for exit"))
		if case==1:
		      print(x+y)
		elif case==2:
		      print(x-y)
		elif case==3:
		      print(x*y)
		elif case==4:
		      print(x//y)
		elif case==5:
		      print("EXIT!!!")
		      x=1
		else:
		      print("Invalid Choice")      	
     
x=int(input("Enter the value of x"))
y=int(input("Enter the value of y"))
operation(x,y)      
                        
