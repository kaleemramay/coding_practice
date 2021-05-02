import sys

arguments = (sys.argv)
try:
    if arguments[1].find(":") > 0:
        time = arguments[1].split(":")
        hour    = int(time[0])
        minute  = int(time[1])
    else:
        hour    = int(arguments[1])
        minute  = int(arguments[2])
    if minute > 60 or hour > 12:
        raise Exception
except Exception as ex:
    print("Invalid format \n Please provide time as \"3:15\" or \"3 15\"")
    exit

def get_angle(hour,minute):
    if minute == 0:
        min_pos = 0
        min_bump = 0
    else:    
        min_pos = 360 * (minute / 60)
        min_bump = (360/12) * (minute/60)
    if hour == 12 or hour == 0:
        hour_pos = 0 + min_bump
    else:
        hour_pos = (360/12) * hour + min_bump
    angle = abs(hour_pos - min_pos)
    return angle
angle = get_angle(hour,minute)
print(angle)