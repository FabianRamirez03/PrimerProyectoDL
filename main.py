from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

root = Tk()

root.title("Logorduin")


# Variable globales
font = "Calibri"


# root.geometry("1400x650")
root.geometry('%dx%d+%d+%d' % (1000, 500, 20, 20))
root.resizable(height=False, width=False)


# Frame donde se digita el codigo
code_Frame = Frame(root, height=150, width=700, bg="red", bd=2)
code_Frame.pack(fill=Y, side="right")

# Frame que contiene el resto de la interfaz fuera del recuadro del codigo
left_Frame = Frame(root, width=935, bg="green", borderwidth=2)
left_Frame.pack(fill="both", side="right")

# Frame que contiene el canvas donde la tortuga dibuja
number_frame = Frame(left_Frame, width=935, height=200, bg="white", bd=2)
number_frame.pack()

# Frame que inferior izquierdo
left_Botom_Frame = Frame(left_Frame, width=935, height=550, bg="blue", bd=2)
left_Botom_Frame.pack(fill="both")

# Frame que contiene la consola
equivalencias_Frame = Frame(left_Botom_Frame, width=750, height=150, bg="red", bd=2)
equivalencias_Frame.pack(side=LEFT)

# Frame que contiene los botones
buttons_Frame = Frame(left_Botom_Frame, width=185, height=100, bg="black", bd=2)
buttons_Frame.pack(side=LEFT)

# _________________________Elementos de la interfaz__________________________________


numberLabel = Label(number_frame, text="Número a analizar", fg="Black", bg="White", font=(font, 15))
numberLabel.place(x=10, y=10)

numberEntry = Entry(number_frame, font = (font, 15), borderwidth=3, relief="sunken")
numberEntry.place(x=10, y=50)

parityLabel = Label(number_frame, text="Paridad:", fg="Black", bg="White", font=(font, 14))
parityLabel.place(x=10, y=90)

comboExample = Combobox(number_frame, font=(font, 14), width=10, values=["Par", "Impar"])
comboExample.place(x=90, y=90)
root.option_add('*TCombobox*Listbox.font', (font, 14))
comboExample.current(0)

analizarBT = PhotoImage(file="Images/button_analizar.png")
analizarButton = Button(number_frame, bg='white', image=analizarBT, bd=0)
analizarButton.place(x=83, y=130)



EquivalenciasLabel = Label(equivalencias_Frame, text="Equivalencias", fg="Black", bg="White", font=(font, 15))
EquivalenciasLabel.place(x=10, y=10)









# Safe closure
def on_closing():
    if messagebox.askokcancel("Salir", "Seguros que quieres salir?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()