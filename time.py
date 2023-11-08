import time as time
tm=time.strftime('%H:%M:%S')

hours = int(time.strftime('%H'))
if hours < 12:
    print("Good morning Sir, time is",tm)
elif 12 < hours < 17:
    print("Good afternoon Akil sir time is",tm)
else:
    print("Good Evining Sir time is",tm)

