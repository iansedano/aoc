package y2022;

import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

import AocTools.Readers;

public class Day01 {
  public static void main(String[] args) throws IOException {
    SolutionDay01 solution = new SolutionDay01();
    System.out.println(solution.partOne());
    System.out.println(solution.partTwo());
  }
}

class SolutionDay01 {
  String text;
  List<Integer> elves;

  public SolutionDay01() throws IOException {
    this.text = Readers.readText("y2022/day01.txt");
    String separator = System.getProperty("line.separator");

    this.elves = Arrays.stream(this.text.split(separator + separator))
        .map(elf -> {
          elf = elf.strip();
          return Arrays.stream(elf.split("\n"))
              .map(String::trim)
              .mapToInt(Integer::parseInt).sum();
        })
        .collect(Collectors.toList());
  }

  int partOne() {
    return Collections.max(this.elves);
  }

  int partTwo() {
    return this.elves.stream()
        .sorted(Comparator.reverseOrder())
        .limit(3)
        .mapToInt(i -> i)
        .sum();
  }
}
