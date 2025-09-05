'''If you cross a 490meterlong street in 7 minutes, calculate your speed in meters per second. Print 
the answer without  any decimal point in it. Hint: Speed = Distance / Time'''

distance = 490  # in meters
time_minutes = 7  # in minutes
time = time_minutes * 60  # convert time to seconds
speed = distance / time  # speed in meters per second

print("Speed in meters per second is:", int(speed))