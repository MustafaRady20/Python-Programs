# importing winsound to load the sound of the alarm
# you can use playsound library instead  of winsound but first you have to install it using pip install playsound

import winsound
from datetime import datetime

alarm_time = input("Enter the time of Alarm to be set:HH:MM:SS AM|PM\n")
alarm_hours = alarm_time[0:2]
alarm_minutes = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[8:10]

print("Setting up alarm..")

while True:
    current_time = datetime.now()

    current_hours = current_time.strftime("%I")
    current_minutes = current_time.strftime("%M")
    current_seconds = current_time.strftime("%S")
    current_period = current_time.strftime("%p")

    if current_period == alarm_period:
        if current_hours == alarm_hours:
            if current_minutes == alarm_minutes:
                if current_seconds == alarm_seconds:
                    print("Time to Wake Up!!!")
                    winsound.PlaySound(
                        "Alarm sound/tense-piano-cinematic-111052.mp3", winsound.SND_FILENAME)
