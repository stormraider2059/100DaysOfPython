import time as tm
getTime=tm.strftime("%H:%M:%S")
print("Your current time is: ",getTime)
hour=int(tm.strftime("%H"))

if hour>=0 and hour<12:
    print("Good Morning!")
elif hour>=12 and hour<16:
    print("Good Afternoon!")
elif hour>=16 and hour<20:
    print("Good Evening!")
else:
    print("Good Night!")