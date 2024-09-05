#funcion2
def calcular_peso_ideal(altura):
    
    peso_ideal_min = 22.1 * (altura * altura)
    peso_ideal_max = 24.9 * (altura * altura)
    return (peso_ideal_min + peso_ideal_max) / 2  


peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))


if altura <= 0:
    print("La altura debe ser mayor que cero.")
else:
    
    bmi = peso / (altura * altura)

    # Comprobamos en qué rango cae el BMI y mostramos el mensaje correspondiente
    if bmi < 18.5:
        print("Su condición es bajo peso")
        peso_ideal = calcular_peso_ideal(altura)
        print(f"Su peso ideal para tener un BMI normal es aproximadamente {peso_ideal:.2f} kg.")
    elif bmi >= 18.5 and bmi < 22:
        print("Su condición es bajo peso")
        peso_ideal = calcular_peso_ideal(altura)
        print(f"Su peso ideal para tener un BMI normal es aproximadamente {peso_ideal:.2f} kg.")
    elif bmi >= 22.1 and bmi < 24.9:
        print("Su condición es peso normal")
    elif bmi >= 25 and bmi < 29.9:
        print("Su condición es sobrepeso")
        peso_ideal = calcular_peso_ideal(altura)
        print(f"Su peso ideal para tener un BMI normal es aproximadamente {peso_ideal:.2f} kg.")
    elif bmi >= 30 and bmi < 34.9:
        print("Su condición es obesidad 1")
        peso_ideal = calcular_peso_ideal(altura)
        print(f"Su peso ideal para tener un BMI normal es aproximadamente {peso_ideal:.2f} kg.")
    elif bmi >= 35 and bmi < 39.9:
        print("Su condición es obesidad 2")
        peso_ideal = calcular_peso_ideal(altura)
        print(f"Su peso ideal para tener un BMI normal es aproximadamente {peso_ideal:.2f} kg.")
    elif bmi >= 40 and bmi < 49.9:
        print("Su condición es obesidad 3")
        peso_ideal = calcular_peso_ideal(altura)
        print(f"Su peso ideal para tener un BMI normal es aproximadamente {peso_ideal:.2f} kg.")
    elif bmi >= 50:
        print("Su condición es obesidad 4")
        peso_ideal = calcular_peso_ideal(altura)
        print(f"Su peso ideal para tener un BMI normal es aproximadamente {peso_ideal:.2f} kg.")
