package y2022;

import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

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
  List<Integer> depths;

  public SolutionDay01() throws IOException {
    this.text = Readers.readText("y2022/day01.txt");
  }

  int partOne() {
    String separator = System.getProperty("line.separator");
    return Collections.max(Arrays.stream(this.text
        .split(separator + separator))
        .map(elf -> {
          elf = elf.strip();
          return Arrays.stream(elf.split("\n"))
              .map(String::trim)
              .mapToInt(Integer::parseInt).sum();
        })
        .toList());
  }

  int partTwo() {
    String separator = System.getProperty("line.separator");
    return Arrays.stream(this.text
        .split(separator + separator))
        .map(elf -> {
          elf = elf.strip();
          return Arrays.stream(elf.split("\n"))
              .map(String::trim)
              .mapToInt(Integer::parseInt).sum();
        })
        .sorted(Comparator.reverseOrder())
        .limit(3)
        .mapToInt(i -> i)
        .sum();
  }
}
