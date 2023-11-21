#symbol_table.py
class symbol_table():
    def __init__(self):
        self.records = {}
        self.scopes = {}
        self.errors = []

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
    
    def getParams(self, id):
        for key in self.records:
            keySplit = key.split('.')
            if keySplit[len(keySplit)-1] == id:
                return self.records[key].params
        return False
    
    def addError(self, error):
        self.errors.append(error)


    def getSymbol(self, varName, scope):
        if varName != None and scope != None:
            validScopes = self.getValidScopes(scope)
            found = None

            for validScope in validScopes:
                fullName = validScope + "." + varName
                for key in self.records:
                    if key == fullName:
                        found = self.records[key]
                # if fullName in self.records:
                #     found = self.records[fullName]

            if found != None:
                return found
                
            if scope != "Object":
                return self.getSymbol(varName, "Object")

            # self.errors.append("getSymbol: Variable " + varName + " not declared")
        return None

    #REVISAR EL GETTYPE
    def getType(self, varName, scope):
        if varName != None and scope != None:
            validScopes = self.getValidScopes(scope)
            found = None

            for validScope in validScopes:
                fullName = validScope + "." + varName
                for key in self.records:
                    if key == fullName:
                        found = self.records[key]

            if found != None:
                return found.type
                
            if scope != "Object":
                return self.getType(varName, "Object")

            # self.errors.append("getSymbol: Variable " + varName + " not declared")
        return None

    def getValidScopes(self, scope):
        validScopes = ["global"]
        tempString = ""
        scopes = scope.split(".")

        for scope in scopes:
            if tempString != "":
                tempString += "."
            tempString += scope
            validScopes.append(tempString)
        return validScopes
    
    def classExists(self, className):
        key = "GLOBAL." + className
        # Verificamos si la clave existe
        if key in self.records:
            # Si decides añadir la propiedad isDryRun a la clase symbol, descomenta la siguiente línea
            # return not self.records[key].isDryRun
            return True
        else:
            return False

    def getAllInScope(self, scope):
        variables = []

        # Traverse the symbol table records.
        for key in self.records:
            # Check if the scope of the symbol matches the given scope.
            if self.records[key].scope == scope:
                # Add the symbol to the variables list.
                variables.append(self.records[key])

        # Return the list of variables in the given scope.
        return variables

class symbol():
    def __init__(self, id, type, line, scope):
        self.id = id
        self.type = type
        self.line = line
        self.scope = scope
        self.inherit = []
        self.params = []
        self.byte = -1
        self.offset = 0
        self.defineAsFunction = False
        self.returnType = None