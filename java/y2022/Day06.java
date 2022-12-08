package y2022;

import java.io.IOException;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import AocTools.Readers;

public class Day06 {
  public static void main(String[] args) throws IOException {
    List<Character> input = Readers.readCharList("y2022/day06.txt");
    
    System.out.println(Day06.partOne(input));
    System.out.println(Day06.partTwo(input));
  }
  
  static <T> boolean checkIfWindowUnique(
    List<T> iterable,
    int startIdx,
    int windowSize
  ){
    return IntStream
      .range(startIdx, startIdx + windowSize)
      .mapToObj(i -> iterable.get(i))
      .collect(Collectors.toSet())
      .size() == windowSize;
  }

  static int partOne(List<Character> input) {
    for (int i = 0; i != input.size(); i++){
      if (checkIfWindowUnique(input, i, 4)){
        return i + 4;
      }
    }
    return -1;
  }

  static int partTwo(List<Character> input) {
    for (int i = 0; i != input.size(); i++){
      if (checkIfWindowUnique(input, i, 14)){
        return i + 14;
      }
    }
    return -1;
  }

}
