#Drink Water Notification Reminder for Windows only

from notifypy import Notify
import win32com.client as wincl
import time

def notificationSender():
    print("Sending Notification...")
    notification = Notify()
    notification.title = "Drink Water"
    notification.message = "Its time to drink water. Grab a glass or a bottle of water and drink it."
    notification.icon = "./drinkWaterNoti/water.png"
    notification.audio = "./drinkWaterNoti/water.wav"
    notification.send()
    print(f"Notification Sent!\n Mr. Microsoft David is speaking...")
    time.sleep(0.5)
    speaker_number = 0
    spk = wincl.Dispatch("SAPI.SpVoice")
    vcs = spk.GetVoices()
    spk.Voice 
    spk.Rate=1
    spk.SetVoice(vcs.Item(speaker_number))
    spk.Speak("Drink Water Champ!")
    print("Another notification will be sent in an hour.\n")
    
while True:                                 
    notificationSender()
    time.sleep(60*60)               # 60*60 = 3600 seconds = 1 hour, sends notification every hour until the program is closed