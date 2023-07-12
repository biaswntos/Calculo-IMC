from math import pow
from time import sleep
r = 'S'
while r == 'S':
    print("=" * 20)
    print("CÁLCULO DE IMC")
    print("=" * 20)

    peso = float(input("Kg: "))
    altura = float(input("Digite sua altura em metros: "))

    imc = peso / (pow(altura, 2))

    print("CALCULANDO...")
    sleep(1)

    print("IMC: {:.2f}.".format(imc))

    if imc < 18.49:
        peso_ideal_minimo = 18.5 * pow(altura, 2)
        peso_ideal_maximo = 25 * pow(altura, 2)
        print("Você está \033[1;33;40mABAIXO DO PESO\033[m.")
        print("Com essa altura, para estar no peso ideal, você precisa ter entre {:.2f}kg e {:.2f}kg.".format(peso_ideal_minimo, peso_ideal_maximo))
        r = str(input("Deseja verificar novamente? [S/N]: ")).upper().strip()

    elif 18.49 <= imc < 25:
        print("Você está no \033[1;32;40mPESO IDEAL\033[m.")
        r = str(input("Deseja verificar novamente? [S/N]: ")).upper().strip()

    elif 25 <= imc < 30:
        peso_ideal_minimo = 18.5 * pow(altura, 2)
        peso_ideal_maximo = 25 * pow(altura, 2)
        print("Você está com \033[1;36;40mSOBREPESO\033[m.")
        print("Com essa altura, para estar no peso ideal, você precisa ter entre {:.2f}kg e {:.2f}kg.".format(peso_ideal_minimo, peso_ideal_maximo))
        r = str(input("Deseja verificar novamente? [S/N]: ")).upper().strip()

    elif 30 <= imc < 40:
        peso_ideal_minimo = 18.5 * pow(altura, 2)
        peso_ideal_maximo = 25 * pow(altura, 2)
        print("Você está com \033[1;31;40mOBESIDADE\033[m.")
        print("Com essa altura, para estar no peso ideal, você precisa ter entre {:.2f}kg e {:.2f}kg.".format(peso_ideal_minimo, peso_ideal_maximo))
        r = str(input("Deseja verificar novamente? [S/N]: ")).upper().strip()

    elif imc > 40:
        peso_ideal_minimo = 18.5 * pow(altura, 2)
        peso_ideal_maximo = 25 * pow(altura, 2)
        print("Você está com \033[1;31;40mOBESIDADE MÓRBIDA\033[m.")
        print("Com essa altura, para estar no peso ideal, você precisa ter entre {:.2f}kg e {:.2f}kg.".format(peso_ideal_minimo, peso_ideal_maximo))
        r = str(input("Deseja verificar novamente? [S/N]: ")).upper().strip()
