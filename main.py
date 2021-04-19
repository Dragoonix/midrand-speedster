speed_driver = int(input("Enter the speed you were driving"))
allowed_speed = 60
points = (speed_driver-allowed_speed)/5
if speed_driver <= allowed_speed :
    message = "ok"
elif speed_driver >= allowed_speed :
    message = str(points)
    if points > 12:
     message = "You are going to Jail !"
print(message)

