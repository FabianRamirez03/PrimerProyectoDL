from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox, Treeview

root = Tk()

root.title("Logorduin")

# Variable globales
font = "Calibri"
valorOctal = ""
valorDecimal = ""
valorHexa = ""

HammingTable = [['Palabras de datos (sin paridad)', '', '', '0', '', '1', '1', '0', '', '1', '0', '1'],
                ['P1', '', '', '0', '', '1', '1', '0', '', '1', '0', '1'],
                ['P2', '', '', '0', '', '1', '1', '0', '', '1', '0', '1'],
                ['P3', '', '', '0', '', '1', '1', '0', '', '1', '0', '1'],
                ['P4', '', '', '0', '', '1', '1', '0', '', '1', '0', '1'],
                ['Palabras de datos (con paridad)', '', '', '0', '', '1', '1', '0', '', '1', '0', '1']]

ParityTable = [['Palabra de datos recibida', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', '1', ''],
               ['P1', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', 'Error', '1'],
               ['P2', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', 'Error', '1'],
               ['P3', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', 'Correcto', '1'],
               ['P4', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', 'Error', '1']]

# root.geometry("1400x650")
root.geometry('%dx%d+%d+%d' % (1000, 500, 20, 20))
root.resizable(height=False, width=False)

# Frame donde se digita el codig
tables_Frame = Frame(root, width=500, bg="white", bd=2)
tables_Frame.pack(fill=Y, side="right")

Hamming_Frame = Frame(tables_Frame, height=200, width=700, bg="white", bd=2)
Hamming_Frame.pack()

Parity_Frame = Frame(tables_Frame, height=200, width=700, bg="white", bd=2)
Parity_Frame.pack()

# Frame que contiene el resto de la interfaz fuera del recuadro del codigo
left_Frame = Frame(root, width=935, bg="white", borderwidth=2)
left_Frame.pack(fill="both", side="left")

# Frame que contiene el canvas donde la tortuga dibuja
number_frame = Frame(left_Frame, width=935, height=200, bg="white", bd=2)
number_frame.pack()

# Frame que contiene la consola
equivalencias_Frame = Frame(left_Frame, width=750, height=150, bg="white", bd=2)
equivalencias_Frame.pack()

# Frame que inferior izquierdo
left_Botom_Frame = Frame(left_Frame, width=935, height=550, bg="white", bd=2)
left_Botom_Frame.pack()

# _________________________Elementos de la interfaz__________________________________


numberLabel = Label(number_frame, text="Número a analizar", fg="Black", bg="White", font=(font, 15))
numberLabel.place(x=10, y=10)

numberEntry = Entry(number_frame, font=(font, 15), borderwidth=3, relief="sunken")
numberEntry.place(x=10, y=50)

parityLabel = Label(number_frame, text="Paridad:", fg="Black", bg="White", font=(font, 14))
parityLabel.place(x=10, y=90)

comboExample = Combobox(number_frame, font=(font, 14), width=10, values=["Par", "Impar"], state='readonly')
comboExample.place(x=90, y=90)
root.option_add('*TCombobox*Listbox.font', (font, 14))
comboExample.current(0)

analizarBT = PhotoImage(file="Images/button_analizar.png")
analizarButton = Button(number_frame, bg='white', image=analizarBT, bd=0)
analizarButton.place(x=83, y=130)

EquivalenciasLabel = Label(equivalencias_Frame, text="Equivalencias", fg="Black", bg="White", font=(font, 15))
EquivalenciasLabel.place(x=10, y=10)

OctalLabel = Label(equivalencias_Frame, text="Octal:  " + valorOctal, fg="Black", bg="White", font=(font, 14))
OctalLabel.place(x=10, y=48)

DecimalLabel = Label(equivalencias_Frame, text="Decimal:  " + valorDecimal, fg="Black", bg="White", font=(font, 14))
DecimalLabel.place(x=10, y=83)

HexaLabel = Label(equivalencias_Frame, text="Hexadecimal:  " + valorHexa, fg="Black", bg="White", font=(font, 14))
HexaLabel.place(x=10, y=118)

HammingLabel = Label(Hamming_Frame, text="Cálculo de los bits de paridad en el código Hamming", fg="Black",
                     bg="White", font=(font, 14))
HammingLabel.grid(row=0, column=0, columnspan=2)

ComprobacionLabel = Label(Parity_Frame, text="Cálculo de los bits de paridad en el código Hamming", fg="Black",
                          bg="White", font=(font, 14))
ComprobacionLabel.grid(row=0, column=0, columnspan=2)

# Tabla de Hamming
style = ttk.Style()
style.configure("Treeview", font=(font, 11))


def showHamming():
    global HammingTable
    tempList = HammingTable

    for row in tempList:
        listBox.insert("", "end", values=(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))


# create Treeview with 3 columns
colsHamming = ('', 'p1', 'p2', 'd1', 'p3', 'd2', 'd3', 'd4', 'p4', 'd5', 'd6', 'd7')
listBox = Treeview(Hamming_Frame, columns=colsHamming, show='headings')
# set column headings
for col in colsHamming:
    if col == colsHamming[0]:
        listBox.heading(col, text=col)
        listBox.column(col, minwidth=0, width=220, stretch=NO, anchor="center")
    else:
        listBox.heading(col, text=col)
        listBox.column(col, minwidth=0, width=40, stretch=NO, anchor="center")
listBox.grid(row=2, column=0, columnspan=2)
showHamming()


# Comprobación de los bits de paridad

def showParity():
    global ParityTable
    tempList = ParityTable

    for row in tempList:
        listBox.insert("", "end", values=(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))


# create Treeview with 3 columns
colsParity = ('', 'p1', 'p2', 'd1', 'p3', 'd2', 'd3', 'd4', 'p4', 'd5', 'd6', 'd7', "Prueba de paridad", "Bit de Paridad")
listBox = Treeview(Parity_Frame, columns=colsParity, show='headings')
# set column headings
for col in colsParity:
    if col == colsParity[0]:
        listBox.heading(col, text=col)
        listBox.column(col, minwidth=0, width=170, stretch=NO, anchor="center")
    elif col == colsParity[len(colsParity)-1] or col == colsParity[len(colsParity)-2]:
        listBox.heading(col, text=col)
        listBox.column(col, minwidth=0, width=110, stretch=NO, anchor="center")
    else:
        listBox.heading(col, text=col)
        listBox.column(col, minwidth=0, width=30, stretch=NO, anchor="center")
listBox.grid(row=2, column=0, columnspan=2)
showParity()


# Safe closure
def on_closing():
    if messagebox.askokcancel("Salir", "Seguros que quieres salir?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
