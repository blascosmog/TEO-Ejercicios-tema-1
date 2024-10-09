def pedir_altura ():
    altura_cm=int(input ("Ingrese su altura en cm: "))
    while altura_cm <10 or altura_cm>300:
        altura_cm=int(input("Altura no válida, introduzca su altura en cm: "))
    return  altura_cm

def pedir_peso ():
    peso_kg=int(input ("Ingrese su peso en cm: "))
    while peso_kg <10 or peso_kg>300:
        peso_kg=int(input("Peso no válido, introduzca su peso en kg: "))
    return  peso_kg

def calcular_imc (altura_cm, peso_kg):
    imc = peso_kg / (altura_cm / 100) ** 2
    return imc

if __name__ == "__main__":
    altura=pedir_altura()
    peso=pedir_peso()
    print ("Tu imc es de :", calcular_imc(altura,  peso)) 
