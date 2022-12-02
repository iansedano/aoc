package y2022;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import AocTools.Readers;

public class Day02 {

  static Map<String, Integer> scoresPart1 = createScoresPart1();

  private static Map<String, Integer> createScoresPart1() {
    Map<String, Integer> scores = new HashMap<String, Integer>();
    scores.put("B X", 1);
    scores.put("C Y", 2);
    scores.put("A Z", 3);
    scores.put("A X", 4);
    scores.put("B Y", 5);
    scores.put("C Z", 6);
    scores.put("C X", 7);
    scores.put("A Y", 8);
    scores.put("B Z", 9);
    return scores;
  }

  static Map<String, Integer> scoresPart2 = createScoresPart2();

  private static Map<String, Integer> createScoresPart2() {
    Map<String, Integer> scores = new HashMap<String, Integer>();
    scores.put("B X", 1);
    scores.put("C X", 2);
    scores.put("A X", 3);
    scores.put("A Y", 4);
    scores.put("B Y", 5);
    scores.put("C Y", 6);
    scores.put("C Z", 7);
    scores.put("A Z", 8);
    scores.put("B Z", 9);
    return scores;
  }

  public static void main(String[] args) throws IOException {
    List<String> lines = Day02.read();
    System.out.println(Day02.partOne(lines));
    System.out.println(Day02.partTwo(lines));
  }

  static List<String> read() throws IOException {
    return Readers.readLines("y2022/day02.txt");
  }

  static int partOne(List<String> lines) {
    return lines.stream()
        .mapToInt(line -> {
          return Day02.scoresPart1.get(line);
        })
        .sum();

  }

  static int partTwo(List<String> lines) {
    return lines.stream()
        .mapToInt(line -> {
          return Day02.scoresPart2.get(line);
        })
        .sum();
  }

}
