from datetime import datetime
from playsound import playsound


alarmtime= input("Enter alarm time in HH:MM:SS like 09:14:59 AM \n") 

alarm_period=alarmtime[9:11].upper()
alarm_hour=alarmtime[0:2]
alarm_minute=alarmtime[3:5]
alarm_second=alarmtime[6:8]
print("Setting up alarm!")

while True:
    now=datetime.now()
    current_period = now.strftime("%p")
    current_hour=now.strftime("%H")
    current_minute=now.strftime("%M")
    current_second=now.strftime("%S")

    if alarm_period==current_period:
        if alarm_hour==current_hour:
            if alarm_minute==current_minute:
                if alarm_second== current_second:
                    print("Wakeuppppppppp")
                    playsound('alarm.mp3')
                    break
