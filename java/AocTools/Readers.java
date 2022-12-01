package AocTools;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class Readers {

  public static List<Integer> parseInts(List<String> lines) {
    return lines.stream().map(Integer::parseInt).collect(Collectors.toList());
  }

  public static String readText(String path) throws IOException {
    return new String(Files.readAllBytes(Paths.get(path)));
  }

  public static List<String> readLines(String path) throws IOException {
    return Files.readAllLines(Paths.get(path));
  }

}
