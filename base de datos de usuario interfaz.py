import tkinter as tk
from tkinter import messagebox

# Función para guardar los datos en un archivo
def guardar_datos():
    global peso, altura, edad, diabetes, hipertension
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())
    edad = int(edad_entry.get())
    diabetes = diabetes_var.get()
    hipertension = hipertension_var.get()
    
    with open("datos_usuario.txt", "w") as archivo:
        archivo.write(f"Peso: {peso} kg\n")
        archivo.write(f"Altura: {altura} metros\n")
        archivo.write(f"Edad: {edad} años\n")
        archivo.write(f"diabetes: {diabetes}\n")
        archivo.write(f"hipertension: {hipertension}\n")

    messagebox.showinfo("Información", "Datos guardados correctamente en 'datos_usuario.txt'.")
    mostrar_actualizar()

# Función para actualizar los datos
def actualizar_datos():
    global peso, altura, edad, diabetes, hipertension
    peso = 0
    altura = 0
    edad = 0
    diabetes = False
    hipertension = False
    
    peso_entry.delete(0, tk.END)
    altura_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    diabetes_var.set(False)
    hipertension_var.set(False)

    # Mostrar el botón de "Guardar Datos"
    guardar_button.grid(row=5, column=0, padx=10, pady=10)
    # Ocultar el botón de "Actualizar Datos"
    actualizar_button.grid_forget()

# Función para mostrar el botón de "Actualizar Datos"
def mostrar_actualizar():
    # Mostrar el botón de "Actualizar Datos"
    actualizar_button.grid(row=5, column=0, padx=10, pady=10)
    # Ocultar el botón de "Guardar Datos"
    guardar_button.grid_forget()

# Crear una ventana principal
root = tk.Tk()
root.title("Registro de Datos de Usuario")

# Etiquetas y entradas de texto para ingresar los datos
peso_label = tk.Label(root, text="Peso (kg):")
peso_label.grid(row=0, column=0, padx=10, pady=5)
peso_entry = tk.Entry(root)
peso_entry.grid(row=0, column=1, padx=10, pady=5)

altura_label = tk.Label(root, text="Altura (metros):")
altura_label.grid(row=1, column=0, padx=10, pady=5)
altura_entry = tk.Entry(root)
altura_entry.grid(row=1, column=1, padx=10, pady=5)

edad_label = tk.Label(root, text="Edad (años):")
edad_label.grid(row=2, column=0, padx=10, pady=5)
edad_entry = tk.Entry(root)
edad_entry.grid(row=2, column=1, padx=10, pady=5)

diabetes_var = tk.BooleanVar()
diabetes_checkbox = tk.Checkbutton(root, text="¿Es diabético?", variable=diabetes_var)
diabetes_checkbox.grid(row=3, column=0, padx=10, pady=5)

hipertension_var = tk.BooleanVar()
hipertension_checkbox = tk.Checkbutton(root, text="¿Tiene hipertensión?", variable=hipertension_var)
hipertension_checkbox.grid(row=4, column=0, padx=10, pady=5)

# Botones para guardar y actualizar datos
guardar_button = tk.Button(root, text="Guardar Datos", command=guardar_datos)
# Mostrar el botón de "Actualizar Datos" al inicio
actualizar_button = tk.Button(root, text="Actualizar Datos", command=actualizar_datos)
actualizar_button.grid(row=5, column=0, padx=10, pady=10)

# Cargar datos desde el archivo al inicio
def cargar_datos():
    global peso, altura, edad, diabetes, hipertension
    try:
        with open("datos_usuario.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if "Peso:" in linea:
                    peso = float(linea.split(":")[1].strip().replace("kg", ""))
                elif "Altura:" in linea:
                    altura = float(linea.split(":")[1].strip().replace("metros", ""))
                elif "Edad:" in linea:
                    edad = int(linea.split(":")[1].strip().replace("años", ""))
                elif "diabetes:" in linea:
                    diabetes = eval(linea.split(":")[1].strip().capitalize())  # Lee True o False
                elif "hipertension:" in linea:
                    hipertension = eval(linea.split(":")[1].strip().capitalize())  # Lee True o False

        # Mostrar los datos cargados
        peso_entry.insert(0, str(peso))
        altura_entry.insert(0, str(altura))
        edad_entry.insert(0, str(edad))
        diabetes_var.set(diabetes)
        hipertension_var.set(hipertension)
        
        # Mostrar solo el botón de "Actualizar Datos"
        mostrar_actualizar()

    except FileNotFoundError:
        pass

# Cargar datos desde el archivo al inicio
cargar_datos()

root.mainloop()
