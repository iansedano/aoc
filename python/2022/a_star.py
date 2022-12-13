function Greedy(Graph, start, target):
    calculate the heurisitc value h(v) of starting node
    add the node to the opened list
    while True:
        if opened is empty:
        break # No solution found
        selecte_node = remove from opened list, the node with the minimun heuristic value
        if selected_node == target:
            calculate path
            return path
        add selected_node to closed list
        new_nodes = get the children of selected_node
        if the selected node has children:
            for each child in children:
              calculate the heuristic value of child
              if child not in closed and opened lists:
                  child.parent = selected_node
                  add the child to opened list
              else if child in opened list:
                  if the heuristic values of child is lower than the corresponding node in opened list:
                    child.parent = selected_node
                    add the child to opened list where h(v) is the sum of the distance of the v node from the initial node and the estimated cost from v node to the final node.