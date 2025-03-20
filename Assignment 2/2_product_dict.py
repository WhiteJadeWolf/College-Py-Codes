"""Write a program that repeatedly asks the user to enter product names and prices. 
Store all of these in a dictionary whose keys are the product names and whose values are the prices. 
When the user is done entering products and prices, allow them to repeatedly enter a 
product name and print the corresponding price or a message if the product is not in the dictionary."""

d={}
while True:
	choice=input("Do you want to add a product (y/n) ? ")
	if choice.lower()=='n':
		break
	elif choice.lower()=='y':
		pname=input("Enter product name : ")
		price=float(input("Enter product price : "))
		d[pname]=price
		print()
	else:
		print("Invalid choice\n")
		
while True :
	ch=input("Do you want to search for a product (y/n) ? ")
	if ch.lower()=='n':
		break
	elif ch.lower()=='y':
		prod=input("Enter product name : ")
		if prod not in d.keys():
			print("Product not found.")
		else:
			print("Price of",prod," = Rs.",d[prod])
		print()
	else:
		print("Invalid choice\n")