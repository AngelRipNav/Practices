#Ejercicio 52:Escribir un programa que me ayude a aprender las tablas de multiplicar.

#Para ello se irá pidiendo la tabla de multiplicar de un número (pedido por teclado con anterioridad) y comprobando que los valores introducidos son correctos. Si es así el programa escribirá "CORRECTO" y en caso contrario deberá escribir "LO SIENTO, SE HA EQUIVOCADO. LA RESPUESTA CORRECTA ES número".

#La última línea mostrará el número de aciertos.

tabla = int(input("¿De qué número quieres practicar la tabla de multiplicar? "))
aciertos = 0

print(f"\n¡Vamos a practicar la tabla del {tabla}!")
print("Responde las siguientes multiplicaciones:")

for i in range(1, 11):
    multv= tabla * i
    

    respuesta_usuario = int(input(f"\n{tabla} x {i} = "))
        
    if respuesta_usuario == multv:
        print("CORRECTO")
        aciertos += 1
    else:
        print(f"LO SIENTO, SE HA EQUIVOCADO. LA RESPUESTA CORRECTA ES {multv}") 
        


print(f"\nRESULTADO FINAL: {aciertos}/10 aciertos")
