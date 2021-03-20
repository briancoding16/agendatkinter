from tkinter import *
from tkinter import messagebox


# #root = Tk()
# root.title("Agenda")
# root.geometry("700x500")
# colorFondo = "#006"
# colorLetra= "#FFF"
# root.configure(background=colorFondo)








lista = []

def guardar():
    n = nombre.get()
    ap = app.get()
    cor = correo.get()
    tel = telefono.get()
    lista.append(n+"$"+ap+"$"+cor+"$"+tel)
    escribirContacto()
    n = nombre.set("")
    ap = app.set("")
    cor = correo.set("")
    tel = telefono.set("")
    consultar()




def eliminar():
    conteliminar.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split("$")
        if conteliminar.get()==arreglo[3]:
            lista.remove(elemento)
            removido=True
    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo("Eliminar","Elemento eliminado"+ " "+ conteliminar.get())


def consultar():
    r = Text(root, width=80, height=15)
    lista.sort()
    valores = []
    r.insert(INSERT, "Nombre\tApellido\t\tTelefono\t\tCorreo\n")
    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[3])
        r.insert(INSERT,arreglo[0]+"\t"+arreglo[1]+"\t"+arreglo[2]+"\t"+arreglo[3])
        r.place(x=20, y=230)
        spinTelefono = Spinbox(root, value=(valores), textvariable=conteliminar)
        spinTelefono.place(x=450, y=50)
    if lista == []:
         spinTelefono=Spinbox(root, value=(valores))
         spinTelefono.place(x=450, y=50)
    r.config(state=DISABLED)         
      
    

def iniciarArchivo():
    archivo=open("ag.txt","a")
    archivo.close()

def cargar():
    archivo = open("ag.txt", "r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1]=="\n":
                linea=linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()

def escribirContacto():
    archivo = open("ag.txt", "w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()













root = Tk()
nombre = StringVar() 
app = StringVar() 
#apm = StringVar() 
correo = StringVar() 
telefono = StringVar() 
conteliminar = StringVar() 
colorFondo = "#006" 
colorLetra = "#FFF" 
iniciarArchivo()
cargar()
consultar()
root.title("Agenda con archivos") 
root.geometry("700x500") 
root.configure(background = colorFondo) 
etiquetaTitulo = Label(root, text="Agenda con Archivos", bg=colorFondo, fg=colorLetra)
etiquetaTitulo.place(x=270, y=10)






etiquetaN = Label(root, text="Nombre", bg=colorFondo, fg=colorLetra)
etiquetaN.place(x=50, y=50) 

cajaN = Entry(root, textvariable=nombre)
cajaN .place(x=150, y=50) 


etiquetaApp = Label(root, text="Apellido", bg=colorFondo, fg=colorLetra)
etiquetaApp.place(x=50, y=80) 

cajaApp = Entry(root, textvariable=app)
cajaApp.place(x=150, y=80) 



# etiquetaApm = Label(root, text="Apellido Materno", bg=colorFondo,fg=colorLetra)
# etiquetaApm.place(x=50, y=110) 



etiquetaT = Label(root, text="Teléfono", bg=colorFondo, fg=colorLetra)
etiquetaT.place(x=50, y=140) 


cajaT = Entry(root, textvariable=telefono)
cajaT.place(x=150, y=140) 


etiquetaC = Label(root, text="Correo", bg=colorFondo, fg=colorLetra)
etiquetaC.place(x=50, y=170) 


cajaC = Entry(root, textvariable=correo)
cajaC.place(x=150, y=170) 

etiquetaEliminar = Label(root, text="Teléfono: ", bg= colorFondo, fg=colorLetra)
etiquetaEliminar.place(x=370, y=50) 



spinTelefono = Spinbox(root, textvariable=conteliminar)
spinTelefono.place(x=450, y=50)

botoGuardar = Button(root, text="Guardar", command=guardar, bg="#009",fg="white")
botoGuardar.place(x=180, y=200) 


botoEliminar = Button(root, text="Eliminar", command=eliminar, bg="#009",fg="white")
botoEliminar.place(x=490, y=80) 






root.mainloop()