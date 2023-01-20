def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

input_seconds = int(input("Enter the number of seconds between 0 and 86,399: "))
hours, minutes, seconds = convert_seconds(input_seconds)
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
 

gitstatus







	
