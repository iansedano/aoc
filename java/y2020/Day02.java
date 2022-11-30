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
      .map(splitline ->
        new EntryPart1(
          Integer.parseInt(splitline[0]),
          Integer.parseInt(splitline[1]),
          splitline[2].charAt(0),
          splitline[3]
        )
      )
      .collect(Collectors.toList());
  }

  List<String> read(String path) throws IOException {
    return Files.readAllLines(Path.of(path));
  }

  long partOne() {
    return this.inputs.stream().filter(entry -> entry.isValid).count();
  }

  int partTwo() {
    return 0;
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

    if (lower <= count & count <= upper) {
      isValid = true;
    } else isValid = false;
  }
}
