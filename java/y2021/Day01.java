package y2021;

import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Day01 {
  public static void main(String[] args) throws IOException {
    SolutionDay01 solution = new SolutionDay01();
    System.out.println(solution.partOne());
    System.out.println(solution.partTwo());
  }
}

class SolutionDay01 {
  List<String> lines;
  List<Integer> depths;

  public SolutionDay01() throws IOException {
    lines = read("y2021/day01.txt");
    depths = parseInts(lines);
  }

  List<Integer> parseInts(List<String> lines) {
    return lines.stream().map(Integer::parseInt).collect(Collectors.toList());
  }

  List<String> read(String path) throws IOException {
    return Files.readAllLines(Path.of(path));
  }

  int partOne() {
    int deeper = 0;
    
    List<Integer> a = depths.subList(0, depths.size() - 1);
    List<Integer> b = depths.subList(1, depths.size());
    
    for (int i = 0; i < a.size(); i++){
      if (a.get(i) < b.get(i)){
        deeper++;
      }
    }
    return deeper;
  }
  
  int partTwo() {
    int deeper = 0;
    
    List<Integer> a = depths.subList(0, depths.size() - 2);
    List<Integer> b = depths.subList(1, depths.size() - 1);
    List<Integer> c = depths.subList(2, depths.size());
    
    List<Integer> sums = new ArrayList<Integer>();
    
    for (int i = 0; i < a.size(); i++){
      sums.add(a.get(i) + b.get(i) + c.get(i));
    }
    
    List<Integer> sumsA = sums.subList(0, sums.size() - 1);
    List<Integer> sumsB = sums.subList(1, sums.size());
    
    for (int i = 0; i < sumsA.size(); i++){
      if (sumsA.get(i) < sumsB.get(i)) {
        deeper ++;
      }
    }
    
    return deeper;
  }
  
  
}
