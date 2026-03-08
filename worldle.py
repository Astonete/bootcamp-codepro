# encontrar palabras secretas

palabra_a_encontrar = "circo"# palabra secreta a encontrar
intentos = 5#numero de intentos para adivinar la palabra
cantidad_letras_de_palabra_a_encontrar = 5#cantidad de letras que tiene la palabra a encontrar


def obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada):# recibimos 2 parametros la plabra a encontrar y la palabra ingresada por el usuario esta funcion se encarga de verificar cada letra de la palabra ingresada y compararla con la palabra a encontrar para devolver una lista con el resultado de la verificacion
    letras_verificadas = [] #aca se guarda las letras ingresadas por el usuario con su respectiva verificacion

    for posicion in range(cantidad_letras_de_palabra_a_encontrar):# recorre la palargra ingresada por el usuario y la compara con la palabra a encontrar letra por letra

        if palabra_a_encontrar[posicion] == palabra_ingresada[posicion]:# verifica si las letras coincide con la posicion correcta de la palabra a encontrar
            letras_verificadas.append("[" + palabra_ingresada[posicion] + "]")# agrega corchetes si la letra se encuentra en la posicion correcta en la varialbeletras_verificadas

        elif palabra_ingresada[posicion] in palabra_a_encontrar:# verifica si la letra se encuentra en la palabra a encontrar pero no en la posicion correcta
            letras_verificadas.append("(" + palabra_ingresada[posicion] + ")")# agrega parentesis si se encuentra la letra en la palabra a encontrar pero no en la posicion correcta en la varialbele letras_verificadas

        else:
            letras_verificadas.append(palabra_ingresada[posicion])# si la letra no se encuentra en la palabra a encontrar agrega la letra sin ningun simbolo en la varialbele letras_verificadas

    return letras_verificadas # devuelve la lista con el resultado de la verificacion de cada letra de la palabra ingresada por el usuario


while intentos > 0:#controla que la cantidad de intentos sea mayor a 0 si llega a cero termina el juego

    print(f"Te quedan {intentos} intentos")#avisa cuantos intentos le quedan al usuario para adivinar la palabra
    palabra_ingresada = input("Ingrese su palabra: ")#pide al usuario que ingrese una palabra para adivinar la palabra a encontrar

    if len(palabra_ingresada) != cantidad_letras_de_palabra_a_encontrar:#controla el  tama;o que ingreso el usuario es distinta a la cantidad de letras que tiene la palabra a encontrar
        print("La palabra debe tener 5 letras")# mensaje que su palabra debe tener 5 letras

    resultado = obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada)#llamamos a la funcion y se carga en la variable resultado la lista con el resultado de la verificacion de cada letra de la palabra ingresada por el usuario

    print("Resultado:", resultado)#se imprime para que se muestre el resultado de la verificacion de cada letra de la palabra ingresada por el usuario

    if palabra_ingresada == palabra_a_encontrar:#avisa cuando el usuario adivina la palabra a encontrar
        print("¡Ganaste!")#mensaje de felicitaciones por adivinar la palabra a encontrar
        break #frena el juego porque ya gano

    intentos -= 1#resta un intento cada vez que el usuario ingresa una palabra para adivinar la palabra a encontrar


if intentos == 0:#si tu intento llegan a 0 perdistes el juego
    print("Perdiste, la palabra era:", palabra_a_encontrar)#mensaje que da error y te muestra la palabra secreta a encontrar