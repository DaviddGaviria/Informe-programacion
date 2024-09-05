#include <stdio.h>

int main() {
    int num_personas;
    float peso, altura, bmi;
    int bajo_peso = 0, peso_normal = 0, sobrepeso = 0;
    int obesidad_1 = 0, obesidad_2 = 0, obesidad_3 = 0, obesidad_4 = 0;

    printf("Ingrese el número de personas: ");
    scanf("%d", &num_personas);

    for (int i = 0; i < num_personas; i++) {
        printf("Ingrese el peso en kilogramos de la persona %d: ", i + 1);
        scanf("%f", &peso);

        printf("Ingrese la altura en metros de la persona %d: ", i + 1);
        scanf("%f", &altura);

        bmi = peso / (altura * altura);

        if (bmi >= 18.5 && bmi < 22) {
            bajo_peso++;
        } 
        else if (bmi >= 22.1 && bmi < 24.9) {
            peso_normal++;
        } 
        else if (bmi >= 25 && bmi < 29.9) {
            sobrepeso++;
        } 
        else if (bmi >= 30 && bmi < 34.9) {
            obesidad_1++;
        } 
        else if (bmi >= 35 && bmi < 39.9) {
            obesidad_2++;
        } 
        else if (bmi >= 40 && bmi < 49.9) {
            obesidad_3++;
        } 
        else if (bmi >= 50) {
            obesidad_4++;
        }
    }

    if (num_personas > 0) {
        printf("Porcentaje de personas con bajo peso: %.2f%%\n", (float)bajo_peso / num_personas * 100);
        printf("Porcentaje de personas con peso normal: %.2f%%\n", (float)peso_normal / num_personas * 100);
        printf("Porcentaje de personas con sobrepeso: %.2f%%\n", (float)sobrepeso / num_personas * 100);
        printf("Porcentaje de personas con obesidad 1: %.2f%%\n", (float)obesidad_1 / num_personas * 100);
        printf("Porcentaje de personas con obesidad 2: %.2f%%\n", (float)obesidad_2 / num_personas * 100);
        printf("Porcentaje de personas con obesidad 3: %.2f%%\n", (float)obesidad_3 / num_personas * 100);
        printf("Porcentaje de personas con obesidad 4: %.2f%%\n", (float)obesidad_4 / num_personas * 100);
    } else {
        printf("No se ingresaron datos.\n");
    }
    return 0;
}