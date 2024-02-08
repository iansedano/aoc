/**
 * https://adventofcode.com/2022/day/3
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 *
 */
int main(void) {
  char buf[64];
  int priorities = 0, groupMember = 2, groupPriorities = 0;
  char group[3][64];
  int groupLengths[3];
  while (fgets(buf, sizeof(buf), stdin) != NULL) {
    int length = strlen(buf) - 1;

    /* Part 1 */

    int half = length / 2;
    char samePartOne = '?';

    for (int i = 0; i < half; i++) {
      char itemA = buf[i];
      for (int j = half; j < length; j++) {
        char itemB = buf[j];
        if (itemA == itemB) {
          samePartOne = itemA;
          break;
        }
      }
      if (samePartOne != '?')
        break;
    }
    priorities += (samePartOne - 38) % 58;

    /* Part 2 */

    groupMember = (groupMember + 1) % 3;
    strncpy(group[groupMember], buf, length); // different lengths
    groupLengths[groupMember] = length;
    if (groupMember < 2)
      continue;

    int samePartTwo = '?';
    for (int i = 0; i < groupLengths[0]; i++) {
      for (int j = 0; j < groupLengths[1]; j++) {
        for (int k = 0; k < groupLengths[2]; k++) {

          if (group[0][i] == group[1][j] && group[1][j] == group[2][k]) {
            samePartTwo = group[0][i];
            break;
          }
        }
        if (samePartTwo != '?')
          break;
      }
      if (samePartTwo != '?')
        break;
    }
    if (samePartTwo == '?') {
      puts("FAIL\n");
      return EXIT_FAILURE;
    }
    groupPriorities += (samePartTwo - 38) % 58;
  }
  printf("Part 1: %d\n", priorities);
  printf("Part 1: %d\n", groupPriorities);
  return EXIT_SUCCESS;
}
