f=open("Waterlog.txt", "a")

import time
from pygame import mixer
mixer.init()

starttime1=time.time()
endtime=time.time()
while (endtime-starttime1)/3600 < 8:
    time.sleep(900)

    currenttime=time.time()
    if (currenttime-starttime1)/60 %45 >=0 and (currenttime-starttime1)/60 %45 <5:
        mixer.music.load("Water.mp3")
        mixer.music.set_volume(1)
        watertime1 = time.time()
        time_to_print = time.ctime(watertime1)
        mixer.music.play()
        time.sleep(2)
        amount = int(input("Enter amount of glasses u drank: "))
        f.write(f"Drank {amount} glasses of water at {time_to_print} \n")
        mixer.music.load("Eyeexercise.mp3")
        mixer.music.set_volume(1)
        mixer.music.play()
        time.sleep(2)
        mixer.music.load("Physicalexercise.mp3")
        mixer.music.set_volume(1)
        mixer.music.play()
        time.sleep(2)

    elif (currenttime-starttime1)/60 %30 >=0 and (currenttime-starttime1)/60 %30 <5:
        mixer.music.load("Water.mp3")
        mixer.music.set_volume(1)
        watertime1 = time.time()
        time_to_print = time.ctime(watertime1)
        mixer.music.play()
        time.sleep(2)
        amount = int(input("Enter amount of glasses u drank: "))
        f.write(f"Drank {amount} glasses of water at {time_to_print} \n")
        mixer.music.load("Eyeexercise.mp3")
        mixer.music.set_volume(1)
        mixer.music.play()
        time.sleep(2)

    else:
        mixer.music.load("Water.mp3")
        mixer.music.set_volume(1)
        watertime1 = time.time()
        time_to_print = time.ctime(watertime1)
        mixer.music.play()
        time.sleep(2)
        amount = int(input("Enter amount of glasses u drank: "))
        f.write(f"Drank {amount} glasses of water at {time_to_print} \n")


    endtime=time.time()



f.close()
time.sleep(15)
f=open("Waterlog.txt")
content= f.read()
print(content)
f.close()






