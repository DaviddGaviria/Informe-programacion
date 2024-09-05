def calcular_bmi(peso, altura):
    return peso / (altura * altura)

def peso_ideal(altura):
    min_bmi = 22.1
    max_bmi = 24.9
    peso_min = min_bmi * (altura * altura)
    peso_max = max_bmi * (altura * altura)
    return (peso_min + peso_max) / 2

def evaluar_condicion(bmi):
    if bmi < 18.5:
        return "Bajo peso"
    elif 18.5 <= bmi < 22.0:
        return "Bajo peso"
    elif 22.1 <= bmi < 24.9:
        return "Peso normal"
    elif 25 <= bmi < 29.9:
        return "Sobrepeso"
    elif 30 <= bmi < 34.9:
        return "Obesidad 1"
    elif 35 <= bmi < 39.9:
        return "Obesidad 2"
    elif 40 <= bmi < 49.9:
        return "Obesidad 3"
    else:
        return "Obesidad 4"

def main():
    try:
        peso = float(input("Ingresa tu peso "))
        altura = float(input("Ingresa tu altura"))
        
        if altura <= 0:
            print("La altura debe ser mayor que cero.")
            return
    except ValueError:
        print("Por favor, ingresa números válidos decimales.")
        return

    bmi = calcular_bmi(peso, altura)
    
    condicion = evaluar_condicion(bmi)
    print(f"Tu condición es: {condicion}")
    
    if condicion != "Peso normal":
        peso_ideal_aprox = peso_ideal(altura)
        print(f"Tu peso ideal debería estar alrededor de {peso_ideal_aprox:.2f} kg.")

main()
