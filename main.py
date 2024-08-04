import tkinter
from tkinter import ttk
import datetime
import sv_ttk

# import local
import get_time
import get_weather

### TO DO
# Add icons https://github.com/metno/weathericons/tree/main/weather
# Add the rest of weather info for current
# Add weather forecast for next hours
# Add weather forecast for next days
# Add satelite image on bottom with current clouds
# Try to adopt the refreshing of up to be better (Don't call API every 1 second)


def enable_fullscreen():
    if root.attributes("-fullscreen"):
        root.attributes("-fullscreen", False)
    else:
        root.attributes("-fullscreen", True)

def update_time():
    last_sync = ""
    # check if there is network connection and load good function
    if get_time.check_network_connection():
        current_time = get_time.get_time_from_ntp()[0]
        current_date = get_time.get_time_from_ntp()[1]
        last_sync = f"Last sync at {get_time.get_time_from_ntp()[2]}"
        sync_time = last_sync
    else:
        current_time = get_time.get_time_from_datetime()[0]
        current_date = get_time.get_time_from_datetime()[1]
        sync_time = last_sync

    label_time.config(text=current_time)
    label_date.config(text=current_date)
    label_time_sync.config(text=sync_time)

    current_temp = get_weather.get_current_weather()
    current_temp = current_temp['temperature']['value']
    label_current_temp.config(text=current_temp)

    root.after(500, update_time)  # Update every 1 second

root = tkinter.Tk()
root.geometry("1280x720")

### TIME
label_time = ttk.Label(root, text="", font=("Roboto", 50))
label_time.grid(row=0, column=0, pady=(0, 0))

label_date = ttk.Label(root, text="", font=("Roboto", 25))
label_date.grid(row=1, column=0, pady=(0, 0))

label_time_sync = ttk.Label(root, text="", font=("Roboto", 10))
label_time_sync.grid(row=2, column=0)

button = ttk.Button(root, text="Click me!", command=enable_fullscreen)
button.grid(row=3, column=0)

### TEMP

label_current_temp = ttk.Label(root, text="", font=("Roboto", 10))
label_current_temp.grid(row=0, column=1)


# This is where the magic happens
#sv_ttk.set_theme("dark")

update_time()

root.mainloop()

