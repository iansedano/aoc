from enum import Enum
from dataclasses import dataclass
from debug import p

class Token_type(Enum):
    NORMAL_OPEN = "("
    NORMAL_CLOSE = ")"
    CURLY_OPEN = "{"
    CURLY_CLOSE = "}"
    SQUARE_OPEN = "["
    SQUARE_CLOSE = "]"
    ANGLE_OPEN = "<"
    ANGLE_CLOSE = ">"

valid_tokens = "(){}[]<>"
open_tokens = "({[<"
close_tokens = ")}]>"

class Node_type(Enum):
    NORMAL = ")"
    CURLY = "}"
    SQUARE = "]"
    ANGLE = ">"
    ROOT = ""

class Node:
    def __init__(self, token):
        
        if token == "ROOT":
            self.type = Node_type.ROOT
        else:
            match token.type:
                case Token_type.NORMAL_OPEN:
                    self.type = Node_type.NORMAL
                case Token_type.CURLY_OPEN:
                    self.type = Node_type.CURLY
                case Token_type.SQUARE_OPEN:
                    self.type = Node_type.SQUARE
                case Token_type.ANGLE_OPEN:
                    self.type = Node_type.ANGLE
                case _:
                    raise Exception("INVALID TOKEN TO OPEN NODE")

        self.children: list[Node] = []
        
        self.closed = False
    
    def close(self):
        self.closed = True
        
    def __repr__(self):
        return str(self.type)

@dataclass
class Token:
    type: Token_type

def is_opening_token(token):
    match token.type:
        case Token_type.NORMAL_OPEN:
            return True
        case Token_type.CURLY_OPEN:
            return True
        case Token_type.SQUARE_OPEN:
            return True
        case Token_type.ANGLE_OPEN:
            return True
        case _:
            return False
            
def is_closing_token(token):
    match token.type:
        case Token_type.NORMAL_CLOSE:
            return True
        case Token_type.CURLY_CLOSE:
            return True
        case Token_type.SQUARE_CLOSE:
            return True
        case Token_type.ANGLE_CLOSE:
            return True
        case _:
            return False
            
def token_matches_parent(token, node):
    
    match node.type:
        case Node_type.NORMAL:
            if token.type == Token_type.NORMAL_OPEN or token.type == Token_type.NORMAL_CLOSE:
                return True
            else:
                return False
        case Node_type.CURLY:
            if token.type == Token_type.CURLY_OPEN or token.type == Token_type.CURLY_CLOSE:
                return True
            else:
                return False
        case Node_type.SQUARE:
            if token.type == Token_type.SQUARE_OPEN or token.type == Token_type.SQUARE_CLOSE:
                return True
            else:
                return False
        case Node_type.ANGLE:
            if token.type == Token_type.ANGLE_OPEN or token.type == Token_type.ANGLE_CLOSE:
                return True
            else:
                return False
        case Node_type.ROOT:
            print("THIS IS THE ROOT")
            return False
        case _:
            raise Exception("SOMETHING WENT WRONG WHEN TRYING TO MATCH TOKEN TO PARENT")

def build_tree(token_list: list[Token]) -> Node:
    def build_helper(token_gen, current_tok, parent_node):

        while current_tok is not None:
            
            if is_opening_token(current_tok):
                new_node = Node(current_tok)
                parent_node.children.append(new_node)
                current_tok = next(token_gen, None)
                build_helper(token_gen, current_tok, new_node)
            elif is_closing_token(current_tok):

                if token_matches_parent(current_tok, parent_node):
                    parent_node.close()
                    return
                else:
                    raise Exception(current_tok.type.value)
                    
            current_tok = next(token_gen, None)
    
    root = Node("ROOT")
    token_gen = (tok for tok in token_list)
    current_tok = next(token_gen, None)
    
    build_helper(token_gen, current_tok, root)
    
    return root
    
ILLEGAL_CHAR_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def print_tree(root, indent=0):
    print(root, root.closed)
    if indent == 0:
        print("ROOT", root)

    for child in root.children:
        for i in range(indent):
            print("\t", end="")
        
        print_tree(child, indent + 1)
        
def get_chars_to_close_open_tree(root):
    
    def helper(node, chars_to_close):
        if not node.closed:
            chars_to_close.append(node.type.value)

        for child in node.children:
            
            helper(child, chars_to_close)
    
    
    chars_to_close = []
    helper(root, chars_to_close)
    return [char for char in chars_to_close[:0:-1]]

POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
    }
    
def get_closing_char_score(chars):
    
    score = 0
    
    for char in chars:
        score *= 5
        score += POINTS[char]
    
    return score