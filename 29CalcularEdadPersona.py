#Ejercicio 29: Calcular la edad de una persona a partir de su fecha de nacimiento y la fecha actual.

def main():
    dia_nac = int(input("Introduce el día de nacimiento: "))
    mes_nac = int(input("Introduce el mes de nacimiento: "))
    ano_nac = int(input("Introduce el año de nacimiento: "))
    dia_act = int(input("Introduce el día actual: "))
    mes_act = int(input("Introduce el mes actual: "))
    ano_act = int(input("Introduce el año actual: "))
    if  (mes_act or mes_nac <=0 or mes_nac >12) or (dia_act or dia_nac <=0 or dia_nac >31):
        print("Fecha incorrecta")
    else:
        edad = ano_act - ano_nac
        if mes_act < mes_nac or (mes_act == mes_nac and dia_act < dia_nac):
            edad = edad - 1
        print(f"Tienes {edad} años")    

if __name__ == "__main__":
    main()