import tkinter
from tkinter import ttk
import datetime
import sv_ttk
from PIL import Image, ImageTk

# import local
import get_time
import get_weather

### TO DO
# Add evertyhing into frames and add 1 px border arround
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
    # refresh after 0.5 seconds
    root.after(100, update_time)

image_path = ""

def update_weather():
    current_weather = get_weather.get_current_weather()
    current_icon = current_weather['symbolCode']['next1Hour']
    current_temp = current_weather['temperature']['value']
    current_rain = current_weather['precipitation']['value']
    current_wind_speed = current_weather['wind']['speed']
    current_wind_speed = current_wind_speed * 3.6
    # image icon
    img = ImageTk.PhotoImage(Image.open(f"./weather_icons/{current_icon}.png"))
    label_current_icon.config(image=img)
    label_current_icon.image = img

    # the rest of current data
    label_current_temp.config(text=f"Temp: {current_temp}ºC")
    label_current_precipitation.config(text=f"Rain: {current_rain} mm")
    label_current_wind.config(text=f"Wind: {current_wind_speed} km/h")
    # refresh after 10 minutes
    root.after(600000, update_time)

root = tkinter.Tk()
root.geometry("1280x720")

#region TIME
label_time = ttk.Label(root, text="", font=("Roboto", 50))
label_time.grid(row=0, column=0, pady=(0, 0))

label_date = ttk.Label(root, text="", font=("Roboto", 25))
label_date.grid(row=1, column=0, pady=(0, 0))

label_time_sync = ttk.Label(root, text="", font=("Roboto", 10))
label_time_sync.grid(row=2, column=0)

button = ttk.Button(root, text="Click me!", command=enable_fullscreen)
button.grid(row=3, column=0)
#endregion

#region WEATHER
label_current_icon = ttk.Label(root, image='')
label_current_icon.grid(row=0, column=2)

label_current_temp = ttk.Label(root, text="", font=("Roboto", 10))
label_current_temp.grid(row=1, column=1)

label_current_precipitation = ttk.Label(root, text="", font=("Roboto", 10))
label_current_precipitation.grid(row=2, column=1)

label_current_wind = ttk.Label(root, text="", font=("Roboto", 10))
label_current_wind.grid(row=3, column=1)
#endregion

# Change theme to dark
sv_ttk.set_theme("dark")

# Do an updates in displayed data
update_time()
update_weather()

root.mainloop()