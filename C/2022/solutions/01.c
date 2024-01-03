/**
 * https://adventofcode.com/2022/day/1
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * Based on @antirez
 */
int main(void) {
  char buf[64];
  long topThree[3] = {0}, sum = 0;

  while (fgets(buf, sizeof(buf), stdin) != NULL) {
    if (buf[0] != '\n' && buf[0] != '\r') {
      sum += strtol(buf, NULL, 10);
      continue;
    }

    // Update top three positions
    for (int i = 0; i < 3; i++) {
      if (topThree[i] < sum) {
        // Move positions down to accommodate new max
        for (int j = 2; j > i; j--) {
          topThree[j] = topThree[j - 1];
        }
        topThree[i] = sum;
        break;
      }
    }

    sum = 0;
  }

  long sumTopThree = 0;
  for (int i = 0; i < 3; i++) {
    sumTopThree += topThree[i];
  }

  printf("Part 1: %ld\n", topThree[0]);
  printf("Part 2: %ld\n", sumTopThree);
  return EXIT_SUCCESS;
}
