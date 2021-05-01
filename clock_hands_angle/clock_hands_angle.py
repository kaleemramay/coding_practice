import sys

arguments = (sys.argv)
try:
    if arguments[1].find(":") == 1:
        time = arguments[1].split(":")
        hour    = int(time[0])
        minute  = int(time[1])
    else:
        hour    = int(arguments[1])
        minute  = int(arguments[2])
except Exception as ex:
    print("Invalid format \n Please provide time as \"3:15\" or \"3 15\"")

def get_angle(hour,minute):
    if minute == 0:
        minute_angle = 0
    else:    
        minute_angle = 360/minute
    if hour == 0:
        hour_angle = 0
    else:
        hour_angle = (360/12) * (hour + (minute/60))
    angle = abs(hour_angle - minute_angle)
    return angle

angle = get_angle(hour,minute)
print(angle)