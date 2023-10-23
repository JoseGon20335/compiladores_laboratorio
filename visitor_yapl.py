#visitor_yapl.py
from antlr4 import *
from symbol_table import symbol_table, symbol
from antlr_build.grammarYaplVisitor import grammarYaplVisitor
from antlr_build.grammarYaplParser import grammarYaplParser

class visitor_yapl(grammarYaplVisitor):

    def __init__(self):
        self.symbol_table = symbol_table()
        self.scope = "GLOBAL"
        self.defaultMethods = {
            "IO": {"out_string": [["String"], "IO"], "out_int": [["Int"], "IO"], "in_string": [[], "String"], "in_int": [[], "Int"]},
            "Object": {"abort": [[], "Object"], "type_name": [[], "String"], "copy": [[], "SELF_TYPE"]},
            "String": {"length": [[], "Int"], "concat": [["String"], "String"], "substr": [["Int", "Int"], "String"]}
        }


    def diagnosis(self, ctx:grammarYaplParser.ProgramContext):
        print(type(ctx))
        print(dir(ctx))

    def visitProgram(self, ctx:grammarYaplParser.ProgramContext):
        # define default methods
        for value in self.defaultMethods:
            for method in self.defaultMethods[value]:
                newSymbol = symbol(method, self.defaultMethods[value][method][1], ctx.start.line, value)
                self.symbol_table.add(method, newSymbol, None, self.defaultMethods[value][method][0], None, None)

        # Add program to symbol table
        self.visitChildren(ctx)
    
    def get_symbol_table(self):
        temp = []
        for key, value in self.symbol_table.records.items():
            addValue = {
                'keyId': key,
                'type': str(value.type) if value.type is not None else "Unknown",
                'line': str(value.line) if value.line is not None else "Unknown",
                'scope': str(value.scope) if value.scope is not None else "Unknown",
                'inherit': str(value.inherit) if value.inherit is not None else "Unknown",
                'params': str(value.params) if value.params is not None else "Unknown",
                'byte': str(value.byte) if value.byte is not None else "Unknown",
                'offset': str(value.offset) if value.offset is not None else "Unknown"
            }
            temp.append(addValue)
        return temp
    
    def getByte(self, type):
        if type == "Int":
            return 8
        elif type == "String":
            return 1
        elif type == "Bool":
            return 1
        elif type == "SELF_TYPE" or type == "class":
            return 8
        else:
            return 8

    def visitClass_def(self, ctx:grammarYaplParser.Class_defContext):
        self.scope = str(ctx.TYPE_ID(0).getText())

        # Check if class already exists
        if self.symbol_table.classExists(self.scope):
            self.symbol_table.addError("Class " + self.scope + " already exists")

        inheritsFrom = []
        # Check if class inherits from a valid class
        if ctx.INHERITS():
            parent_name = str(ctx.TYPE_ID(1).getText())

            if not self.symbol_table.classExists(parent_name):
                self.symbol_table.addError("Class " + parent_name + " does not exist")

            if parent_name == "Main":
                self.symbol_table.addError("Main class cannot be inherited")

            if self.scope == parent_name:
                self.symbol_table.addError("Class " + self.scope + " cannot inherit from itself")

            parentClass = self.symbol_table.getSymbol(parent_name, self.scope)
            if parentClass is not None:
                inheritsFrom = [parentClass.varName]
                tempParent = parentClass

                while tempParent.inheritsFrom:
                    inheritsFrom.append(tempParent.inheritsFrom[0])
                    tempParent = self.symbol_table.getSymbol(tempParent.inheritsFrom[0], self.scope)

                parentMethods = self.symbol_table.getAllInScope(parent_name)
                for method in parentMethods:
                    print("Class " + self.scope + " inherits method " + method.varName)
                    self.symbol_table.addSymbol(method.varName, method.dataType, self.scope, method.line, method.numParams, method.paramTypes, isOverridable=True, isFunc=method.isFunc)

        newSymbol = symbol(self.scope, ctx.CLASS().getText(), ctx.start.line, self.scope)
        self.symbol_table.add(self.scope, newSymbol, inheritsFrom=inheritsFrom)

        # Visit children after validating class
        self.visitChildren(ctx)
    
    def visitFeature(self, ctx: grammarYaplParser.FeatureContext):
        # If both OBJECT_ID and TYPE_ID are present, it's an attribute or a method. 
        # Based on the earlier logic, it seems the presence of formal() indicates it's a method.
        if ctx.OBJECT_ID() and ctx.TYPE_ID():
            # Assign common values 
            currentSymbol = ctx.OBJECT_ID().getText()
            data_type = ctx.TYPE_ID(0).getText()
            line = ctx.start.line
            params = []
            types = []
            methodScope = self.scope + "." + currentSymbol
            oldScope = self.scope

            # Check if it's a method by the presence of formal() 
            if ctx.formal():
                for formal_ctx in ctx.formal():
                    params.append(formal_ctx.OBJECT_ID().getText())
                    types.append(formal_ctx.TYPE_ID().getText())

                # Add the method to the symbol table
                self.symbol_table.add(currentSymbol, data_type, self.scope, line, len(params), types, isFunc=True)
                self.scope = methodScope
                print("Method: " + currentSymbol)
            else:
                # It's an attribute, so add it to the symbol table
                newSymbol = symbol(currentSymbol, data_type, line, self.scope)
                byte = self.getByte(data_type)
                self.symbol_table.add(currentSymbol, newSymbol, None, None, byte, None)

            # Visit children after validating attribute/method
            self.visitChildren(ctx)

            # Return to old scope after visiting children of attribute/method
            self.scope = oldScope

    def visitFormal(self, ctx:grammarYaplParser.FormalContext):
        name = ctx.OBJECT_ID().getText()
        data_type = ctx.TYPE_ID().getText()
        newSymbol = symbol(name, data_type, ctx.start.line, self.scope)
        self.symbol_table.add(name, newSymbol, None, None, self.getByte(data_type), None)
        self.visitChildren(ctx)
    
    def visitAddSub(self, ctx:grammarYaplParser.AddSubContext):
        # Visit children first
        self.visitChildren(ctx)

        expressions = ctx.expr()
        expected = ["Bool", 'Int']
        out = "Bool"
        types = []

        for expr in expressions:
            for expected_exp in expected:
                if hasattr(expr, expected_exp):
                    types.append(out)
                    break
            else:
                types.append(self.symbolTable.getType(expr.getText(), self.currentScope))

        same = True
        for i in range(1, len(types)):
            if types[i] not in expected:
                same = False

        symbol = ctx.getText()

        if same:
            if hasattr(ctx, "ADD"):  # Adjust this check based on your actual implementation
                print("Add: Same type")
                newSymbol = symbol(symbol, "Int", ctx.start.line, self.scope)
                self.symbol_table.add(symbol, newSymbol, None, None, self.getByte("Int"), None)
            else:
                print("Substract: Same type")
                newSymbol = symbol(symbol, "Int", ctx.start.line, self.scope)
                self.symbol_table.add(symbol, newSymbol, None, None, self.getByte("Int"), None)
        else:
            if hasattr(ctx, "ADD"):  # Adjust this check based on your actual implementation
                # Logic for validateTypes integrated
                expected_type = "String"
                expr_type = self.symbolTable.getType(expressions[0].getText(), self.currentScope)
                sameString = expr_type == expected_type

                if sameString:
                    print("Add: Same type")
                else:
                    self.symbolTable.addError("Add operation with different or invalid types")
            else:
                self.symbolTable.addError("Substract operation with different or invalid types")
        
    def visitMinus(self, ctx:grammarYaplParser.MinusContext):
        self.visitChildren(ctx)
    
    def visitNew(self, ctx:grammarYaplParser.NewContext):
        symbol = ctx.getText()
        symbolType = ctx.TYPE_ID().symbol.text

        foundSymbol = False
        if self.symbolTable.getSymbol(symbolType, self.currentScope) is not None:
            foundSymbol = True

        if foundSymbol:
            inherited = self.symbolTable.getAllInScope(symbolType)

            for inheritedSymbol in inherited:
                print("New: Inherited symbol " + inheritedSymbol.varName)
                newSymbol = symbol(inheritedSymbol.varName, inheritedSymbol.dataType, ctx.start.line, self.currentScope)
                self.symbol_table.add(inheritedSymbol.varName, newSymbol, None, None, self.getByte(inheritedSymbol.dataType), None)

            print("New: Symbol found " + symbolType)
            newSymbol = symbol(symbol, symbolType, ctx.start.line, self.currentScope)
            self.symbol_table.add(symbol, newSymbol, None, None, self.getByte(symbolType), None)
        else:
            print("New: Symbol not found " + symbolType)
            self.symbolTable.addError("New: Symbol not found " + symbolType + " in line " + str(ctx.start.line))

        # Continues with visiting children
        self.visitChildren(ctx)
    
    def visitDispatch(self, ctx:grammarYaplParser.DispatchContext):
        # Visit children before validating
        self.visitChildren(ctx)

        symbol = ctx.OBJECT_ID().symbol.text
        expr = ctx.expr(0).getText()
        completeExpr = ctx.getText()
        type = self.symbolTable.getType(expr, self.currentScope)
        searchScope = self.currentScope

        inputTypes = []
        for i in range(1, len(ctx.expr())):
            inputTypes.append(self.symbolTable.getType(ctx.expr(i).getText(), self.currentScope))

        expr = ctx.expr(0).getText()
        if type == None:
            print("Dispatch: Symbol not found " + expr)
            return

        # Check if expr is a type
        if self.symbolTable.getSymbol(type, self.currentScope) != None:
            print("Dispatch: Symbol is of type " + type)
            searchScope = type
            
        if self.symbolTable.getSymbol(symbol, searchScope) != None:
            print("Dispatch: Symbol found " + symbol)

            symbolType = self.symbolTable.getSymbol(symbol, searchScope).dataType
            callingMethod = self.symbolTable.getSymbol(symbol, searchScope)

            if callingMethod == None:
                print("Dispatch: Symbol not found " + symbol)
                self.symbolTable.addError("Dispatch: Symbol not found " + symbol + " in line " + str(ctx.start.line))
            else:
                same = True
                if len(inputTypes) != len(callingMethod.paramTypes):
                    self.symbolTable.addError("Dispatch: Invalid number of parameters for " + symbol)
                    same = False
                else:
                    for i in range(len(callingMethod.paramTypes)):
                        if callingMethod.paramTypes[i] not in inputTypes and inputTypes[i] != "self":
                            same = False
                            self.symbolTable.addError("Dispatch: Invalid parameter type for " + symbol)

                if same:
                    print("Dispatch: Symbol found " + symbol + " with valid input types")
                    newSymbol = symbol(completeExpr, symbolType, ctx.start.line, self.scope)
                    self.symbol_table.add(completeExpr, newSymbol, None, None, self.getByte(symbolType), None)
                else:
                    print("Dispatch: Symbol not found " + symbol)
        else:
            print("Dispatch: Symbol not found " + symbol)

    
    def visitString(self, ctx:grammarYaplParser.StringContext):
        name = ctx.STRING().getText()
        type = "String"
        print("String ", name)
        newSymbol = symbol(name, type, ctx.start.line, self.scope)
        self.symbol_table.add(ctx.STRING().getText(), newSymbol, None, None, self.getByte("String"), None)
        self.visitChildren(ctx)
    
    def visitBool(self, ctx:grammarYaplParser.BoolContext):
        name = ctx.BOOL().getText()
        type = "Bool"
        print("Bool ", name)
        newSymbol = symbol(name, type, ctx.start.line, self.scope)
        self.symbol_table.add(ctx.TYPE_ID(0), newSymbol, None, None, self.getByte("Bool"), None)
        self.visitChildren(ctx)
        
    def visitMulDiv(self, ctx: grammarYaplParser.MulDivContext):
        # Visit children first
        self.visitChildren(ctx)

        expressions = ctx.expr()
        expected = ["Bool", 'Int']
        out = "Bool"
        types = []

        # Logic from validateVariousTypes starts here
        for expr in expressions:
            for expected_exp in expected:
                if hasattr(expr, expected_exp):
                    types.append(out)
                    break
            else:
                types.append(self.symbolTable.getType(expr.getText(), self.scope))

        same = True
        for i in range(1, len(types)):
            if types[i] not in expected:
                same = False

        # Now, based on the result, determine the operation
        symbol = ctx.getText()
        if ctx.MULT():  # Replace `MUL` with the correct token or method if it's different
            operation = "Multiply"
        elif ctx.DIV():  # Replace `DIV` with the correct token or method if it's different
            operation = "Divide"
        else:
            operation = "Unknown"

        # Validate the operation
        if same == True:
            print(f"{operation}: Same type")
            newSymbol = symbol(symbol, "Int", ctx.start.line, self.scope)
            self.symbol_table.add(symbol, newSymbol, None, None, self.getByte("Int"), None)
        else:
            self.symbolTable.addError(f"{operation} operation with different or invalid types")

    def visitIsvoid(self, ctx:grammarYaplParser.IsvoidContext):
        self.visitChildren(ctx)

    def visitInteger(self, ctx:grammarYaplParser.IntegerContext):
        name = ctx.INTEGER().getText()
        newSymbol = symbol(ctx.INTEGER().getText(), "Int", ctx.start.line, self.scope)
        self.symbol_table.add(name, newSymbol, None, None, self.getByte("Int"), None)
        self.visitChildren(ctx)
    
    def visitStatic_dispatch(self, ctx:grammarYaplParser.Static_dispatchContext):
        # Visit children first
        self.visitChildren(ctx)

        symbol = ctx.getText()

        inputTypes = []
        # Assuming the syntax in your grammar for `expr` is consistent with `yaplParser`, 
        # if not, modify this part accordingly
        for expr in ctx.expr():
            inputTypes.append(self.symbolTable.getType(expr.getText(), self.scope))

        # Assuming the syntax in your grammar for `OBJECT_ID` is consistent with `yaplParser`, 
        # if not, modify this part accordingly
        callingMethod = self.symbolTable.getSymbol(ctx.OBJECT_ID().symbol.text, self.scope)

        if callingMethod == None:
            print("Static Dispatch: Symbol not found " + symbol)
            self.symbolTable.addError("Static Dispatch: Symbol not found " + symbol + " in line " + str(ctx.start.line))
        else:
            same = True
            if len(inputTypes) != len(callingMethod.paramTypes):
                same = False
                self.symbolTable.addError("Static Dispatch: Invalid number of parameters for " + symbol)
            else:
                for i in range(len(callingMethod.paramTypes)):
                    if callingMethod.paramTypes[i] not in inputTypes:
                        same = False
                        self.symbolTable.addError("Static Dispatch: Invalid parameter type for " + symbol)

            if same:
                print("Static Dispatch: Symbol found " + symbol + " with valid input types")
                symbolType = callingMethod.dataType
                newSymbol = symbol(symbol, symbolType, ctx.start.line, self.scope)
                self.symbol_table.add(symbol, newSymbol, None, None, self.getByte(symbolType), None)
            else:
                print("Static Dispatch: Symbol not found " + symbol)

    def visitWhile(self, ctx:grammarYaplParser.WhileContext):
        # Visit children first
        self.visitChildren(ctx)

        symbol = ctx.getText()
        
        expr = ctx.expr(0).getText()
        type = self.symbolTable.getType(expr, self.scope)

        # Check if expr is a type
        if type in self.symbolTable.symbolTable:
            print("While: Symbol is of type " + type)
            expr = type

        if self.symbolTable.getSymbol(expr, self.scope) != None:
            print("While: Symbol found " + expr)

            symbolType = self.symbolTable.getSymbol(expr, self.scope).dataType
            newSymbol = symbol(symbol, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbol, newSymbol, None, None, self.getByte(symbolType), None)
        else:
            print("While: Symbol not found " + expr)

    def visitComparison(self, ctx:grammarYaplParser.ComparisonContext):
        # Visit children first
        self.visitChildren(ctx)

        expressions = ctx.expr()
        expected = ["Bool", 'Int']
        out = "Bool"
        types = []

        for expr in expressions:
            for expected_exp in expected:
                if hasattr(expr, expected_exp):
                    types.append(out)
                    break
            else:
                types.append(self.symbolTable.getType(expr.getText(), self.scope))

        same = True
        for i in range(1, len(types)):
            if types[i] not in expected:
                same = False

        symbol = ctx.getText()

        if same:
            print("Compare: Same type")
            newSymbol = symbol(symbol, "Bool", ctx.start.line, self.scope)
            self.symbol_table.add(symbol, newSymbol, None, None, self.getByte("Bool"), None)
        else:
            self.symbolTable.addError("Compare operation with different or invalid types")
    
    def visitParenthesis(self, ctx:grammarYaplParser.ParenthesisContext):
        self.visitChildren(ctx)
        name = ctx.expr().getText()
        type = self.symbol_table.getSymbol(name, self.scope).type

        if type != None:
            print("Parenthesis: Symbol found " + name)
            newSymbol = symbol(name, type.dataType, ctx.start.line, self.scope)
            self.symbol_table.add(name, newSymbol, None, None, self.getByte(type.dataType), None)
        else:
            print("Parenthesis: Symbol not found " + name)

    
    def visitObject_id(self, ctx:grammarYaplParser.Object_idContext):
        print("Object_id ", ctx.OBJECT_ID().getText())
    
    def visitNeg(self, ctx:grammarYaplParser.NegContext):
        # Visit children before validating
        self.visitChildren(ctx)

        symbol = ctx.getText()
        expr = ctx.expr().getText()
        type = self.symbolTable.getType(expr, self.currentScope)

        # Check if expr is a type
        if type in self.symbolTable.symbolTable:
            print("Neg: Symbol is of type " + type)
            expr = type

        if self.symbolTable.getSymbol(expr, self.currentScope) != None:
            print("Neg: Symbol found " + expr)
            symbolType = self.symbolTable.getSymbol(expr, self.currentScope).dataType
            newSymbol = symbol(symbol, symbolType, ctx.start.line, self.currentScope)
            self.symbol_table.add(symbol, newSymbol, None, None, self.getByte(symbolType), None)
        else:
            print("Neg: Symbol not found " + expr)

    def visitNot(self, ctx: grammarYaplParser.NotContext):
        # Visit children before validating
        self.visitChildren(ctx)

        symbol_text = ctx.getText()
        expr = ctx.expr().getText()

        # Obtain type from symbol table
        type = self.symbolTable.getType(expr, self.scope)

        # Check if expr is a type
        if type in self.symbolTable.symbolTable:
            print("Not: Symbol is of type " + type)
            expr = type

        # Check if the symbol exists in the symbol table
        found_symbol = self.symbolTable.getSymbol(expr, self.scope)

        if found_symbol:
            print("Not: Symbol found " + expr)
            symbolType = found_symbol.dataType
            newSymbol = symbol(symbol_text, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbol_text, newSymbol, None, None, self.getByte(symbolType), None)
        else:
            print("Not: Symbol not found " + expr)

    def visitSelf(self, ctx:grammarYaplParser.SelfContext):
        name = ctx.getText()
        type = "SELF_TYPE"
        print("Self ", name)
        newSymbol = symbol(name, type, ctx.start.line, self.scope)
        self.symbol_table.add(name, newSymbol, None, None, self.getByte(type), None)
        self.visitChildren(ctx)
    
    def visitBlock(self, ctx:grammarYaplParser.BlockContext):
        self.visitChildren(ctx)
        print("Block ", ctx.getText())
    
    def visitLet(self, ctx:grammarYaplParser.LetContext):
        newSymbol = symbol(ctx.LET().getText(), "LET", ctx.start.line, self.scope)
        print("Let ", ctx.getText())
        self.symbol_table.add(ctx.LET().getText(), newSymbol, None, None, self.getByte("Let"), None)
        for i in range(len(ctx.OBJECT_ID())):
            if(ctx.TYPE_ID(i) != None):
                name = ctx.OBJECT_ID(i).getText()
                data_type = ctx.TYPE_ID(i).getText()
                newSymbol = symbol(name, data_type, ctx.start.line, self.scope)
                print("Let ", name, data_type)
                self.symbol_table.add(name, newSymbol, None, None, self.getByte(data_type), None)
        self.visitChildren(ctx)
    
    def visitIf(self, ctx: grammarYaplParser.IfContext):
        # Visit children before validating
        self.visitChildren(ctx)

        # Get symbol and expression
        symbol_text = ctx.IF().getText()
        expr = ctx.expr(0).getText()

        # Obtain type from symbol table
        type = self.symbolTable.getType(expr, self.scope)

        # Check if expr is a type
        if type in self.symbolTable.symbolTable:
            print("If: Symbol is of type " + type)
            expr = type

        # Check if the symbol exists in the symbol table
        found_symbol = self.symbolTable.getSymbol(expr, self.scope)

        if found_symbol:
            print("If: Symbol found " + expr)
            symbolType = found_symbol.dataType
            newSymbol = symbol(symbol_text, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbol_text, newSymbol, None, None, self.getByte(symbolType), None)
        else:
            print("If: Symbol not found " + expr)

    def visitAssign(self, ctx: grammarYaplParser.AssignContext):
        # Visit children before validating
        self.visitChildren(ctx)

        currentSymbol = str(ctx.OBJECT_ID())
        symbolType = self.symbolTable.getType(currentSymbol, self.scope)
        type = self.symbolTable.getType(ctx.expr().getText(), self.scope)

        # Check if the current symbol is in the symbol table
        if symbolType == None:
            # Add error to the symbol table
            self.symbolTable.addError("Assign: Symbol not found " + currentSymbol)
            return

        # Implicit casting validation
        if (symbolType == "Bool" and type == "Int") or (symbolType == "Int" and type == "Bool"):
            print("Assign: Implicit casting")
        elif symbolType != type and type != "SELF_TYPE":
            symbolTypeInstance = self.symbolTable.getSymbol(symbolType, self.scope)
            typeInstance = self.symbolTable.getSymbol(type, self.scope)

            # Check if there's any inheritance relationship that can be used for casting
            if (type in symbolTypeInstance.inheritsFrom) or (symbolType in typeInstance.inheritsFrom):
                print("Assign: Implicit casting with inheritance")
            else:
                # Add error to the symbol table
                error_msg = f"Invalid type for {currentSymbol}: {symbolType} trying to assign {type}"
                self.symbolTable.addError(error_msg)

class bottomUpValidator(grammarYaplVisitor):


    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        print(self.symbol_table.scopes)

    def visitDeep(self, ctx):
        if not hasattr(ctx, 'children'):
            #print("   *|   ",ctx.getText(), type(ctx))
            #print("     *   ",self.symbol_table.lookup(ctx.getText()))
            #print("     *   ",ctx.getParent().getText())
            #print("     *   ", type(ctx.getParent()))
            #print("     *   ", ctx.getText())
            #print("     *   ", dir(ctx))
            if self.symbol_table.lookup(ctx.getText()) != False: 
                self.goUp(ctx)


            # handle terminal nodes

            #return self.visit(ctx)
        else:
            #results = [self.visitDeep(child) for child in ctx.children]
            #return all(results)
            for child in ctx.children:
                self.visitDeep(child)
            
            # handle non terminal nodes

    def goUp(self, ctx):
        print("     *   ",ctx.getText(), type(ctx))
        self.visit(ctx.getParent())
        if hasattr(ctx.getParent(), 'getParent'):
            self.goUp(ctx.getParent())




    def visitAddSub(self, ctx):
        # Esto se asegura de que se comprueben los casteos y que los valores que se están operando sean válidos entre ellos
        child_types = [self.visit(child) for child in ctx.children]
        sumando1 = ctx.children[0]
        sumando2 = ctx.children[2]

        type_sumando1 = type(sumando1)
        type_sumando2 = type(sumando2)

        isTable1 = self.symbol_table.lookup(sumando1.getText())
        isTable2 = self.symbol_table.lookup(sumando2.getText())

        type_table1 = isTable1.type if isTable1 != False else None
        type_table2 = isTable2.type if isTable2 != False else None

        #print("    '   ", sumando1.getText(), type_sumando1, isTable1, type_table1)
        #print("    '   ", sumando2.getText(), type_sumando2, isTable2, type_table2)
#
        ## existen 3 tipos de match: que type_table y type_table sean iguales, que type_sumando y type_table sean correspondientes entre ellos, o que type_sumando y type_sumando sean correspondientes entre ellos
#
        ## type_sumando1 y type_sumando2 son iguales
        #print("    '   ", self.translateType(type_sumando1), self.translateType(type_sumando2))
        #print("    '   ", type_table1, type_table2)

        if type_sumando1 == type_sumando2 and self.translateType(type_sumando1) != "Bool" and self.translateType(type_sumando1) != "String":
            #print(" Scott Pilgrim")
            ctx.__class__ = type_sumando1

        # type_sumando1 y type_table1 son iguales
        elif self.translateType(type_sumando1) == type_table2 and self.translateType(type_sumando1) != "Bool" and self.translateType(type_sumando1) != "String":
            #print(" Ramona Flowers")
            ctx.__class__ = type_sumando1

        elif self.translateType(type_sumando1) == "Int" and type_table2 == "Bool":
            #print(" Envy Adams")
            ctx.__class__ = type_sumando1
        else:
            print("ERROR: Cannot add unmatching types of values. Expected Int + Int or Int + Bool")
            #exit(1)

    def visitMinus(self, ctx):
        child_types = [self.visit(child) for child in ctx.children]
        minuendo = ctx.children[0]
        sustraendo = ctx.children[2]

        type_minuendo = type(minuendo)
        type_sustraendo = type(sustraendo)

        isTable1 = self.symbol_table.lookup(minuendo.getText())
        isTable2 = self.symbol_table.lookup(sustraendo.getText())

        type_table1 = isTable1.type if isTable1 != False else None
        type_table2 = isTable2.type if isTable2 != False else None

        if type_minuendo == type_sustraendo and self.translateType(type_minuendo) != "Bool" and self.translateType(type_minuendo) != "String":
            ctx.__class__ = type_minuendo

        elif self.translateType(type_minuendo) == type_table2 and self.translateType(type_minuendo) != "Bool" and self.translateType(type_minuendo) != "String":
            ctx.__class__ = type_minuendo

        elif self.translateType(type_minuendo) == "Int" and type_table2 == "Bool":
            ctx.__class__ = type_minuendo

        else:
            print("ERROR: Cannot substract unmatching types of values. Expected Int - Int or Int - Bool")
            #exit(1)



    def visitMulDiv(self, ctx):
        child_types = [self.visit(child) for child in ctx.children]

        multiplicando = ctx.children[0]
        multiplicador = ctx.children[2]

        type_multiplicando = type(multiplicando)
        type_multiplicador = type(multiplicador)

        isTable1 = self.symbol_table.lookup(multiplicando.getText())
        isTable2 = self.symbol_table.lookup(multiplicador.getText())

        type_table1 = isTable1.type if isTable1 != False else None
        type_table2 = isTable2.type if isTable2 != False else None

        if type_multiplicando == type_multiplicador and self.translateType(type_multiplicando) != "Bool" and self.translateType(type_multiplicando) != "String":
            ctx.__class__ = type_multiplicando
        elif self.translateType(type_multiplicando) == type_table2 and self.translateType(type_multiplicando) != "Bool" and self.translateType(type_multiplicando) != "String":
            ctx.__class__ = type_multiplicando
        elif self.translateType(type_multiplicando) == "Int" and type_table2 == "Bool":
            ctx.__class__ = type_multiplicando
        else:
            print("ERROR: Cannot multiply unmatching types of values. Expected Int * Int or Int * Bool")
            #exit(1)

    def visitEq(self, ctx):
        child_types = [self.visit(child) for child in ctx.children]
        print(ctx.__class__)
        comparando1 = ctx.children[0]
        print(ctx.children[1].getText())
        comparando2 = ctx.children[2]

        type_comparando1 = type(comparando1)
        type_comparando2 = type(comparando2)

        isTable1 = self.symbol_table.lookup(comparando1.getText())
        isTable2 = self.symbol_table.lookup(comparando2.getText())

        type_table1 = isTable1.type if isTable1 != False else None
        type_table2 = isTable2.type if isTable2 != False else None

        if type_comparando1 == type_comparando2 and self.translateType(type_comparando1) != "Bool" and self.translateType(type_comparando1) != "String":
            ctx.__class__ = type_comparando1
        elif self.translateType(type_comparando1) == type_table2 and self.translateType(type_comparando1) != "Bool" and self.translateType(type_comparando1) != "String":
            ctx.__class__ = type_comparando1
        elif self.translateType(type_comparando1) == "Int" and type_table2 == "Bool":
            ctx.__class__ = type_comparando1
        else:
            print("ERROR: Cannot compare unmatching types of values. Expected Int == Int or Int == Bool")
            #exit(1)
        print(ctx.__class__)


        
    def translateType(self, type):
        if type == grammarYaplParser.IntegerContext:
            return "Int"
        elif type == grammarYaplParser.StringContext:
            return "String"
        elif type == grammarYaplParser.BoolContext:
            return "Bool"
        
    
    def visitAssign(self, ctx):
        #print('-' * 50)
        #print("LLEGAMOS ASIGNACION!")
        #print("         - ", ctx.__class__)
        #print(ctx.getText())
        child_types = [self.visit(child) for child in ctx.children]
        #print(child_types)
        asignando = ctx.children[0] # variable que recibe
        asignado = ctx.children[2] # valor que se asigna
        isTable1 = self.symbol_table.lookup(asignando.getText())
        isTable2 = self.symbol_table.lookup(asignado.getText())

        if isTable1 != False and isTable2 != False:
            # mismo tipo de dato
            if isTable1.type == isTable2.type:
                # asignación de una variable a otra variable
                #rint("Asignación de una variable a otra variable")
                contexto = { 'Int': grammarYaplParser.IntegerContext, 'Bool': grammarYaplParser.BoolContext, 'String': grammarYaplParser.StringContext, 'SELF_TYPE': grammarYaplParser.SelfContext }
                ctx.__class__ = contexto[isTable1.type]
                #print("         // ", ctx.__class__)
                #return contexto[isTable1.type]
            else:
                # reglas de casteo y asignacion
                if isTable1.type == "Int" and isTable2.type == "Bool":
                    #rint("Bool to Int, True = 1, False = 0")
                    ctx.__class__ = grammarYaplParser.IntegerContext
                    #print("         // ", ctx.__class__)
                    #return grammarYaplParser.IntegerContext
                elif isTable1.type == "Bool" and isTable2.type == "Int":
                    ctx.__class__ = grammarYaplParser.BoolContext
                    #print("         // ", ctx.__class__)
                    #rint("Int to Bool, 0 = False, (>0) = True")
                    #return grammarYaplParser.BoolContext
                else:
                    print("ERROR: Cannot assign different types of values")
                    #return "ERROR"
                    #exit(1)

        else:
            # asignación de un valor explicito a una variable

            # int to int ERROR
            print("-------------------------------------------------------------------------------------------------------------------------------")
            print(asignado)
            print(type(asignado))
            print(isTable1)
            print(isTable1.type)
            
            if isTable1.type == "Int" and type(asignado) == grammarYaplParser.IntegerContext:
                #rint("int to int")
                #return grammarYaplParser.IntegerContext
                ctx.__class__ = grammarYaplParser.IntegerContext
                #print("         // ", ctx.__class__)

            # bool to bool
            elif isTable1.type == "Bool" and (asignado.getText() == "true" or asignado.getText() == "false"):
                #rint("bool to bool")
                #return grammarYaplParser.BoolContext
                ctx.__class__ = grammarYaplParser.BoolContext
                #print("         // ", ctx.__class__)
            # string to string
            elif isTable1.type == "String" and type(asignado) == grammarYaplParser.StringContext:
                #rint("string to string")
                #return grammarYaplParser.StringContext
                ctx.__class__ = grammarYaplParser.StringContext
                #print("         // ", ctx.__class__)
            # int to bool
            elif isTable1.type == "Bool" and type(asignado) == grammarYaplParser.IntegerContext:
                #rint("int to bool")
                #return grammarYaplParser.BoolContext
                ctx.__class__ = grammarYaplParser.BoolContext
                #print("         // ", ctx.__class__)
            # bool to int
            elif isTable1.type == "Int" and (asignado.getText() == "true" or asignado.getText() == "false"):
                #rint("bool to int")
                #return grammarYaplParser.IntegerContext
                ctx.__class__ = grammarYaplParser.IntegerContext
                #print("         // ", ctx.__class__)
            else:
                print("ERROR: Cannot assign different types of values")
                #return "ERROR"
                #exit(1)
        #print("         - ", ctx.__class__)
        #print('-' * 50)
