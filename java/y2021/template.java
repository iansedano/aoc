package y2021;

import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;

import java.util.List;
import java.util.stream.Collectors;

public class template {
  public static void main(String[] args) throws IOException {
    SolutionDayX solution = new SolutionDayX();
    System.out.println(solution.partOne());
    System.out.println(solution.partTwo());
  }
}

class SolutionDayX {
  List<String> lines;
  List<Integer> depths;

  public SolutionDayX() throws IOException {
    lines = read("y2021/day__.txt");
    depths = parseInts(lines);
  }

  List<Integer> parseInts(List<String> lines) {
    return lines.stream().map(Integer::parseInt).collect(Collectors.toList());
  }

  List<String> read(String path) throws IOException {
    return Files.readAllLines(Path.of(path));
  }

  int partOne() {
    return 0;
  }
  
  int partTwo() {
    return 0;
  }
}
