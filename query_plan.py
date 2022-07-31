from operators.node import Node
from operators.node_factory import NodeFactory
from query_parameters import QueryParameters
    
class QueryPlan:
    query: str
    tree_root: Node
    node_factory: NodeFactory = NodeFactory()
    
    def __init__(self, query_string: str):
        query_params = QueryParameters(query_string)
        self.tree = self.build_tree(query_params)
        self.show_tree()
        
    def build_tree(self, query_params: QueryParameters):
        cur_node, functions = self.setup_tree(query_params)
        next_token_index = 1
        while next_token_index < len(functions):
            self.add_node(cur_node, functions, next_token_index)
            cur_node = cur_node.child
            next_token_index += 1

    def setup_tree(self, query_params):
        operators = query_params.get_operators()
        args = query_params.get_args()
        self.tree_root = self.node_factory.build(operators[0], args[0])
        cur_node = self.tree_root
        functions = list(zip(operators, args))
        return cur_node,functions

    def add_node(self, cur_node, functions, next_token_index):
        operator, arg = functions[next_token_index]
        cur_node.child = self.node_factory.build(operator, arg)
            
    def show_tree(self):
        cur_node = self.tree_root
        while cur_node:
            cur_node = cur_node.child
            
    def execute(self) -> list:
        outs = []
        try:
            while True:
                tuple = next(self.tree_root)
                outs.append(tuple)
        except StopIteration:
            return outs
