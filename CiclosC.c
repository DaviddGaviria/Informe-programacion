
#include <stdio.h>


float calcBmi(float h, float w);


int main(){
    
    int numerodePersonas, i;

  
    printf("Ingrese el número de personas: ");
    scanf("%d", &numerodePersonas);

    float alturas[numerodePersonas], pesos[numerodePersonas], bmis[numerodePersonas];

  
    for (i = 0; i < numerodePersonas; i++) {
        
        printf("\nPersona %d:\n", i + 1);
        printf("Ingrese su altura en centímetros: ");
        scanf("%f", &alturas[i]);

        
        printf("Ingrese su peso en kilogramos: ");
        scanf("%f", &pesos[i]);

        
        bmis[i] = calcBmi(alturas[i], pesos[i]);
    }

    
    for (i = 0; i < numerodePersonas; i++) {
        printf("Persona %d: Su índice de masa corporal es %.2f kg/m^2\n", i + 1, bmis[i]);
    }

    return 0;
}


float calcBmi(float h, float w) {
    float bmi;

    
    bmi = w / ((h / 100.0) * (h / 100.0));
    return bmi;
}
