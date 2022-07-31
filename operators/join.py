from .node import Node
from .frum import From

class Join(Node):
    
    fields: str
    is_header = True
    ARG_DELIMITER = ","
    
    def __init__(self, fields):
        super().__init__()
        tables = [table.strip() for table in fields.split(self.ARG_DELIMITER)]
        self.set_children(tables)

    def __next__(self) -> list[str]:
        tuple1 = next(self.left_child)
        tuple2 = next(self.right_child)
        return tuple1 + tuple2
    
    def set_children(self, tables):
        print("tables", tables)
        self.left_child, self.right_child = From(tables[0]), From(tables[1])