# saldo inicial $1000 menu

'''saldo = 1000
print("\t: Menu")
print("1. Deposite el dinero en la cuenta")
print("2. Retiro de dinero de la cuenta")
print("3. Consulte saldo disponible")
print("4. Salir")
opcion=int(input("Digite la opción del menu: "))
print()

if opcion == 1:
    deposito = float(input("Digite la cantidad del deposito: "))
    saldo += deposito # es lo mismo que escribir saldo = saldo + deposito
    print(f"Su nuevo saldo es: {saldo}")
elif opcion ==2:
    retiro = float(input("Digite la cantidad del retiro: "))
    if retiro > saldo:
        print("fondo insuficiente")
    else:
        saldo -= retiro
        print (f"El nuevo saldo es {saldo}")
elif opcion == 3:
    print (f"Su nuevo saldo es {saldo}")
elif opcion ==4:
    print("Gracias por su operación")
else:
    print("Operacion invalida")'''
     
# simplificar ek codigo con white 

saldo = 1000
print("\t: Menu")
print("1. Deposite el dinero en la cuenta")
print("2. Retiro de dinero de la cuenta")
print("3. Consulte saldo disponible")
print("4. Salir")
opcion=int(input("Digite la opción del menu: "))
print()
#while opcion > 0 and opcion < 4:
    if opcion == 1:
        deposito = float(input("Digite la cantidad del deposito: "))
        saldo += deposito # es lo mismo que escribir saldo = saldo + deposito
        print(f"Su nuevo saldo es: {saldo}")
    elif opcion ==2:
        retiro = float(input("Digite la cantidad del retiro: "))
        if retiro > saldo:
            print("fondo insuficiente")
        else:
            saldo -= retiro
            print (f"El nuevo saldo es {saldo}")
    elif opcion == 3:
        print (f"Su nuevo saldo es {saldo}")
    elif opcion ==4:
        print("Gracias por su operación")
    else:
        print("Operacion invalida")
        
    