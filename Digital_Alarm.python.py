from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%y")
        print(now)
        if now == set_alarm_timer:
            print("Please Wake Up!")
            winsound.playsound("Sound.wav" , winsound.SND_ASYNC)
            break
def actual_time():
    set_alarm_timer = f"{hour.get()}: {main.get()}: {sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()
clock.title("ShaliniS Alarm Clock ")
clock.geometry("600x400")
time_formate = Label(clock ,text = "set time in 24 hour formate", fg = "white" , bg = "red" , font = "Arial")
addTime = Label(clock,text = "Hour Min sec", font = 80).place(x = 150)


hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock,textvariable = hour, bg = "green" , width = 25).place(x = 110, y =30)
minTime = Entry(clock,textvariable = min, bg = "green" , width = 25).place(x = 110, y =30)
secTime = Entry(clock,textvariable = sec, bg = "green" , width = 25).place(x = 110, y =30)

submit = Button(clock, text = "set Alarm" , fg = "red" , width = 10 , command = actual_time).place(x = 1)
clock.mainloop()
