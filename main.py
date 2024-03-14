from tkinter import *
import time
from pygame import mixer
import threading
import os
import json

mixer.init()
try:
    with open('data.json', 'r') as json_file:
        loaded_data = json.load(json_file)

    want_shutdown = loaded_data['want_shutdown']
    want_clean = loaded_data['want_clean']
except Exception as e:
    print(e)
    want_shutdown = False
    want_clean = False

run = None
time1 = 0


def settings():
    global want_shutdown
    global want_clean

    def b_shut():
        global want_shutdown
        global want_clean
        if not want_shutdown:
            shutdown_button.config(image=on_image)
            want_shutdown = True
            loaded_data['want_shutdown'] = True
        else:
            shutdown_button.config(image=off_image)
            want_shutdown = False
            loaded_data['want_shutdown'] = False
        data = {'want_clean': want_clean,
                'want_shutdown': want_shutdown}
        with open('data.json', 'w') as new_json:
            json.dump(data, new_json)

    def b_clean():
        global want_clean
        global want_shutdown
        if not want_clean:
            clean_button.config(image=on_image)
            want_clean = True
            loaded_data['want_clean'] = True
        else:
            clean_button.config(image=off_image)
            want_clean = False
            loaded_data['want_clean'] = False
        data = {'want_clean': want_clean,
                'want_shutdown': want_shutdown}
        with open('data.json', 'w') as new_json:
            json.dump(data, new_json)

    settings = Toplevel()
    settings.title("settings")
    settings.geometry("300x400")
    settings.resizable(False, False)
    settings.grab_set()  # uniemozliwia edycje 1 okna

    Label(settings, text="Settings:", font=('arial', 20)).grid(row=0, column=0, columnspan=1)
    Label(settings, text="What after time?", font=('arial', 10)).grid(row=1, column=0, columnspan=1)
    Label(settings, text="computer shutdown", font=('arial', 15)).grid(row=2, column=0, padx=5, pady=5)
    on_image = PhotoImage(file="img/on-button.png")
    off_image = PhotoImage(file="img/off-button.png")
    shutdown_button = Button(settings, image=off_image, borderwidth=0, highlightthickness=0, command=b_shut)
    shutdown_button.grid(row=2, column=1, padx=5, pady=5)
    if want_shutdown:
        shutdown_button.config(image=on_image)
    if not want_shutdown:
        shutdown_button.config(image=off_image)

    Label(settings, text="cleaning temporary files", font=('arial', 13)).grid(row=3, column=0, padx=5, pady=5)
    clean_button = Button(settings, image=off_image, borderwidth=0, highlightthickness=0, command=b_clean)
    clean_button.grid(row=3, column=1, padx=5, pady=5)
    if want_clean:
        clean_button.config(image=on_image)
    if not want_clean:
        clean_button.config(image=off_image)
    settings.mainloop()


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


def start():
    if start_button['state'] == 'normal':
        global time1, minutes_clock, seconds_clock
        hours_clock = int(hour.get()[-2:]) * 3600
        if int(minutes.get()[-2:]) < 60:
            minutes_clock = int(minutes.get()[-2:]) * 60
        if int(minutes.get()[-2:]) > 59:
            minutes.set('59')
            minutes_clock = int(minutes.get()[-2:]) * 60
        if int(seconds.get()[-2:]) < 60:
            seconds_clock = int(seconds.get()[-2:])
        if int(seconds.get()[-2:]) > 59:
            seconds.set('59')
            seconds_clock = int(seconds.get()[-2:])

        time1 = int(hours_clock) + int(minutes_clock) + int(seconds_clock)
        if time1 != 0:
            global run
            if not run:
                run = True
            else:
                run = False
            start_timer_thread()
        else:
            pass


def start_timer_thread():
    threading.Thread(target=start_timer).start()


def buttonsstate():
    h_up.config(state='normal')
    h_down.config(state='normal')
    s_up.config(state='normal')
    s_down.config(state='normal')
    m_up.config(state='normal')
    m_down.config(state='normal')
    reset_button.config(state='normal')
def clean():
    try:
        os.system("del /q %temp%\*")
        os.system("del /q C:\Windows\Temp\*")
        os.system("rd /s /q C:\$Recycle.Bin")
        os.system("del /q /s /f C:\Windows\Logs\*")
    except Exception as e:
        print(e)

def start_timer():
    global run
    global time1
    start_button.config(state='disabled')

    if run:
        while run and time1 > 0:
            if time1 != 0:
                h_up.config(state='disabled')
                h_down.config(state='disabled')
                s_up.config(state='disabled')
                s_down.config(state='disabled')
                m_up.config(state='disabled')
                m_down.config(state='disabled')

                reset_button.config(state='disabled')
                start_button.config(bg='red', text='PAUSE')
                time.sleep(1)
                start_button.config(state='normal')
                time1 = time1 - 1
                godziny = time1 // 3600
                reszta_po_godzinach = time1 % 3600
                minuty = reszta_po_godzinach // 60
                sekundy = reszta_po_godzinach % 60
                if len(str(godziny)) == 1 and run:
                    hour.set('0' + str(godziny))
                if len(str(minuty)) == 1 and run:
                    minutes.set('0' + str(minuty))
                if len(str(sekundy)) == 1 and run:
                    seconds.set('0' + str(sekundy))

                if len(str(godziny)) == 2 and run:
                    hour.set(str(godziny))
                if len(str(minuty)) == 2 and run:
                    minutes.set(str(minuty))
                if len(str(sekundy)) == 2 and run:
                    seconds.set(str(sekundy))

                if godziny == 0 and minuty == 0 and sekundy == 0 and run:
                    start_button.config(text='START', bg='green')
                    alarm = mixer.Sound('sound/sound.mp3')
                    alarm.play()
                    hour.set('00')
                    minutes.set('00')
                    seconds.set('00')
                    buttonsstate()
                    if want_shutdown:
                        os.system("shutdown /s /t 15")
                    if want_clean:
                        clean()

            else:
                start_button.config(state='normal')
    else:
        buttonsstate()
        start_button.config(text='START', bg='green')

        pass
    run = False
    start_button.config(state='disabled')
    time.sleep(1.5)
    start_button.config(state='normal')


def on_closing():
    global run
    run = False
    window.destroy()


def reset():
    minutes.set('00')
    hour.set('00')
    seconds.set('00')


window = Tk()
window.title('Timer')
window.geometry('500x500')
window.config(bg='#131927')
window.bind('<Return>', lambda event: start())
window.resizable(False, False)
# obrazki

up_image = PhotoImage(file='img/up.png')
down_image = PhotoImage(file='img/down.png')

# Napis: TIMER
Label(window, text='TIMER', font=('Consolas', 40, 'bold'), bg='#131927', fg='#55ed00').pack(anchor=CENTER)
settings = Button(window, text='setings', bg='white', command=settings)
settings.place(x=440, y='20')

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

start_button = Button(window, text='START', command=start, bg='green', fg='white', width=5,
                      font=('consolas', 20))
start_button.pack(pady=25, padx=10)
reset_button = Button(window, text='RESET', command=reset, bg='#7c4e4a', fg='white', width=5,
                      font=('consolas', 20))
reset_button.pack()
window.mainloop()
