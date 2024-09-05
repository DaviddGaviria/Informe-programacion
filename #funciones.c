#include <stdio.h>

float calcularPesoIdeal(float altura) {
    float pesoIdealMin = 22.1 * (altura * altura);
    float pesoIdealMax = 24.9 * (altura * altura);
    return (pesoIdealMin + pesoIdealMax) / 2;
}

int main() {
    float peso, altura, bmi, pesoIdeal;
    printf("Ingrese el peso en kilogramos: ");
    if (scanf("%f", &peso) != 1) {
        printf("Error en la entrada de datos.\n");
        return 1; // Indica un error
    }
    printf("Ingrese su altura en metros: ");
    if (scanf("%f", &altura) != 1) {
        printf("Error en la entrada de datos.\n");
        return 1;
    }
    
    if (altura <= 0) {
        printf("La altura debe ser mayor que cero.\n");
        return 1;
    }
    bmi = peso / (altura * altura);

    if (bmi < 18.5) {
        printf("Su condición es bajo peso\n");
        pesoIdeal = calcularPesoIdeal(altura);
        printf("Su peso ideal para tener un BMI normal es aproximadamente %.2f kg.\n", pesoIdeal);
    } 
    else if (bmi >= 18.5 && bmi < 22) {
        printf("Su condición es bajo peso\n");
        pesoIdeal = calcularPesoIdeal(altura);
        printf("Su peso ideal para tener un BMI normal es aproximadamente %.2f kg.\n", pesoIdeal);
    } 
    else if (bmi >= 22.1 && bmi < 24.9) {
        printf("Su condición es peso normal\n");
    } 
    else if (bmi >= 25 && bmi < 29.9) {
        printf("Su condición es sobrepeso\n");
        pesoIdeal = calcularPesoIdeal(altura);
        printf("Su peso ideal para tener un BMI normal es aproximadamente %.2f kg.\n", pesoIdeal);
    } 
    else if (bmi >= 30 && bmi < 34.9) {
        printf("Su condición es obesidad 1\n");
        pesoIdeal = calcularPesoIdeal(altura);
        printf("Su peso ideal para tener un BMI normal es aproximadamente %.2f kg.\n", pesoIdeal);
    } 
    else if (bmi >= 35 && bmi < 39.9) {
        printf("Su condición es obesidad 2\n");
        pesoIdeal = calcularPesoIdeal(altura);
        printf("Su peso ideal para tener un BMI normal es aproximadamente %.2f kg.\n", pesoIdeal);
    } 
    else if (bmi >= 40 && bmi < 49.9) {
        printf("Su condición es obesidad 3\n");
        pesoIdeal = calcularPesoIdeal(altura);
        printf("Su peso ideal para tener un BMI normal es aproximadamente %.2f kg.\n", pesoIdeal);
    } 
    else if (bmi >= 50) {
        printf("Su condición es obesidad 4\n");
        pesoIdeal = calcularPesoIdeal(altura);
        printf("Su peso ideal para tener un BMI normal es aproximadamente %.2f kg.\n", pesoIdeal);
    }

    return 0;
}