sale_amount = int(input("Enter sales amount you sold in 2022:"))

associate = input("Enter s for seniors commision\nEnter j for juniors commission")

if sale_amount > 0 and sale_amount < 5000:
	if associate == 's':
	 print(f'Senior sales commssion this year is: {sale_amount*0.04}')
	if associate == 'j':
	 print(f'Junior sales commission this year is: {sale_amount*0.03}') 
	 
elif sale_amount > 5000 and sale_amount < 25000 :
	if associate == 's':
	 print (f'Senior sales commission this year is: {sale_amount*0.05}')
	if associate == 'j':
	 print (f'Junior sales commission this year is: {sale_amount*0.04}')
elif sale_amount > 25000 and sale_amount < 100000 :
	if associate == 's':
	 print (f'Senior sales commission this year is: {sale_amount*0.07}')
	if associate == 'j':
	 print (f'Junior sales commission this year is: {sale_amount*0.05}')
		

elif sale_amount > 100000 :
	if associate == 's':
	 print (f'Senior sales commission this year is: {sale_amount*0.1}')
	if associate == 'j':
	 print (f'Junior sales commission this year is: {sale_amount*0.07}')
	
	
else: 
	print ("Come to HR")
	
