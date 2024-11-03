#include "file_reader.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char **readLinesFromFile(const char *path, int *lineCount) {
  FILE *file = fopen(path, "r");
  if (file == NULL) {
    perror("Error opening file");
    return NULL;
  }

  char buffer[MAX_LINE_LENGTH];
  char **lines = NULL;
  int count = 0;

  while (fgets(buffer, MAX_LINE_LENGTH, file)) {
    // Resize the array of pointers
    char **temp = realloc(lines, sizeof(char *) * (count + 1));
    if (temp == NULL) {
      perror("Memory allocation failed");
      // Free previously allocated memory
      for (int i = 0; i < count; i++) {
        free(lines[i]);
      }
      free(lines);
      fclose(file);
      return NULL;
    }
    lines = temp;

    // Allocate memory for the line and copy it
    lines[count] = malloc(strlen(buffer) + 1);
    if (lines[count] == NULL) {
      perror("Memory allocation failed");
      for (int i = 0; i <= count; i++) {
        free(lines[i]);
      }
      free(lines);
      fclose(file);
      return NULL;
    }
    strcpy(lines[count], buffer);
    count++;
  }

  fclose(file);
  *lineCount = count;
  return lines;
}
