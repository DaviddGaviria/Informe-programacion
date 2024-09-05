# Declaramos las variables peso, altura y bmi
peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calculamos el índice de masa corporal (BMI)
bmi = peso / (altura * altura)

# Comprobamos en qué rango cae el BMI y mostramos el mensaje correspondiente
if bmi >= 18.5 and bmi < 22:
    print("Su condición es bajo peso")
elif bmi >= 22.1 and bmi < 24.9:
    print("Su condición es peso normal")
elif bmi >= 25 and bmi < 29.9:
    print("Su condición es sobrepeso")
elif bmi >= 30 and bmi < 34.9:
    print("Su condición es obesidad 1")
elif bmi >= 35 and bmi < 39.9:
    print("Su condición es obesidad 2")
elif bmi >= 40 and bmi < 49.9:
    print("Su condición es obesidad 3")
elif bmi >= 50:
    print("Su condición es obesidad 4")
