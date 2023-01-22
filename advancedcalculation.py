def convert_seconds(seconds):
	
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

input_seconds = int(input("Enter the number of seconds since the beginning of new year: "))
hours, minutes, seconds = convert_seconds(input_seconds)
print(f" {hours} hours, {minutes} minutes, {seconds} seconds after 2022.")


def total_population():
	
	print('Total population was 34205119') 
	population = int(34205119)
	flapjack_eaten =  ((population + 350) ** 2 - 12 // 50) ** 0.2
	
	print(f'number of flapjack eaten is {flapjack_eaten}')

total_population()
