# Inicializar las variables
peso = 0
altura = 0
edad = 0

# Leer los datos desde el archivo si existen
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
except FileNotFoundError:
    pass

# Solicitar al usuario los datos si son iguales a 0
if peso == 0:
    peso = float(input("Ingrese su peso en kg: "))
if altura == 0:
    altura = float(input("Ingrese su altura en metros: "))
if edad == 0:
    edad = int(input("Ingrese su edad en años: "))

# Guardar los datos en un archivo
with open("datos_usuario.txt", "w") as archivo:
    archivo.write(f"Peso: {peso} kg\n")
    archivo.write(f"Altura: {altura} metros\n")
    archivo.write(f"Edad: {edad} años\n")

print("Datos guardados correctamente en 'datos_usuario.txt'.")

# Imprimir los datos directamente desde las variables
print("Datos almacenados:")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} metros")
print(f"Edad: {edad} años")

actualizar = input("¿Desea actualizar los datos? (si/no): ").lower()
if actualizar == "si":
    peso = 0
    altura = 0
    edad = 0
    print("Los datos han sido restablecidos a 0. Por favor, ingrese los nuevos datos.")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    print("Datos almacenados:")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} metros")
    print(f"Edad: {edad} años")

# Guardar los datos en un archivo
with open("datos_usuario.txt", "w") as archivo:
    archivo.write(f"Peso: {peso} kg\n")
    archivo.write(f"Altura: {altura} metros\n")
    archivo.write(f"Edad: {edad} años\n")

print("Datos guardados correctamente en 'datos_usuario.txt'.")
