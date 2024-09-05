#Bmi python

def calc_bmi(peso, altura):
    return peso / (altura * altura)


numerodepersonas = int(input("Ingrese el número de personas: "))


for i in range(1, numerodepersonas + 1):
    print(f"\nPersona {i}")
    
    
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    
    
    bmi = calc_bmi(peso, altura)
    
    
    print(f"Persona {i}: Su índice de masa corporal es {bmi:.2f} kg/m^2")


    
    



