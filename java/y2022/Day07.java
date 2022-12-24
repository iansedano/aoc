package y2022;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import AocTools.Readers;

class Folder{
  String name;
  int size;
  List<Folder> subfolders;
  
  public Folder(String name){
    this.name = name;
    size = 0;
    subfolders = new ArrayList<Folder>();
  }
}
 

public class Day07 {
  public static void main(String[] args) throws IOException {
    String input = Readers.readText("y2022/day07.txt");
    
    System.out.println(Arrays.asList(input.split("$ cd")));
    
    // List<List<String>> commands = Arrays
    //   .asList(input.split("$ cd"))
    //   .stream()
    //   .map(chunk -> Arrays.asList(chunk.split("\n")))
    //   .collect(Collectors.toList());
    
    // System.out.println(commands.toString());
      
    // System.out.println(Day07.partOne());
    // System.out.println(Day07.partTwo());
  }

  static int partOne() {
    return 0;
  }

  static int partTwo() {
    return 0;
  }

}
