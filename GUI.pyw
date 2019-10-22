# * coding=utf-8 *
import tkinter as tk
import tkinter.messagebox as messagebox
import pandas as ps
import csv
import time
from WeightData import Display

def Write():
    Date=datainput.get()
    Weight=weightinput.get()
    try:
        time.strptime(Date,'%Y.%m.%d')
        data=[Date,Weight]
        with open('WeightData.csv','a+') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(data)
        messagebox.showinfo('Tips','Write Data Success!')
        datainput.delete(0,tk.END)
        weightinput.delete(0,tk.END)
    except Exception as e:
        messagebox.showerror('Exception',str(e))






window=tk.Tk()
#set title
window.title('Weight Record')

#set size
window.geometry('300x100')
dateLabel=tk.Label(window,text=" Date",font=("Arial",12)).place(x=20,y=10)
weightLabel=tk.Label(window,text="Weight",font=("Arial",12)).place(x=20,y=50)
datainput=tk.Entry(window,show=None)
datainput.place(x=80,y=12)
weightinput=tk.Entry(window,show=None)
weightinput.place(x=80,y=52)

writeButton=tk.Button(window,text="Write",width=10,height=1,bg='pink',command=Write).place(x=215,y=10)
displayButton=tk.Button(window,text="Display",width=10,height=1,bg='pink',command=Display).place(x=215,y=48)


window.mainloop()