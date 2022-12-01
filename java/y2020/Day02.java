package y2020;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.stream.Collectors;

public class Day02 {

  public static void main(String[] args) throws IOException {
    SolutionDay02 solution = new SolutionDay02();
    System.out.println(solution.partOne());
    System.out.println(solution.partTwo());
  }
}

class SolutionDay02 {

  List<String> lines;
  List<EntryPart1> inputs;

  public SolutionDay02() throws IOException {
    this.lines = read("y2020/day02.txt");
    this.inputs = parseInputs(lines);
  }

  List<EntryPart1> parseInputs(List<String> lines) {
    return lines
        .stream()
        .map(line -> line.strip().split("[ -]"))
        .map(splitLine -> new EntryPart1(
            Integer.parseInt(splitLine[0]),
            Integer.parseInt(splitLine[1]),
            splitLine[2].charAt(0),
            splitLine[3]))
        .collect(Collectors.toList());
  }

  List<String> read(String path) throws IOException {
    return Files.readAllLines(Path.of(path));
  }

  long partOne() {
    return this.inputs.stream().filter(entry -> entry.isValid).count();
  }

  long partTwo() {
    return this.lines.stream()
        .map(line -> line.strip().split("[ -]"))
        .map(splitline -> new EntryPart2(
            Integer.parseInt(splitline[0]),
            Integer.parseInt(splitline[1]),
            splitline[2].charAt(0),
            splitline[3]))
        .filter(entry -> entry.isValid)
        .count();
  }
}

class EntryPart1 {

  int lower;
  int upper;
  char letter;
  String password;
  Boolean isValid;

  public EntryPart1(int lower, int upper, char letter, String password) {
    this.lower = lower;
    this.upper = upper;
    this.letter = letter;
    this.password = password;

    long count = password.chars().filter(ch -> ch == this.letter).count();

    isValid = lower <= count & count <= upper;
  }
}

class EntryPart2 {

  int posOne;
  int posTwo;
  char letter;
  String password;
  Boolean isValid;

  public EntryPart2(int lower, int upper, char letter, String password) {
    this.posOne = lower;
    this.posTwo = upper;
    this.letter = letter;
    this.password = password;

    this.isValid = password.charAt(posOne - 1) == this.letter ^
        password.charAt(posTwo - 1) == this.letter;
  }
}

// 0 != 0 False
// 1 != 0 True
// 0 != 1 True
// 1 != 1 False

// 0 + 0 = 0 == 1 False
// 1 + 0 = 1 == 1 True
// 0 + 1 = 1 == 1 True
// 1 + 1 = 2 == 1 False
