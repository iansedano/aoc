package y2022;

import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import AocTools.Readers;

public class Day05 {
  public static void main(String[] args) throws IOException {
    List<String> lines = Readers.readLines("y2022/day05.txt");
    List<Deque<Character>> stacks = Day05
      .parseStacks(lines.subList(0, 8));
    List<List<Integer>> instructions = Day05
      .parseInstructions(lines.subList(10, lines.size()));

    System.out.println(Day05.partOne(stacks, instructions));
    
    stacks = Day05
      .parseStacks(lines.subList(0, 8));
    System.out.println(Day05.partTwo(stacks, instructions));
  }
  
  static List<Deque<Character>> createStacks(int howMany){
    return IntStream
      .range(0, howMany)
      .mapToObj(i -> new LinkedList<Character>())
      .collect(Collectors.toList());
  }
  
  static Stream<List<Character>> parseStackLines(List<String> lines){
    return lines.stream()
      .map(line -> {
        List<Character> list = line
          .codePoints()
          .mapToObj(ch -> (char) ch)
          .skip(1) // Skip first "["
          .collect(Collectors.toList());
        
        return IntStream.range(0, list.size())
          .filter(n -> n % 4 == 0)
          .mapToObj(list::get)
          .collect(Collectors.toList());
      });
  }
  
  static void addToStacks(List<Character> row, List<Deque<Character>> stacks){
    ListIterator<Character> it = row.listIterator();

    while (it.hasNext()) {
      int idx = it.nextIndex();
      Character item = it.next();
      if (item != ' '){
        stacks.get(idx).addFirst(item);
      }
    }
  }
  
  static List<Deque<Character>> parseStacks(List<String> lines){
    List<Deque<Character>> stacks = Day05.createStacks(9);
    
    Day05.parseStackLines(lines)
      .forEach(row -> addToStacks(row, stacks));
    
    return stacks;
  }
  
  static List<List<Integer>> parseInstructions(List<String> lines){
    return lines.stream()
      .map(line -> {
        System.out.println("line");
        System.out.println(line.toString());
        List<String> split = Arrays.asList(line.split(" "));
        return Arrays.asList(
          Integer.parseInt(split.get(1)),
          Integer.parseInt(split.get(3)),
          Integer.parseInt(split.get(5))
        );
      })
      .collect(Collectors.toList());
  }
  
  static String partOne(
    List<Deque<Character>> stacks, List<List<Integer>> instructions
  ) {
    instructions.stream()
    .forEach(instruction -> {
      int howMany = instruction.get(0);
      int from = instruction.get(1) - 1;
      int to = instruction.get(2) - 1;
      
      IntStream.range(0, howMany)
      .forEach(i -> {
        stacks.get(to).addLast(
          stacks.get(from).pollLast()
        );
      });
    });
    
    return stacks
      .stream()
      .map(stack -> stack.pollLast().toString())
      .collect(Collectors.joining());
  }

  static String partTwo(
    List<Deque<Character>> stacks, List<List<Integer>> instructions
  ) {
    instructions.stream()
      .forEach(instruction -> {
        int howMany = instruction.get(0);
        int from = instruction.get(1) - 1;
        int to = instruction.get(2) - 1;
        
        List<Character> crane9001 = IntStream
          .range(0, howMany)
          .mapToObj(i -> stacks.get(from).removeLast())
          .collect(Collectors.toList());
        
        Collections.reverse(crane9001);
        
        crane9001
          .stream()
          .forEach(ch -> stacks.get(to).addLast(ch));
      });
    
    return stacks
      .stream()
      .map(stack -> stack.pollLast().toString())
      .collect(Collectors.joining());
  }

}
