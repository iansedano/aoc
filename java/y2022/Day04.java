package y2022;

import java.io.IOException;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import AocTools.Readers;

public class Day04 {
  public static void main(String[] args) throws IOException {
    List<String> lines = Readers.readLines("y2022/day04.txt");
    List<List<int[]>> ranges = Day04.parse(lines);
    System.out.println(Day04.partOne(ranges));
    System.out.println(Day04.partTwo(ranges));
  }
  
  static List<List<int[]>> parse(List<String> lines){
    return lines
      .stream()
      .map(line -> Stream
        .of(line.split(","))
        .map(ranges -> Stream
            .of(ranges.split("-"))
            .mapToInt(i -> Integer.parseInt(i))
            .toArray()
        )
        .collect(Collectors.toList())
      )
      .collect(Collectors.toList());
  }
  
  static boolean isFullOverlap(int[] rangeA, int[] rangeB){
    int minA = rangeA[0];
    int maxA = rangeA[1];
    int minB = rangeB[0];
    int maxB = rangeB[1];
    
    return (minA <= minB && maxA >= maxB) || (minA >= minB && maxA <= maxB);
  }
  
  static boolean isAnyOverlap(int[] rangeA, int[] rangeB){
    int minA = rangeA[0];
    int maxA = rangeA[1];
    int minB = rangeB[0];
    int maxB = rangeB[1];
    
    return (minA <= maxB && maxA >= minB);
  }

  static int partOne(List<List<int[]>> rangePairs) {
    return rangePairs
      .stream()
      .mapToInt(ranges -> {
        int[] rangeA = ranges.get(0);
        int[] rangeB = ranges.get(1);
        
        return Day04.isFullOverlap(rangeA, rangeB) ? 1 : 0;
      })
      .sum();
  }

  static int partTwo(List<List<int[]>> rangePairs) {
    return rangePairs
      .stream()
      .mapToInt(ranges -> {
        int[] rangeA = ranges.get(0);
        int[] rangeB = ranges.get(1);
        
        return Day04.isAnyOverlap(rangeA, rangeB) ? 1 : 0;
      })
      .sum();
  }

}
