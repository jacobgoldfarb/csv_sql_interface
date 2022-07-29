class Node:
    
    def __repr__(self) -> str:
        return type(self).__name__
    
    def __init__(self):
        self.child = None
        
    def __next__(self):
        raise NotImplementedError

    def __iter__(self):
        return self
