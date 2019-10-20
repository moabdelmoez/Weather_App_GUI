import tkinter as tk
from tkinter import font
import requests

height = 400
width = 500

def test_function(entry):
    print("This is the entry:", entry)

def get_weather(city):
    weather_key = 'XXXXX'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key,
              'q': city,
              'units': 'metric'}
    response = requests.get(url,params=params)
    weather = response.json()

    label['text'] = format_response(weather)

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final =  'City: %s \nConditions: %s\nTemp: %s'% (name, description, temp)
    except:
        final = 'Please try again'

    return final

#application window
root = tk.Tk()

#set the canvas, as a container to all buttons and stuff
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

#set the background image, it works only with png files
background_image = tk.PhotoImage(file='japan_landscape_illustration-01.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#set the top frame
frame = tk.Frame(root, bg='#42cbf5', bd=5)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

#set entry
entry = tk.Entry(frame, font=('Courier', 20))
# entry.pack(side='left')
# entry.grid(row=0, column=2)
entry.place(relheight=1, relwidth=0.65)

#set button
button = tk.Button(frame, text="Get Weather", font=('Courier', 11), command=lambda: get_weather(entry.get()))
# button.pack(side='left', fill='both', expand=True)
# button.grid(row=0, column=0)
button.place(relx=0.7, relheight=1, relwidth=0.3)

#set the lower frame
lower_frame = tk.Frame(root, bg='#42cbf5', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor='n')

#set label
label = tk.Label(lower_frame, font=('Courier', 20), anchor='nw', justify='left', bd=4)
# label.pack(side='top')
# label.grid(row=0, column=1)
label.place(relheight=1, relwidth=1)

#event loop
root.mainloop()
