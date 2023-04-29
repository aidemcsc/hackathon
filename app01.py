import requests
from bs4 import BeautifulSoup
import time
import tkinter as tk 
from tkinter import Text, filedialog
import os


URL = 'https://events.cuny.edu/page'
page_number = 1
page = requests.get(URL+'1')

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='wrap-content')
#print(results.prettify())

project_href = [i['href'] for i in soup.find_all('a', href=True)]

#Like a big body that holds the whole app
root = tk.Tk()
root.title('CUNY REVAMPED Events')
apps = []
#adjusts size of the app
canvas = tk.Canvas(root, height = 700, width = 700, bg = '#263D42')
canvas.create_text(350,40, text="Today's Events", fill='black', font=('Helvetica 15 bold'))

#attaches it to the root
canvas.pack()

#building a white frame inside the green canvas
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight= 0.8, relx = 0.1, rely= 0.1)
event_details = Text(frame, bg='white', fg='black', font = 'Helvetica 12', height = 100, width = 560, wrap='word')
event_details.pack()
event_details.tag_configure("bold", font="Helvetica 12 bold")
event_elements = results.find_all("li", class_="box cec-list-item")
div_elements = results.find_all("div")
for event_element in event_elements:
    href_elements = event_element.find_all('a', href=True)
    div_element = event_element.find("div")
    string_soup = str(div_element)
    string_soup_second =(string_soup.partition('<br/>')[2])
    string_soup_third = (string_soup_second.partition('<h4>')[0])
    
    for href_element in href_elements:
        setting_elements = event_element.find_all('h4')
        event_details.insert(tk.INSERT, f'{href_element.text.strip()}:\n', 'bold')
        
        for setting_element in setting_elements:
            event_details.insert(tk.INSERT, f'{setting_element.text.strip()}\n')
    string = (string_soup_third.strip('</div>')).strip('<p')
    event_details.insert(tk.INSERT, f'{string}\n\n')

root.mainloop()