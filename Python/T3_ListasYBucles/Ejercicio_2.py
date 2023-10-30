#Pedir contraseña

contra = str(input("Introduzca la contraseña: "))

#Comprobar contraseña

contra2 = str(input("Repita la contraseña: "))

if contra != contra2:
    while contra != contra2:
        contra2 = str(input("Las contraseñas no coinciden, repita la contraseña: "))

print("Contraseña creada correctamente :)")