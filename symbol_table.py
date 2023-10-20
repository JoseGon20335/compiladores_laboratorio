#symbol_table.py
class symbol_table():
    def __init__(self):
        self.records = {}
        self.scopes = {}

    # Define el método iterador para que la clase sea iterable.
    def __iter__(self):
        return iter(self.records.items())

    def __len__(self):
        return len(self.records)

    """def addScope(self, scope):
        if scope not in self.scopes:
            self.scopes[scope] = {}

    def addChildScope(self, scope, child):
        if child not in self.scopes[scope]:
            self.scopes[scope][child] = {}"""

    def add(self, id, symbol, inherit, params, byte, offset):
        if inherit is not None:
            symbol.inherit = inherit

        if params is not None:
            symbol.params = params
        
        if byte is not None:
            symbol.byte = byte

        if offset is not None:
            symbol.offset = offset

        actualId = symbol.scope + '.' + id
        self.records[actualId] = symbol


    def lookup(self, id):
        for key in self.records:
            keySplit = key.split('.')
            if keySplit[len(keySplit)-1] == id:
                return self.records[key]
        
        return False
    

class symbol():
    def __init__(self, id, type, line, scope):
        self.id = id
        self.type = type
        self.line = line
        self.scope = scope
        self.inherit = None
        self.params = []
        self.byte = 0
        self.offset = 0