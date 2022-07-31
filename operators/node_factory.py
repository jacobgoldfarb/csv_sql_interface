from .select import Select
from .frum import From
from .where import Where
from .limit import Limit
from .join import Join
from .node import Node

class NodeFactory:
    def build(self, operator: str, args: str) -> Node:
        if operator == "select":
            return Select(args)
        elif operator == "from":
            if len(args.split(",")) > 1:
                return Join(args)
            return From(args)
        elif operator == "where":
            return Where(args)
        elif operator == "limit":
            return Limit(args)
        else:
            raise SyntaxError(f"Invalid token: `{operator}`")