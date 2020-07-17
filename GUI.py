import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600


def test_function(entry):
    print("This is the entry:", entry)

#4813510a39138ffc206f9d67d68296a8
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City : %s \nConditions: %s \nTempreture (F):%s' %(name,desc,temp)
    except:
        final_str = 'Error loading the information'

    return final_str

def get_weather(city):
    weather_key = '4813510a39138ffc206f9d67d68296a8'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)

    weather = response.json()
    label['text'] = format_response(weather)


root = tk.Tk()
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH) #creating the height an width of the window
canvas.pack()   #.pack is needed to execute the tk commands

background_image = tk.PhotoImage(file = 'sunny.png')
background_image = tk.Label(root, image=background_image)
background_image.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg = 'red', bd=8, cursor='arrow')
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor='n')  #placing frame inside the window

entry = tk.Entry(frame, font=('Arial', 18))
entry.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text = "Search", font=('Arial', 18), command=lambda: get_weather(entry.get())) #placing buttons inside the frame
button.place(relx=0.7, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='red', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font = ('Arial', 25), anchor='nw', justify = 'left', bd=5)
label.place(relwidth=1, relheight=1)
print(tk.font.families())
root.mainloop()
