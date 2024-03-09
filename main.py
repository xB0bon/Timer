from tkinter import *
import time
import playsound

def update_window():
    time_now.set(time.strftime("%a, %d %b %Y\n%H:%M:%S")) # %a - dzien, %d - dzien tygodnia, %b - miesiac
    window.after(1000, update_window) # co 1 sekundę się powtarza


window = Tk()
window.title('Timer')
window.geometry('500x500')
window.config(bg='#131927')

# Napis: TIMER
Label(window, text='TIMER', font=('Consolas', 40, 'bold'), bg='#131927', fg='#55ed00').pack()

# Aktualny czas
time_now = StringVar(window)
Label(window, textvariable=time_now, fg='#59bd4f', bg='#131927').pack()

update_window()

window.mainloop()
