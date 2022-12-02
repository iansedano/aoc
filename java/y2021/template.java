package y2021;

import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;

import java.util.List;
import java.util.stream.Collectors;

import AocTools.Readers;

public class DayXX {
  public static void main(String[] args) throws IOException {
    System.out.println(DayXX.partOne());
    System.out.println(DayXX.partTwo());
  }

  static List<String> read() throws IOException {
    return Readers.readLines("y2021/day__.txt");
  }

  static int partOne() {
    return 0;
  }

  static int partTwo() {
    return 0;
  }

}
