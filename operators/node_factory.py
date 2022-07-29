from .select import Select
from .frum import From

class NodeFactory:
    def build(self, operator: str, args: str):
        if operator == "select":
            return Select(args)
        elif operator == "from":
            return From(args)
        else:
            raise SyntaxError(f"Invalid token: `{operator}`")