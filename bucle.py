#Imprimir todas las potencias de 2 hasta llegar al numero mil.

#def operacion(numero, potencia):
#    resultado = numero**potencia    
#    while (resultado <= 1000):
 #       resultado = numero**potencia
  #      print(str(numero) + " Elevado a la " + str(potencia) + " Es igual a: " + str(resultado))
   #     potencia = potencia + 1

#    else:
 #       print("Hemos terminado")


#def run():
 #   numero = int(input("Escribe el numero al que quieres hallarle las potencias: "))
  #  print("Comenzamos con " + str(numero))
   # operacion(numero, 2)
    


#if __name__ == '__main__':
 #   run()


def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print(" 2 Elevado a la " + str(contador) +
         " Es igual a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador




if __name__ == '__main__':
    run()