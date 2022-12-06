package AocTools;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Readers {

  public static List<Integer> readInts(List<String> lines) {
    return lines.stream().map(Integer::parseInt).collect(Collectors.toList());
  }

  public static String readText(String path) throws IOException {
    return new String(Files.readAllBytes(Paths.get(path)));
  }

  public static List<String> readLines(String path) throws IOException {
    return Files.readAllLines(Paths.get(path)).stream()
        .filter(line -> line != "")
        .collect(Collectors.toList());
  }

  public static List<List<String>> readChunks(String path) throws IOException {
    return Arrays
        .stream(Readers.readText(path).split("\n\n"))
        .map(chunk -> Arrays
          .stream(chunk.split("\n"))
          .collect(Collectors.toList()))
        .collect(Collectors.toList());
  }

}
