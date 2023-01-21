def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

input_seconds = int(input("Enter the number of seconds since 2022: "))
hours, minutes, seconds = convert_seconds(input_seconds)
print(f"{hours} hours, {minutes} minutes, {seconds} seconds , after the start of 2022.")

def population():
	deaths = input_seconds //13
	births = input_seconds //7
	immigrants = input_seconds// 35
	
	print(f'{births + deaths - immigrants} is the population')
	
population() 
 
