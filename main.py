import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox, Treeview
from tkinter import messagebox
import matplotlib.pyplot as plt
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import convertions

root = Tk()

root.title("Logorduin")

# Variable globales
font = "Calibri"
valorOctal = ""
valorDecimal = ""
valorHexa = ""

inputData = ""

HammingTable = [
    ['Palabras de datos (sin paridad)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['P1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['P2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['P3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['P4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['P5', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['Palabras de datos (con paridad)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
]

ParityTable = [
    ['Palabra de datos recibida', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
     ''],
    ['P1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Error', ''],
    ['P2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Error', ''],
    ['P3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Correcto', ''],
    ['P4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Error', '']]

ParityTable = convertions.detectError('01101011101010111')[1]



# root.geometry("1400x650")
root.geometry('%dx%d+%d+%d' % (1400, 800, 20, 20))
root.resizable(height=False, width=False)

# Frame donde estan las tablas
tables_Frame = Frame(root, width=500, bg="white", bd=2)
tables_Frame.pack(fill=Y, side="right")

Hamming_Frame = Frame(tables_Frame, height=200, width=700, bg="white", bd=2)
Hamming_Frame.pack()

Parity_Frame = Frame(tables_Frame, height=200, width=700, bg="white", bd=2)
Parity_Frame.pack()

# Frame que el contenido del lado izquierdo
left_Frame = Frame(root, width=400, bg="white", borderwidth=2)
left_Frame.pack(fill="both", side="left")

# Frame que contiene el canvas donde la tortuga dibuja
number_frame = Frame(left_Frame, width=400, height=200, bg="white", bd=2)
number_frame.pack()
number_frame.pack(side='top', padx=0, pady=0, anchor='w')

# Frame que contiene las equivalencias
equivalencias_Frame = Frame(left_Frame, width=400, height=500, bg="white", bd=2)
equivalencias_Frame.pack()

# Frame que contiene la señal NZRI
NZRI_Frame = Frame(left_Frame, width=400, height=500, bg="white", bd=2)
NZRI_Frame.pack()


# _____________________________________Validaciones__________________________________


def validate():
    if convertions.validateBinary(numberEntry.get()):

        noiseLabel = Label(number_frame, text="Seleccione la posición del bit \n al que desea insertar ruido: ", fg="Black", bg="White", font=(font, 15))
        noiseLabel.place(x=20, y=140)
        noiseCombobox = Combobox(number_frame, font=(font, 14), width=10, values=["0", "1"], state='readonly')
        noiseCombobox.place(x=270, y=140)

        global valorOctal, valorDecimal, valorHexa, HammingTable, inputData
        inputData = numberEntry.get()
        valorOctal = convertions.convertOctal(numberEntry.get())
        valorDecimal = convertions.convertDecimal(numberEntry.get())
        valorHexa = convertions.convertHexadecimal(numberEntry.get())

        tempList = [[valorOctal, valorDecimal, valorHexa]]
        tempList.sort(key=lambda e: e[1], reverse=False)

        for i, (valorOctal, valorDecimal, valorHexa) in enumerate(tempList, start=1):
            convertionsBox.insert("", "end", values=(valorOctal, valorDecimal, valorHexa))
            displayNZRI(numberEntry.get())
        HammingTable = convertions.Hamming(numberEntry.get(), getParity())
        showHamming()
        showParity()



    else:
        messagebox.showinfo(message="El número ingresado debe ser binario y de 12 bits", title="Error")


def displayNZRI(number):
    for widget in NZRI_Frame.winfo_children():
        widget.destroy()
    Values = convertions.convertNZRI(number)
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    ax = figure.add_subplot(111)

    plt.setp(ax, xticks=Values[0], xticklabels=Values[2],
             yticks=[0, 1])
    ax.step(Values[0], Values[1], where='post')
    plot = FigureCanvasTkAgg(figure, NZRI_Frame)
    plot.draw()
    plot.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    ax.set_title('Código NZRI generado.')


# _________________________Elementos de la interfaz__________________________________


numberLabel = Label(number_frame, text="Número a analizar", fg="Black", bg="White", font=(font, 15))
numberLabel.place(x=20, y=10)

numberEntry = Entry(number_frame, font=(font, 15), borderwidth=3, relief="sunken")
numberEntry.place(x=20, y=50)

parityLabel = Label(number_frame, text="Paridad:", fg="Black", bg="White", font=(font, 15))
parityLabel.place(x=20, y=90)

parityCombobox = Combobox(number_frame, font=(font, 14), width=10, values=["Par", "Impar"], state='readonly')
parityCombobox.place(x=100, y=90)
root.option_add('*TCombobox*Listbox.font', (font, 14))
parityCombobox.current(0)

analizarBT = PhotoImage(file="Images/button_analizar.png")
analizarButton = Button(number_frame, bg='white', image=analizarBT, bd=0, command=validate)
analizarButton.place(x=265, y=50)

# NZRI display


# Table for convertions
label = Label(equivalencias_Frame, text="Equivalencias", font=("Arial", 15)).grid(row=0, columnspan=2)
# create Treeview with 3 columns
cols = ('Octal', 'Decimal', 'Hexadecimal')
convertionsBox = ttk.Treeview(equivalencias_Frame, columns=cols, show='headings')
# set column headings
for col in cols:
    convertionsBox.heading(col, text=col)
    convertionsBox.column(col, minwidth=0, width=140, stretch=NO, anchor="center")
convertionsBox.grid(row=1, column=0, columnspan=2)

HammingLabel = Label(Hamming_Frame, text="Cálculo de los bits de paridad en el código Hamming", fg="Black",
                     bg="White", font=(font, 14))
HammingLabel.grid(row=0, column=0, columnspan=2)

ComprobacionLabel = Label(Parity_Frame, text="Comprobación de los bits de paridad en el código Hamming", fg="Black",
                          bg="White", font=(font, 14))
ComprobacionLabel.grid(row=0, column=0, columnspan=2)

# Tabla de Hamming
style = ttk.Style()
style.configure("Treeview", font=(font, 11))


def showHamming():
    global HammingTable, listBox
    tempList = HammingTable
    for i in listBox.get_children():
        listBox.delete(i)

    for row in tempList:
        listBox.insert("", "end", values=(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
            row[13], row[14], row[15], row[16], row[17]))



# create Treeview with 3 columns
colsHamming = (
'', 'p1', 'p2', 'd1', 'p3', 'd2', 'd3', 'd4', 'p4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'p5', 'd12')
listBox = Treeview(Hamming_Frame, columns=colsHamming, show='headings')
# set column headings
for col in colsHamming:
    if col == colsHamming[0]:
        listBox.heading(col, text=col)
        listBox.column(col, minwidth=0, width=220, stretch=NO, anchor="center")
    else:
        listBox.heading(col, text=col)
        listBox.column(col, minwidth=0, width=40, stretch=NO, anchor="center")
listBox.grid(row=0, column=0, columnspan=2)
showHamming()


# Comprobación de los bits de paridad

def showParity():
    global ParityTable, listBoxParity
    tempList = convertions.detectError('01101011101010111')[1]
    for row in tempList:
        listBoxParity.insert("", "end", values=(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
            row[13], row[14], row[15], row[16], row[17], row[18], row[19]))

# create Treeview with 3 columns
colsParity = ('', 'p1', 'p2', 'd1', 'p3', 'd2', 'd3', 'd4', 'p4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'p5', 'd12',
              "Prueba de paridad", "Bit de Paridad")
listBoxParity = Treeview(Parity_Frame, columns=colsParity, show='headings')
# set column headings
for col in colsParity:
    if col == colsParity[0]:
        listBoxParity.heading(col, text=col)
        listBoxParity.column(col, minwidth=0, width=170, stretch=NO, anchor="center")
    elif col == colsParity[len(colsParity) - 1] or col == colsParity[len(colsParity) - 2]:
        listBoxParity.heading(col, text=col)
        listBoxParity.column(col, minwidth=0, width=110, stretch=NO, anchor="center")
    else:
        listBoxParity.heading(col, text=col)
        listBoxParity.column(col, minwidth=0, width=30, stretch=NO, anchor="center")
listBoxParity.grid(row=2, column=0, columnspan=2)

def getParity():
    result = False
    if parityCombobox.get() == "Par":
        result = True
    return result


def getNoisedNumber():
    return 1


# Safe closure
def on_closing():
    if messagebox.askokcancel("Salir", "Seguros que quieres salir?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
