#Actividad 20: Programa que recibe como datos de entrada una hora expresada en horas, minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán, transcurrido un segundo.

def main():
    hora = int(input("Introduce la hora: "))
    minutos = int(input("Introduce los minutos: "))
    segundos = int(input("Introduce los segundos: "))
    segundos = segundos + 1
    if segundos >= 60:
        segundos = 0
        minutos = minutos + 1
        if minutos >= 60:
            minutos = 0
            hora = hora + 1
            if hora >= 24:
                hora = 0
    print(f"{hora}:{minutos}:{segundos}")
if __name__ == "__main__":
    main()