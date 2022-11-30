package y2021;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class Day02 {

  public static void main(String[] args) throws IOException {
    SolutionDay02 solution = new SolutionDay02();
    System.out.println(solution.partOne());
    System.out.println(solution.partTwo());
  }
}

class SolutionDay02 {

  List<String> lines;
  List<Instruction> instructions;
  List<InstructionBeta> instructionsBeta;

  public SolutionDay02() throws IOException {
    lines = read("y2021/day02.txt");
    instructions = parseInstructions(lines);
    instructionsBeta = parseInstructionsBeta(lines);
  }

  List<Instruction> parseInstructions(List<String> lines) {
    return lines
      .stream()
      .map(line -> new Instruction(line))
      .collect(Collectors.toList());
  }

  List<InstructionBeta> parseInstructionsBeta(List<String> lines) {
    return lines
      .stream()
      .map(line -> new InstructionBeta(line))
      .collect(Collectors.toList());
  }

  List<String> read(String path) throws IOException {
    return Files.readAllLines(Path.of(path));
  }

  int partOne() {
    int xPosition = 0;
    int yPosition = 0;

    for (Instruction instruction : instructions) {
      if (instruction.dimension == Dimension.X) xPosition += instruction.amount;
      if (instruction.dimension == Dimension.Y) yPosition += instruction.amount;
    }

    return xPosition * yPosition;
  }

  int partTwo() {
    int xPosition = 0;
    int yPosition = 0;
    int aim = 0;

    for (InstructionBeta instruction : instructionsBeta) {
      if (instruction.type == InstructionType.AIM) aim += instruction.amount;
      
      if (instruction.type == InstructionType.FORWARD) {
        xPosition += instruction.amount;
        yPosition += instruction.amount * aim;
      }
    }
    
    return xPosition * yPosition;
  }
}

enum Dimension {
  X,
  Y,
}

class Instruction {

  Dimension dimension;
  int amount;

  public Instruction(String line) throws NumberFormatException {
    String[] parts = line.split(" ");
    dimension = Objects.equals(parts[0], "forward") ? Dimension.X : Dimension.Y;
    amount = Integer.parseInt(parts[1]);

    if (Objects.equals(parts[0], "up")) amount *= -1;
  }
}

enum InstructionType {
  AIM,
  FORWARD,
}

class InstructionBeta {

  InstructionType type;
  int amount;

  public InstructionBeta(String line) throws NumberFormatException {
    String[] parts = line.split(" ");
    type =
      Objects.equals(parts[0], "forward")
        ? InstructionType.FORWARD
        : InstructionType.AIM;
    amount = Integer.parseInt(parts[1]);
    if (Objects.equals(parts[0], "up")) amount *= -1;
  }
}
