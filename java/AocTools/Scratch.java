package AocTools;

import java.util.Arrays;

public class Scratch {
  public static void main(String[] args) {
    System.out.println(charNums('a'));
    System.out.println(charNums('z'));
    System.out.println(charNums('A'));
    System.out.println(charNums('Z'));
    
    Scratch.subLists();
  }
  
  public static int charNums(char ch){
    
    return (int) ch;
  }
  
  public static void subLists(){
    System.out.println(
    Arrays.asList(0,1,2,3,4,5,6,7,8,9,10).subList(0,11-2)
    );
  }
}
