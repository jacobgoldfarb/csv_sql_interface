import csv
from time import sleep
from .node import Node

class From(Node):
    cur_index = 0
    
    def __init__(self, table):
        super().__init__()
        self.table = table
        file_name = f'./data/{self.table}.csv'
        self.file = open(file_name, newline='')
        self.reader = csv.reader(self.file, delimiter=':', quoting=csv.QUOTE_NONE)

    def __next__(self) -> str:
        try:
            return next(self.reader)
        except StopIteration:
            self.file.close()
            raise