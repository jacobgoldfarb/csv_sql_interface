import re

class QueryParameters:
    
    param_order = ["select", "limit", "where", "from"]
    KEYWORDS: set[str] = { "select", "limit", "delete", "from", "where", "insert", "update", "join" }

    def __init__(self, query_string):
        self.parse_query(query_string)
        self.reorder_params()
    
    def parse_query(self, query_string: str) -> tuple[list[str], list[str]]:
        pattern = self.get_operator_parsing_regex_pattern()
        parsed_operators = re.findall(pattern, query_string)
        self.operators = [operator.strip().lower() for operator in parsed_operators]
        self.args = [arg.strip() for arg in re.split(pattern, query_string)[1:]]

    def get_operator_parsing_regex_pattern(self):
        pattern = " |".join(map(re.escape, self.KEYWORDS))
        pattern = pattern + "| " + pattern.upper()
        return pattern

    def reorder_params(self):
        function_lookup = {operator: self.args[i] for i, operator in enumerate(self.operators)}
        self.ordered_params = [(operator, function_lookup[operator]) for operator in self.param_order if operator in self.operators]
        
    def get_operators(self):
        return [param[0] for param in self.ordered_params]

    def get_args(self):
        return [param[1] for param in self.ordered_params]
        