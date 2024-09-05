#include <stdio.h>

float peso, altura, bmi;

int main() {

    printf("Ingrese el peso en kilogramos: ");
    scanf("%f", &peso);

    printf("Ingrese su altura en metros: ");
    scanf("%f", &altura);

    bmi = peso / (altura * altura);

    if (bmi >= 18.5 && bmi < 22) {-{.}
        printf("Su condición es bajo peso\n");
    } 
    else if (bmi >= 22.1 && bmi < 24.9) {
        printf("Su condición es peso normal\n");
    } 
    else if (bmi >= 25 && bmi < 29.9) {
        printf("Su condición es sobrepeso\n");
    } 
    else if (bmi >= 30 && bmi < 34.9) {
        printf("Su condición es obesidad 1\n");
    } 
    else if (bmi >= 35 && bmi < 39.9) {
        printf("Su condición es obesidad 2\n");
    } 
    else if (bmi >= 40 && bmi < 49.9) {
        printf("Su condición es obesidad 3\n"); 
    } 
    else if (bmi >= 50) {
        printf("Su condición es obesidad 4\n"); }

    return 0;

}
   
    

