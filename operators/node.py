class Node:    
    
    def __init__(self):
        self.child = None
        self.left = None
        self.right = None
        
    def __repr__(self) -> str:
        return type(self).__name__
    
    def __next__(self) -> tuple:
        raise NotImplementedError

    def __iter__(self):
        return self
