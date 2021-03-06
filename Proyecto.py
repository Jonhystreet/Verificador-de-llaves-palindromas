import AFS
import  instrucciones

import tkinter
from tkinter import Label
from tkinter import *
from tkinter import ttk

class Principal:
    def __init__(self,descripcion):
        self.resultado=None
        self.tran=None
        self.descri=descripcion
        self.ventana=tkinter.Tk()
    
    def cargar_resultado(self,listbox,listbox2):
        for r in self.resultado:
            listbox.insert(END,r)
        for t in self.tran:
            listbox2.insert(END, t)
          
    def sgda_ventana(self):
        segunda_ventana=tkinter.Toplevel(self.ventana)
        segunda_ventana.title('Ventana de procedimiento')
        segunda_ventana.minsize(width=600,height=500)
        
        scrollbar = Scrollbar(segunda_ventana)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        listbox = Listbox(segunda_ventana)
        listbox.config( width=60, height=30,yscrollcommand=scrollbar.set,font=("Courier", 10))
        scrollbar.config(command=listbox.yview)
        
        
        listbox['bg'] = 'black'
        listbox['fg'] = "#38EB5C"
    
        listbox2 = Listbox(segunda_ventana)
        listbox2.config( width=40, height=30,yscrollcommand=scrollbar.set,font=("Courier", 10))
        listbox2['bg'] = 'black'
        listbox2['fg'] = "#38EB5C"
        
        self.cargar_resultado(listbox,listbox2)
   
        listbox.pack(side=LEFT, fill=Y)
        listbox2.pack()
        self.ventana.iconify()

    def  evaluar(self):
        auto=AFS.Autopi(self.text.get())
        auto.validar()
        
        self.resultado=auto.resultado
        self.tran=auto.transiciones

        self.sgda_ventana()
        

    def main(self):
        self.ventana.title('Ventana principal')
        img = PhotoImage(file="img.gif")
        widget = Label(self.ventana, image=img).pack()

        plbra=tkinter.Entry(self.ventana)
        plbra.pack()
        self.text=plbra
        
        boton = tkinter.Button(self.ventana, text="Validar", command=self.evaluar, bg="#38EB5C",relief="groove")
        boton['bg'] = 'black'
        boton['fg'] = "#38EB5C"
        boton.pack()
        

     
        listbox = Listbox(self.ventana)
        listbox.place(relwidth=1 ,relheight=-0.50)
        listbox['bg'] = 'black'
        listbox['fg'] = "#38EB5C"
    
        
        for des in self.descri:
            listbox.insert(END, des)
            
        listbox.pack(fill=X, expand=1)
        
        scrollbar = Scrollbar(self.ventana)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        listbox.config(yscrollcommand=scrollbar.set , font=("Courier", 14))
        scrollbar.config(command=listbox.yview)

        self.ventana.minsize(width=600,height=500)
        self.ventana.mainloop()
        



des = instrucciones.des
p=Principal(des)
p.main()