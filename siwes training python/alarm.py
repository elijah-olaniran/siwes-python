#import time
#for i in range(6):
    #time.sleep(2)
    #print("\a")


#import time
#for i in range(8):
    #for i in range(5):
        #time.sleep(0.5)
        #print("\a")
    #time.sleep(3)
        


import datetime
import time
print("Olaniran Elijah Abidemi")
alarmA = input("What time should alarm wake you up? ")
alarmB = input("What minute? ")

while True:
    time = datetime.datetime.now()
    if alarmA == str(time.hour) and alarmB == str(time.minute):
        print("Stand up the time is past 12")
        break
    else:
        continue





