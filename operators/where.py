from .node import Node

class Where(Node):
    fields: str
    relevant_index: int
    predicate: callable
    is_header = True
    ARG_DELIMITER = "AND"
    predicate_operators = {"=", "<", ">", ">=", "<=", "!=", "in"}
    
    str_operator_lookup ={
                "=": lambda x, y: x == y,
                "<": lambda x, y: x < y,
                ">": lambda x, y: x > y,
                "<=": lambda x, y: x <= y,
                ">=": lambda x, y: x >= y,
                "!=": lambda x, y: x != y,
                # "in": lambda x,y: Where.set_in_predicate(x, y)
            }
    
    def __init__(self, fields):
        super().__init__()
        self.fields = self.parse_args(fields)

    def __next__(self) -> list[str]:
        if self.is_header:
            header = next(self.child)
            self.set_relevant_predicate_index(header)
            self.is_header = False
            return header
        while True:
            tuple = next(self.child)
            parsed_tuple = tuple[0].split(",")
            if self.predicate(parsed_tuple[self.relevant_index]):
                return tuple 

    def set_relevant_predicate_index(self, header):
        attributes = header[0].split(",")
        self.relevant_index = attributes.index(self.left_term)
    
    def parse_args(self, pred):
        pred = pred.lower()
        for op in self.predicate_operators:
            if op not in pred: continue
            operands = pred.split(op)
            self.left_term = operands[0].strip()
            # May be constant term
            self.right_term = operands[1].strip()
            if op == "=":
                self.predicate = lambda x: x == self.right_term
            elif op == "<":
                self.predicate = lambda x: x < self.right_term
            elif op == ">":
                self.predicate = lambda x: x > self.right_term
            elif op == "<=":
                self.predicate = lambda x: x <= self.right_term
            elif op == ">=":
                self.predicate = lambda x: x >= self.right_term
            elif op == "!=":
                self.predicate = lambda x: x != self.right_term
            elif op == "in":
                self.set_in_predicate()
            else:
                raise SyntaxError
    
    def set_in_predicate(self):
        if self.right_term[0] != "(" or self.right_term[-1] != ")":
            raise SyntaxError
        self.predicate = lambda x: str(x) in set(self.right_term[1:-1].split(","))

            