from .node import Node

class Select(Node):
    
    fields: str
    is_header = True
    is_wildcard = False
    indices = []
    WILDCARD = "*"
    ARG_DELIMITER = ","
    
    def __init__(self, fields):
        super().__init__()
        self.fields = self.parse_args(fields)

    def __next__(self) -> list[str]:
        tuple = self.parse_args(next(self.child)[0])
        if self.is_header: 
            self.set_indices(tuple)
            self.is_header = False
            return tuple if self.is_wildcard else self.fields
        return [tuple[i] for i in self.indices]
    
    def parse_args(self, header):
        return [attr.strip() for attr in header.split(self.ARG_DELIMITER)]

    def set_indices(self, header: list[str]):
        if self.WILDCARD in self.fields:
            self.is_wildcard = True
            self.indices = list(range(len(header)))
        else:
            self.indices = [i for i, field in enumerate(header) if field in self.fields]
        for field in self.fields:
            if field not in header and field != self.WILDCARD:
                raise SyntaxError(f"{field} not a valid attribute.")
