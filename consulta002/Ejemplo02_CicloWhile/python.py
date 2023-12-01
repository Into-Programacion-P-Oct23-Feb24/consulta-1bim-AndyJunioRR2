contador = 0

while contador < 5:
    contador += 1 
numero_secreto = 7
intentos = 0

while True:
    guess = int(input("Adivina el número (entre 1 y 10) \n"
                      "Cuentas con 3 intentos para poder adivinarlo: "))
    
    if guess == numero_secreto:
        print(f"¡Correcto! ¡El número era {numero_secreto}!")
        break  
    else:
        print("Número incorrecto. Intente de nuevo.")
        intentos += 1

    if intentos >= 3:
        print("Agotaste tus intentos. El número secreto era:", numero_secreto)
        break  