#include "file_reader.h"
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define DAY "01"
#define YEAR "2023"
#define PATH "inputs/" DAY ".in"


char* stripNonDigits(const char* str) {
    char* result = malloc(strlen(str) + 1);
    int j = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        if (isdigit(str[i])) {
            result[j++] = str[i];
        }
    }
    result[j] = '\0';
    return result;
}

int main() {
    int lineCount = 0;
    char **lines = readLinesFromFile(PATH, &lineCount);
    int* combinedIntegers = malloc(sizeof(int) * lineCount);
    
    if (lines == NULL) {
      return EXIT_FAILURE;
    }

    
    for (int i = 0; i < lineCount; i++) {
        char* cleanLine = stripNonDigits(lines[i]);
        int firstDigit = cleanLine[0] - '0';
        int lastDigit = cleanLine[strlen(cleanLine) - 1] - '0';
        combinedIntegers[i] = 10 * firstDigit + lastDigit;

        printf("Line %d: %s, Combined Int: %d\n", i, lines[i], combinedIntegers[i]);

        free(cleanLine);
        free(lines[i]); // Free each line
    }
    free(lines); // Free the array of pointers
    

    // Use combinedIntegers as needed

    free(combinedIntegers); // Don't forget to free this

    printf("\n");
    return EXIT_SUCCESS;
}
