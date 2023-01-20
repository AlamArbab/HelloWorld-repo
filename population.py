days = 19
minutes = 15
seconds = 20

total_seconds = (days * 24 * 60 * 60) + (minutes * 60) + seconds
print(total_seconds)

def calculate_poppulation():
	
	
	birth = total_seconds//7
	death = total_seconds //13
	immigrants = total_seconds//35
	
	print(f'population is {birth + death - immigrants}')
	
		
calculate_poppulation()
