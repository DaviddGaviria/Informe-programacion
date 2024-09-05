def main():
    numero_personas = int(input("Ingrese el número de personas: "))
    
   
    bajo_peso = 0
    peso_normal = 0
    sobrepeso = 0
    obesidad_1 = 0
    obesidad_2 = 0
    obesidad_3 = 0
    obesidad_4 = 0

 
    for i in range(numero_personas):
        peso = float(input(f"Ingrese el peso en kilogramos de la persona {i+1}: "))
        altura = float(input(f"Ingrese la altura en metros de la persona {i+1}: "))

        bmi = peso / (altura * altura)

        
        if bmi < 18.5:
            bajo_peso += 1
        elif 18.5 <= bmi < 24.9:
            peso_normal += 1
        elif 25 <= bmi < 29.9:
            sobrepeso += 1
        elif 30 <= bmi < 34.9:
            obesidad_1 += 1
        elif 35 <= bmi < 39.9:
            obesidad_2 += 1
        elif 40 <= bmi < 49.9:
            obesidad_3 += 1
        elif bmi >= 50:
            obesidad_4 += 1

   
    if numero_personas > 0:
        print(f"\nPorcentaje de personas con bajo peso: {bajo_peso / numero_personas * 100:.2f}%")
        print(f"Porcentaje de personas con peso normal: {peso_normal / numero_personas * 100:.2f}%")
        print(f"Porcentaje de personas con sobrepeso: {sobrepeso / numero_personas * 100:.2f}%")
        print(f"Porcentaje de personas con obesidad 1: {obesidad_1 / numero_personas * 100:.2f}%")
        print(f"Porcentaje de personas con obesidad 2: {obesidad_2 / numero_personas * 100:.2f}%")
        print(f"Porcentaje de personas con obesidad 3: {obesidad_3 / numero_personas * 100:.2f}%")
        print(f"Porcentaje de personas con obesidad 4: {obesidad_4 / numero_personas * 100:.2f}%")
    else:
        print("No se ingresaron datos.")
    
if __name__ == "__main__":
    main()


