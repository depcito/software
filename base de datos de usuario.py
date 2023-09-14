# Inicializar las variables
peso = 0
altura = 0
edad = 0
diabetes= 0
hipertension = 0


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
            elif "diabetes:" in linea:
                d = (linea.split(":")[1].strip())
                if d == "False":
                    diabetes = 2
                if d == "True":
                    diabetes = 1
            elif "hipertension:" in linea:
                h = (linea.split(":")[1].strip())
                if h == "False":
                    hipertension = 2
                if h == "True":
                    hipertension = 1
                
except FileNotFoundError:
    pass

# Solicitar al usuario los datos si son iguales a 0
if peso == 0:
    peso = float(input("Ingrese su peso en kg: "))
if altura == 0:
    altura = float(input("Ingrese su altura en metros: "))
if edad == 0:
    edad = int(input("Ingrese su edad en años: "))
if diabetes == 0:
    d = input("es diabetico? (si/no): ").lower()
    if d == "si":
        diabetes = 1
    else:
        diabetes = 2
if hipertension == 0 :
    h = input("es hipertenso? (si/no): ").lower()
    if h == "si":
        hipertension = 1
    else:
        hipertension = 2


# Guardar los datos en un archivo
with open("datos_usuario.txt", "w") as archivo:
    archivo.write(f"Peso: {peso} kg\n")
    archivo.write(f"Altura: {altura} metros\n")
    archivo.write(f"Edad: {edad} años\n")
    archivo.write(f"diabetes: {diabetes} \n")
    archivo.write(f"hipertension: {hipertension} \n")


print("Datos guardados correctamente en 'datos_usuario.txt'.")

# Imprimir los datos directamente desde las variables
print("Datos almacenados:")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} metros")
print(f"Edad: {edad} años")
print(f"diabetes: {diabetes}")
print(f"hipertension: {hipertension}")
actualizar = input("¿Desea actualizar los datos? (si/no): ").lower()
if actualizar == "si":
    peso = 0
    altura = 0
    edad = 0
    diabetes = 3
    hipertension = 3
    print("Los datos han sido restablecidos a 0. Por favor, ingrese los nuevos datos.")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    edad = int(input("Ingrese su edad en años: "))
    d = input("es diabetico? (si/no): ")
    if d == "si":
        diabetes = 1
    elif d == "no":
        diabetes = 2
        
    h = input("es hipertenso? (si/no): ")
    if h == "si":
        hipertension = 1
    else:
        hipertension = 2


    print("Datos almacenados:")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} metros")
    print(f"Edad: {edad} años")
    print(f"diabetes: {diabetes}")
    print(f"hipertension: {hipertension}")


# Guardar los datos en un archivo
with open("datos_usuario.txt", "w") as archivo:
    archivo.write(f"Peso: {peso} kg\n")
    archivo.write(f"Altura: {altura} metros\n")
    archivo.write(f"Edad: {edad} años\n")
    archivo.write(f"diabetes: {diabetes} \n")
    archivo.write(f"hipertension: {hipertension} \n")


print("Datos guardados correctamente en 'datos_usuario.txt'.")
#los valores de diabetes e hipertension son 1 y 2 donde 1 es true y 2 es false
