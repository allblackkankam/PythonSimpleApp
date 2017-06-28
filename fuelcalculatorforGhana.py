print "Fuel Calculator"
print "1 Pertol","2 Diesel" , "3 Kerosene" , "4 LPG"
choice = raw_input("Choose: ")
amount = int(raw_input("How Much:GHc"  ))
def litre( a,b):
	print a/b, "Litres"
if choice == "1":
	litre(amount,3.850)
elif choice=="2":
	litre(amount,3.830)
elif choice == "3":
	litre(amount,3.673)
elif choice=="4":
	kg=amount/3.320
	print kg,"KG"
else:
	print "invalid"








