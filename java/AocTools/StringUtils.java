package AocTools;

import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StringUtils {
  
  public static void main(String[] args) {
    System.out.println(StringUtils.toIntList("Hello World").toString());
    System.out.println(StringUtils.toIntStream("Hello World").toString());
    System.out.println(StringUtils.toCharList("Hello World").toString());
    System.out.println(Arrays.toString(new String[] {"Hello", "World"}));
    System.out.println(Arrays.toString("Hello World".split("")));
    
    System.out.println(
      StringUtils.toSetSplitString("Hello, Hello").toString()
    );
    System.out.println(
      StringUtils.toSetSplitString_("Hello, Hello").toString()
    );
    System.out.println(
      StringUtils.toIntSetSplitString("Hello, Hello").toString()
    );
  }
  
  public static List<Integer> toIntList(String s){
    return s.codePoints().boxed().collect(Collectors.toList());
  }
  
  public static Stream<Integer> toIntStream(String s){
    return s.codePoints().boxed();
  }
  
  public static List<Character> toCharList(String s){
    return s.codePoints().mapToObj(c -> (char) c).collect(Collectors.toList());
  }
  
  public static Stream<Character> toCharStream(String s){
    return s.codePoints().mapToObj(c -> (char) c);
  }
  
  public static Stream<String> toListSplitString(String s){
    return s.codePoints().mapToObj(c -> String.valueOf((char) c));
  }
  
  public static Set<String> toSetSplitString(String s){
    return s
      .codePoints()
      .mapToObj(c -> String.valueOf((char) c))
      .collect(Collectors.toSet());
  }
  
  public static Set<String> toSetSplitString_(String s){
    return Stream.of(s.split("")).collect(Collectors.toSet());
  }
  
  public static Set<Integer> toIntSetSplitString(String s){
    return s.codePoints().boxed().collect(Collectors.toSet());
  }

  
}
