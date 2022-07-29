import re

from operators.node import Node
from operators.node_factory import NodeFactory
    
class QueryPlan:
    query: str
    tree_root: Node
    KEYWORDS: set[str] = { "select", "delete", "from", "where", "insert", "update", "join" }
    node_factory: NodeFactory = NodeFactory()
    
    def __init__(self, query_string: str):
        self.operators, self.args = self.get_split_query(query_string)
        self.tree = self.build_tree(self.operators, self.args)
        # self.show_tree()
        
    def build_tree(self, operators: list[str], args: list[str]):
        self.tree_root = self.node_factory.build(operators[0],args[0])
        cur_node = self.tree_root
        functions = list(zip(operators, args))
        next_token_index = 1
        while next_token_index < len(functions):
            self.add_node(cur_node, functions, next_token_index)
            next_token_index += 1

    def add_node(self, cur_node, functions, next_token_index):
        operator, arg = functions[next_token_index]
        cur_node.child = self.node_factory.build(operator, arg)
        cur_node = cur_node.child
            
    def get_split_query(self, query_string: str) -> tuple[list[str], list[str]]:
        pattern = " |".join(map(re.escape, self.KEYWORDS))
        operators = [operator.strip() for operator in re.findall(pattern, query_string)]
        args = [arg.strip() for arg in re.split(pattern, query_string)[1:]]
        return operators, args
    
    def show_tree(self):
        cur_node = self.tree_root
        while cur_node:
            print(cur_node)
            cur_node = cur_node.child
            
    def execute(self) -> list:
        outs = []
        try:
            while True:
                tuple = next(self.tree_root)
                outs.append(tuple)
        except StopIteration:
            return outs
