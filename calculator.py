print"SIMPLE CALCULATOR"
print"1=Add","2=Subtract","3=Divide","4=Multipy","5=Exit"
choice=raw_input("Choice")
first=int(raw_input("Enter Number"))
second=int(raw_input("Enter Number"))
if choice=="1":
	result=first+second
	print result,
elif choice=="2":
	result=first-second
	print result,
elif choice=="3":
	result=first/second
	print result,
elif choice=="4":
	result=first*second
	print result,
else:
	print"Exit"




	
	