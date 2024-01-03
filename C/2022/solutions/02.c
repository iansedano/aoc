#include <stdio.h>
#include <stdlib.h>

/**
 * rock > paper > scissors > rock ...
 *
 * This means that we can place these on a cycle:
 *
 * 0 > 1 > 2 > 0 > 1 > 2 ...
 *
 * The cycle can made by using modulo 3:
 *
 * o = opponent
 * draw = (o + 0) % 3
 * win = (o + 1) % 3
 * lose = (o + 2) % 3
 */
int main(void) {
  char buf[8];
  int scorePartOne = 0, scorePartTwo = 0;
  while (fgets(buf, sizeof(buf), stdin) != NULL) {
    char opponent = buf[0];
    char me = buf[2];

    // 0 rock, 1 paper, 2 scissors
    opponent %= 65;
    me %= 88;

    // Outcome 2 for win, 1 for loss and 0 for draw
    int outcome = (opponent - me + 3) % 3;

    // Flip loss and draw so 2 win, 1 draw, 0 loss
    // Which allows to multiply by 3 for score
    if (outcome < 2)
      outcome = outcome ^ 1;

    scorePartOne += me + 1 + (3 * outcome);

    /*
    Part 2

    Desired outcome + 2 = number of positions forward we need to be
    (opponent + number of positions forward) % 3 = toPlay
    */
    int desiredOutcome = me;
    int toPlay = (opponent + desiredOutcome + 2) % 3;
    scorePartTwo += toPlay + 1 + (3 * desiredOutcome);
  }
  printf("Part 1: %d\n", scorePartOne);
  printf("Part 1: %d\n", scorePartTwo);
  return EXIT_SUCCESS;
}
