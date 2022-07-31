from .node import Node

class Limit(Node):
    
    fields: str
    limit: int
    count: int = 0
    is_header: bool = True

    def __init__(self, fields):
        super().__init__()
        self.fields = self.parse_args(fields)

    def __next__(self) -> list[str]:
        tuple = next(self.child)
        if self.is_header: 
            self.is_header = False
            return tuple
        else:
            if self.count == self.limit:
                raise StopIteration
            self.count += 1
            return tuple
    
    def parse_args(self, limit):
        try:
            self.limit = int(limit)
        except TypeError:
            raise SyntaxError("Invalid LIMIT argument.")
