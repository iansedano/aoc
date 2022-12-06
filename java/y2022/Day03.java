package y2022;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import AocTools.Readers;
import AocTools.Partition;

public class Day03 {
  
  static String input;
  
  public static void main(String[] args) throws IOException {
    input = Readers.readText("y2022/day03.txt");
    System.out.println(Day03.partOne());
    System.out.println(Day03.partTwo());
  }
  
  static List<List<Set<Character>>> parseToDividedSacks(String input){
    return Stream.of(input.split("\n"))
      .map(line -> {
        int midPoint = Math.floorDiv(line.length(), 2);
        return Stream
          .of(
              line
                .substring(0, midPoint)
                .codePoints()
                .mapToObj(c -> (char) c)
                .collect(Collectors.toSet()),
              line
                .substring(midPoint, line.length())
                .codePoints()
                .mapToObj(c -> (char) c)
                .collect(Collectors.toSet())
            )
            .collect(Collectors.toList());
        })
        .collect(Collectors.toList());
  }
  
  static List<List<Set<Character>>> parseToGroups(String input){
    List<String> sacks = Arrays.asList(input.split("\n"));
    
    Partition<String> triple = new Partition<String>(sacks, 3);
    
    return triple
      .stream()
      .map(group -> group
        .stream()
        .map(sack -> sack
          .codePoints()
          .mapToObj(c -> (char) c)
          .collect(Collectors.toSet())
        )
        .collect(Collectors.toList())
      )
      .collect(Collectors.toList());
  }
  
  
  static int getPriority(char ch){
    return (ch - 38) % 58;
  }

  static long partOne() {

    return Day03
      .parseToDividedSacks(Day03.input)
      .stream()
      .mapToInt(sack -> {
        sack.get(0).retainAll(sack.get(1));
        return getPriority(sack.get(0).iterator().next());
      })
      .sum();
  }

  static int partTwo() {
    return Day03
      .parseToGroups(Day03.input)
      .stream()
      .mapToInt(group -> {
        group.get(0).retainAll(group.get(1));
        group.get(0).retainAll(group.get(2));
        return getPriority(group.get(0).iterator().next());
      })
      .sum();
  }
}

