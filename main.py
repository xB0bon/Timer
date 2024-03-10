from tkinter import *
import time
from pygame import mixer

mixer.init()


def update_window():
    time_now.set(time.strftime("%a, %d %b %Y\n%H:%M:%S"))  # %a - dzien, %d - dzien tygodnia, %b - miesiac
    window.after(1000, update_window)  # co 1 sekundę się powtarza


def hour_add():
    hour_now = int(hour.get()) + 1
    if hour_now >= 0:
        if hour_now < 99:
            hour.set(str(hour_now).zfill(2))
        else:
            hour.set('00')
    else:
        hour.set('00')


def hour_subs():
    hour_now = int(hour.get()) - 1
    if hour_now >= 0:
        if hour_now >= 0:
            hour.set(str(hour_now).zfill(2))
    else:
        hour.set('00')


def minutes_add():
    minute_now = int(minutes.get()) + 1
    if minute_now >= 0:
        if minute_now < 60:
            minutes.set(str(minute_now).zfill(2))
        else:
            minutes.set('59')
    else:
        minutes.set('00')


def minutes_subs():
    minutes_now = int(minutes.get()) - 1
    if minutes_now >= 0:
        minutes.set(str(minutes_now).zfill(2))
    else:
        minutes.set('00')


def seconds_add():
    seconds_now = int(seconds.get()) + 1
    if seconds_now >= 0:
        if seconds_now < 60:
            seconds.set(str(seconds_now).zfill(2))
        else:
            seconds.set('59')
    else:
        seconds.set('00')


def seconds_subs():
    seconds_now = int(seconds.get()) - 1
    if seconds_now >= 0:
        seconds.set(str(seconds_now).zfill(2))
    else:
        seconds.set('00')


def start_timer():
    time.sleep(1)
    hours_clock = int(hour.get()) * 3600
    minutes_clock = int(minutes.get()) * 60
    seconds_clock = int(seconds.get())
    time1 = int(hours_clock) + int(minutes_clock) + int(seconds_clock)
    if time1 > 0:
        time1 = time1 - 1
        godziny = time1 // 3600
        reszta_po_godzinach = time1 % 3600
        minuty = reszta_po_godzinach // 60
        sekundy = reszta_po_godzinach % 60
        if len(str(godziny)) == 1:
            hour.set('0' + str(godziny))
        if len(str(minuty)) == 1:
            minutes.set('0' + str(minuty))
        if len(str(sekundy)) == 1:
            seconds.set('0' + str(sekundy))

        if len(str(godziny)) == 2:
            hour.set(str(godziny))
        if len(str(minuty)) == 2:
            minutes.set(str(minuty))
        if len(str(sekundy)) == 2:
            seconds.set(str(sekundy))

        if godziny == 0 and minuty == 0 and sekundy == 0:
            mixer.Sound('sound/sound.mp3').play()
            hour.set('00')
            minutes.set('00')
            seconds.set('00')
        window.after(10, start_timer)
    else:
        pass


window = Tk()
window.title('Timer')
window.geometry('500x500')
window.config(bg='#131927')
# obrazki

up_image = PhotoImage(file='img/up.png')
down_image = PhotoImage(file='img/down.png')

# Napis: TIMER
Label(window, text='TIMER', font=('Consolas', 40, 'bold'), bg='#131927', fg='#55ed00').pack()

# Aktualny czas
time_now = StringVar(window)
Label(window, textvariable=time_now, fg='#59bd4f', bg='#131927').pack()

# frame glowny
timer_main_frame = Frame(window, bg='#131927')
timer_main_frame.pack()

# przyciski

h_up = Button(timer_main_frame, image=up_image, bg='#131927', activebackground='#162334',
              relief='flat', borderwidth=0, border=0, command=hour_add)
h_down = Button(timer_main_frame, image=down_image, bg='#131927', activebackground='#162334',
                relief='flat', borderwidth=0, border=0, command=hour_subs)
h_up.grid(row=0, column=0)
h_down.grid(row=2, column=0)

m_up = Button(timer_main_frame, image=up_image, bg='#131927', activebackground='#162334', relief='flat', borderwidth=0,
              border=0, command=minutes_add)
m_down = Button(timer_main_frame, image=down_image, bg='#131927', activebackground='#162334', relief='flat',
                borderwidth=0, border=0, command=minutes_subs)
m_up.grid(row=0, column=2)
m_down.grid(row=2, column=2)

s_up = Button(timer_main_frame, image=up_image, bg='#131927', activebackground='#162334', relief='flat', borderwidth=0,
              border=0, command=seconds_add)
s_down = Button(timer_main_frame, image=down_image, bg='#131927', activebackground='#162334', relief='flat',
                borderwidth=0, border=0, command=seconds_subs)
s_up.grid(row=0, column=4)
s_down.grid(row=2, column=4)

# godziny
hour = StringVar(window)
hour.set('00')

hour_entry = Entry(timer_main_frame, bg='#131927', font=('consolas', 60, 'bold'),
                   width=2, fg='white', textvariable=hour)
hour_entry.grid(row=1, column=0)
Label(timer_main_frame, text='hours', bg='#131927', fg='white', font=('consolas', 15)).grid(row=1, column=1)

# minuty
minutes = StringVar(window)
minutes.set('00')

minute_entry = Entry(timer_main_frame, bg='#131927', font=('consolas', 60, 'bold'),
                     width=2, fg='white', textvariable=minutes)
minute_entry.grid(row=1, column=2)
Label(timer_main_frame, text='minutes', bg='#131927', fg='white', font=('consolas', 15)).grid(row=1, column=3)

# sekundy
seconds = StringVar(window)
seconds.set('00')

seconds_entry = Entry(timer_main_frame, bg='#131927', font=('consolas', 60, 'bold'),
                      width=2, fg='white', textvariable=seconds)
seconds_entry.grid(row=1, column=4)
Label(timer_main_frame, text='seconds', bg='#131927', fg='white', font=('consolas', 15)).grid(row=1, column=5)

start_button = Button(window, text='START', command=start_timer, bg='green', fg='white', width=5, font=('consolas', 20))
start_button.pack(pady=30, padx=10)
update_window()
window.mainloop()
