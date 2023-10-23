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
        # define default 
        print("_____Program_____")
        for value in self.defaultMethods:
            for method in self.defaultMethods[value]:
                newSymbol = symbol(method, self.defaultMethods[value][method][1], ctx.start.line, value)
                self.symbol_table.add(method, newSymbol, None, self.defaultMethods[value][method][0], None, None)
                print("Class " + method)

        reservados = ["Int", "String", "Bool", "IO", "Object"]
        for value in reservados:
            newSymbol = symbol(value, "class", ctx.start.line, "GLOBAL")
            self.symbol_table.add(value, newSymbol, None, None, None, None)
            print("Class " + value)
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
        print("_____Class_____")
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
                    newSymbol = symbol(method.varName, method.dataType, method.line, self.scope)
                    self.symbol_table.add(method.varName, newSymbol, None, method.paramTypes, method.byte)
                    print("Class " + method.varName)

        newSymbol = symbol(self.scope, ctx.CLASS().getText(), ctx.start.line, self.scope)
        self.symbol_table.add(self.scope, newSymbol, inheritsFrom, None, None, None)
        print("Class " + self.scope)

        # Visit children after validating class
        self.visitChildren(ctx)
    
    def visitMethod(self, ctx: grammarYaplParser.FeatureContext):
        print("_____Method_____")
        # If both OBJECT_ID and TYPE_ID are present, it's an attribute or a method. 
        # if ctx.OBJECT_ID() and ctx.TYPE_ID():
        # Assign common values 
        currentSymbol = str(ctx.OBJECT_ID().getText())
        data_type = str(ctx.TYPE_ID().getText())
        line = ctx.start.line
        params = []
        types = []
        # methodScope = self.scope + "." + currentSymbol
        oldScope = self.scope

        # Check if it's a method by the presence of formal() 
        if ctx.formal():
            for formal_ctx in ctx.formal():
                params.append(str(formal_ctx.OBJECT_ID().getText()))
                types.append(str(formal_ctx.TYPE_ID().getText()))

        # Add the method to the symbol table
        newSymbol = symbol(currentSymbol, data_type, line, self.scope)
        # Adding number of parameters and their types as well
        self.symbol_table.add(currentSymbol, newSymbol, None, params, self.getByte(data_type), types)
        print("Method: " + currentSymbol)
        self.scope = currentSymbol
        print("Method: " + currentSymbol)
        # else:
        #     # It's an attribute, so add it to the symbol table
        #     newSymbol = symbol(currentSymbol, data_type, line, self.scope)
        #     byte = self.getByte(data_type)
        #     self.symbol_table.add(currentSymbol, newSymbol, None, None, byte, None)

        # Visit children after validating attribute/method
        self.visitChildren(ctx)

        # Return to old scope after visiting children of attribute/method
        self.scope = oldScope

    def visitAttribute(self, ctx:grammarYaplParser.AttributeContext):
        print("_____Attribute_____")
        currentSymbol = ctx.OBJECT_ID().symbol.text
        type = ctx.TYPE_ID(0).getText()
        line = ctx.start.line

        newSymbol = symbol(currentSymbol, type, line, self.scope)
        self.symbol_table.add(currentSymbol, newSymbol, None, None, self.getByte(type), None)
        print("Attribute: " + currentSymbol)

        # Visit children after validating attribute
        self.visitChildren(ctx)

    def visitFormal(self, ctx:grammarYaplParser.FormalContext):
        print("_____Formal_____")
        name = ctx.OBJECT_ID().getText()
        data_type = ctx.TYPE_ID().getText()
        newSymbol = symbol(name, data_type, ctx.start.line, self.scope)
        self.symbol_table.add(name, newSymbol, None, None, self.getByte(data_type), None)
        print("Formal: " + name)
        self.visitChildren(ctx)
    
    def visitAddSub(self, ctx:grammarYaplParser.AddSubContext):
        print("_____AddSub_____")
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
                types.append(self.symbol_table.getType(expr.getText(), self.scope))

        same = True
        for i in range(1, len(types)):
            if types[i] not in expected:
                same = False

        symbolGet = ctx.getText()

        if same:
            if hasattr(ctx, "ADD"):  # Adjust this check based on your actual implementation
                print("Add: Same type")
                newSymbol = symbol(symbolGet, "Int", ctx.start.line, self.scope)
                self.symbol_table.add(symbolGet, newSymbol, None, None, self.getByte("Int"), None)
                print("Add ", symbolGet)
            else:
                print("Substract: Same type")
                print(symbolGet)
                print(ctx.start.line)
                newSymbol = symbol(symbolGet, "Int", ctx.start.line, self.scope)
                self.symbol_table.add(symbolGet, newSymbol, None, None, self.getByte("Int"), None)
                print("Substract ", symbolGet)
        else:
            if hasattr(ctx, "ADD"):  # Adjust this check based on your actual implementation
                # Logic for validateTypes integrated
                expected_type = "String"
                expr_type = self.symbol_table.getType(expressions[0].getText(), self.scope)
                sameString = expr_type == expected_type

                if sameString:
                    print("Add: Same type")
                else:
                    self.symbol_table.addError("Add operation with different or invalid types")
            else:
                self.symbol_table.addError("Substract operation with different or invalid types")
        
    def visitMinus(self, ctx:grammarYaplParser.MinusContext):
        print("_____Minus_____")
        self.visitChildren(ctx)
    
    def visitNew(self, ctx:grammarYaplParser.NewContext):
        print("_____New_____")
        symbolGet = ctx.getText()
        symbolType = ctx.TYPE_ID().symbol.text

        foundSymbol = False
        if self.symbol_table.getSymbol(symbolType, self.scope) is not None:
            foundSymbol = True

        if foundSymbol:
            inherited = self.symbol_table.getAllInScope(symbolType)

            for inheritedSymbol in inherited:
                print("New: Inherited symbol " + inheritedSymbol.id)
                newSymbol = symbol(inheritedSymbol.id, inheritedSymbol.type, ctx.start.line, self.scope)
                self.symbol_table.add(inheritedSymbol.id, newSymbol, None, None, self.getByte(inheritedSymbol.type), None)

            print("New: Symbol found " + symbolType)
            newSymbol = symbol(symbolGet, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, self.getByte(symbolType), None)
            print("New ", symbolGet)
        else:
            print("New: Symbol not found " + symbolType)
            self.symbol_table.addError("New: Symbol not found " + symbolType + " in line " + str(ctx.start.line))

        # Continues with visiting children
        self.visitChildren(ctx)
    
    def visitDispatch(self, ctx:grammarYaplParser.DispatchContext):
        print("_____Dispatch_____")
        # Visit children before validating
        self.visitChildren(ctx)

        symbolGet = ctx.OBJECT_ID().symbol.text
        expr = ctx.expr(0).getText()
        completeExpr = ctx.getText()
        type = self.symbol_table.getType(expr, self.scope)
        searchScope = self.scope

        inputTypes = []
        for i in range(1, len(ctx.expr())):
            inputTypes.append(self.symbol_table.getType(ctx.expr(i).getText(), self.scope))

        expr = ctx.expr(0).getText()
        if type == None:
            print("Dispatch: Symbol not found " + expr)
            return

        # Check if expr is a type
        if self.symbol_table.getSymbol(type, self.scope) != None:
            print("Dispatch: Symbol is of type " + type)
            searchScope = type
            
        if self.symbol_table.getSymbol(symbolGet, searchScope) != None:
            print("Dispatch: Symbol found " + symbol)

            symbolType = self.symbol_table.getSymbol(symbolGet, searchScope).dataType
            callingMethod = self.symbol_table.getSymbol(symbolGet, searchScope)

            if callingMethod == None:
                print("Dispatch: Symbol not found " + symbolGet)
                self.symbol_table.addError("Dispatch: Symbol not found " + symbolGet + " in line " + str(ctx.start.line))
            else:
                same = True
                if len(inputTypes) != len(callingMethod.paramTypes):
                    self.symbol_table.addError("Dispatch: Invalid number of parameters for " + symbol)
                    same = False
                else:
                    for i in range(len(callingMethod.paramTypes)):
                        if callingMethod.paramTypes[i] not in inputTypes and inputTypes[i] != "self":
                            same = False
                            self.symbol_table.addError("Dispatch: Invalid parameter type for " + symbol)

                if same:
                    print("Dispatch: Symbol found " + symbol + " with valid input types")
                    newSymbol = symbol(completeExpr, symbolType, ctx.start.line, self.scope)
                    self.symbol_table.add(completeExpr, newSymbol, None, None, self.getByte(symbolType), None)
                    print("Dispatch ", completeExpr)
                else:
                    print("Dispatch: Symbol not found " + symbol)
        else:
            print("Dispatch: Symbol not found " + symbol)

    
    def visitString(self, ctx:grammarYaplParser.StringContext):
        print("_____String_____")
        name = ctx.STRING().getText()
        type = "String"
        print("String ", name)
        newSymbol = symbol(name, type, ctx.start.line, self.scope)
        self.symbol_table.add(ctx.STRING().getText(), newSymbol, None, None, self.getByte("String"), None)
        print("String ", name)
        self.visitChildren(ctx)
    
    def visitBool(self, ctx:grammarYaplParser.BoolContext):
        print("_____Bool_____")
        name = ctx.BOOL().getText()
        type = "Bool"
        print("Bool ", name)
        newSymbol = symbol(name, type, ctx.start.line, self.scope)
        self.symbol_table.add(ctx.TYPE_ID(0), newSymbol, None, None, self.getByte("Bool"), None)
        print("Bool ", name)
        self.visitChildren(ctx)
        
    def visitMulDiv(self, ctx: grammarYaplParser.MulDivContext):
        print("_____MulDiv_____")
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
                types.append(self.symbol_table.getType(expr.getText(), self.scope))

        same = True
        for i in range(1, len(types)):
            if types[i] not in expected:
                same = False

        # Now, based on the result, determine the operation
        symbolGet = ctx.getText()
        if ctx.MULT():  # Replace `MUL` with the correct token or method if it's different
            operation = "Multiply"
        elif ctx.DIV():  # Replace `DIV` with the correct token or method if it's different
            operation = "Divide"
        else:
            operation = "Unknown"

        # Validate the operation
        if same == True:
            print(f"{operation}: Same type")
            newSymbol = symbol(symbolGet, "Int", ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, self.getByte("Int"), None)
            print(f"{operation} ", symbolGet)
        else:
            self.symbol_table.addError(f"{operation} operation with different or invalid types")

    def visitIsvoid(self, ctx:grammarYaplParser.IsvoidContext):
        print("_____Isvoid_____")
        self.visitChildren(ctx)

        symbolGet = ctx.getText()
        expr = ctx.expr().getText()
        type = self.symbol_table.getType(expr, self.scope)

        for key, value in self.symbol_table.records.items():
            if type == key.split(".")[1]:
                print("Isvoid: Symbol is of type " + type)
                expr = type

        # if type in self.symbol_table.symbolTable:
        #     print("Isvoid: Symbol is of type " + type)
        #     expr = type

        if self.symbol_table.getSymbol(expr, self.scope) != None:
            print("Isvoid: Symbol found " + expr)
            symbolType = self.symbol_table.getSymbol(expr, self.scope).dataType
            newSymbol = symbol(symbolGet, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, self.getByte("Bool"), None)
            print("Isvoid ", symbolGet)
        else:
            print("Isvoid: Symbol not found " + expr)

    def visitInteger(self, ctx:grammarYaplParser.IntegerContext):
        print("_____Integer_____")
        name = ctx.INTEGER().getText()
        newSymbol = symbol(ctx.INTEGER().getText(), "Int", ctx.start.line, self.scope)
        self.symbol_table.add(name, newSymbol, None, None, self.getByte("Int"), None)
        print("Integer ", name)
        self.visitChildren(ctx)
    
    def visitStatic_dispatch(self, ctx:grammarYaplParser.Static_dispatchContext):
        print("_____Static_dispatch_____")
        # Visit children first
        self.visitChildren(ctx)

        symbolGet = ctx.getText()

        inputTypes = []
        # Assuming the syntax in your grammar for `expr` is consistent with `yaplParser`, 
        # if not, modify this part accordingly
        for expr in ctx.expr():
            inputTypes.append(self.symbol_table.getType(expr.getText(), self.scope))

        # Assuming the syntax in your grammar for `OBJECT_ID` is consistent with `yaplParser`, 
        # if not, modify this part accordingly
        callingMethod = self.symbol_table.getSymbol(ctx.OBJECT_ID().symbol.text, self.scope)

        if callingMethod == None:
            print("Static Dispatch: Symbol not found " + symbolGet)
            self.symbol_table.addError("Static Dispatch: Symbol not found " + symbolGet + " in line " + str(ctx.start.line))
        else:
            same = True
            if len(inputTypes) != len(callingMethod.paramTypes):
                same = False
                self.symbol_table.addError("Static Dispatch: Invalid number of parameters for " + symbolGet)
            else:
                for i in range(len(callingMethod.paramTypes)):
                    if callingMethod.paramTypes[i] not in inputTypes:
                        same = False
                        self.symbol_table.addError("Static Dispatch: Invalid parameter type for " + symbolGet)

            if same:
                print("Static Dispatch: Symbol found " + symbolGet + " with valid input types")
                symbolType = callingMethod.dataType
                newSymbol = symbol(symbolGet, symbolType, ctx.start.line, self.scope)
                self.symbol_table.add(symbolGet, newSymbol, None, None, self.getByte(symbolType), None)
                print("Static Dispatch ", symbolGet)
            else:
                print("Static Dispatch: Symbol not found " + symbolGet)

    def visitWhile(self, ctx:grammarYaplParser.WhileContext):
        print("_____While_____")
        # Visit children first
        self.visitChildren(ctx)

        symbolGet = ctx.getText()
        
        expr = ctx.expr(0).getText()
        type = self.symbol_table.getType(expr, self.scope)

        # Check if expr is a type
        for key, value in self.symbol_table.records.items():
            if type == key.split(".")[1]:
                print("While: Symbol is of type " + type)
                expr = type

        # if type in self.symbol_table.symbolTable:
        #     print("While: Symbol is of type " + type)
        #     expr = type

        if self.symbol_table.getSymbol(expr, self.scope) != None:
            print("While: Symbol found " + expr)

            symbolType = self.symbol_table.getSymbol(expr, self.scope).dataType
            newSymbol = symbol(symbolGet, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, self.getByte(symbolType), None)
            print("While ", symbolGet)
        else:
            print("While: Symbol not found " + expr)

    def visitComparison(self, ctx:grammarYaplParser.ComparisonContext):
        print("_____Comparison_____")
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
                types.append(self.symbol_table.getType(expr.getText(), self.scope))

        same = True
        for i in range(1, len(types)):
            if types[i] not in expected:
                same = False

        symbolGet = ctx.getText()

        if same:
            print("Compare: Same type")
            newSymbol = symbol(symbolGet, "Bool", ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, self.getByte("Bool"), None)
            print("Compare ", symbolGet)
        else:
            self.symbol_table.addError("Compare operation with different or invalid types")
    
    def visitParenthesis(self, ctx:grammarYaplParser.ParenthesisContext):
        print("_____Parenthesis_____")
        self.visitChildren(ctx)
        name = ctx.expr().getText()
        type = self.symbol_table.getSymbol(name, self.scope)

        if type != None:
            type = type.type
            print("Parenthesis: Symbol found " + name)
            newSymbol = symbol(name, type, ctx.start.line, self.scope)
            self.symbol_table.add(name, newSymbol, None, None, self.getByte(type), None)
            print("Parenthesis ", name)
        else:
            print("Parenthesis: Symbol not found " + name)

    
    def visitObject_id(self, ctx:grammarYaplParser.Object_idContext):
        print("_____Object_id_____")
        print("Object_id ", ctx.OBJECT_ID().getText())
    
    def visitNeg(self, ctx:grammarYaplParser.NegContext):
        print("_____Neg_____")
        # Visit children before validating
        self.visitChildren(ctx)

        symbolGet = ctx.getText()
        expr = ctx.expr().getText()
        type = self.symbol_table.getType(expr, self.scope)

        print(type)
        print(self.symbol_table.records)

        for key, value in self.symbol_table.records.items():
            if type == key.split(".")[1]:
                print("Neg: Symbol is of type " + type)
                expr = type

        # if type in self.symbol_table.records:
        #     print("Neg: Symbol is of type " + type)
        #     expr = type

        print(expr)
        print(self.scope)

        if self.symbol_table.getSymbol(expr, self.scope) != None:
            print("Neg: Symbol found " + expr)
            symbolType = self.symbol_table.getSymbol(expr, self.scope).dataType
            newSymbol = symbol(symbolGet, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, self.getByte(symbolType), None)
            print("Neg ", symbolGet)
        else:
            print("Neg: Symbol not found " + expr)

    def visitNot(self, ctx: grammarYaplParser.NotContext):
        print("_____Not_____")
        # Visit children before validating
        self.visitChildren(ctx)

        symbol_text = ctx.getText()
        expr = ctx.expr().getText()

        # Obtain type from symbol table
        type = self.symbol_table.getType(expr, self.scope)

        # Check if expr is a type
        for key, value in self.symbol_table.records.items():
            if type == key.split(".")[1]:
                print("Not: Symbol is of type " + type)
                expr = type

        # if type in self.symbol_table.symbolTable:
        #     print("Not: Symbol is of type " + type)
        #     expr = type

        # Check if the symbol exists in the symbol table
        found_symbol = self.symbol_table.getSymbol(expr, self.scope)

        if found_symbol:
            print("Not: Symbol found " + expr)
            symbolType = found_symbol.dataType
            newSymbol = symbol(symbol_text, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbol_text, newSymbol, None, None, self.getByte(symbolType), None)
            print("Not ", symbol_text)
        else:
            print("Not: Symbol not found " + expr)

    def visitSelf(self, ctx:grammarYaplParser.SelfContext):
        print("_____Self_____")
        name = ctx.getText()
        type = "SELF_TYPE"
        print("Self ", name)
        newSymbol = symbol(name, type, ctx.start.line, self.scope)
        self.symbol_table.add(name, newSymbol, None, None, self.getByte(type), None)
        print("Self ", name)
        self.visitChildren(ctx)
    
    def visitBlock(self, ctx:grammarYaplParser.BlockContext):
        print("_____Block_____")
        self.visitChildren(ctx)
        print("Block ", ctx.getText())
    
    def visitLet(self, ctx:grammarYaplParser.LetContext):
        print("_____Let_____")
        newSymbol = symbol(ctx.LET().getText(), "LET", ctx.start.line, self.scope)
        print("Let ", ctx.getText())
        self.symbol_table.add(ctx.LET().getText(), newSymbol, None, None, self.getByte("Let"), None)
        for i in range(len(ctx.OBJECT_ID())):
            name = ctx.OBJECT_ID(i).getText()
            data_type = ctx.TYPE_ID(i).getText()
            newSymbol = symbol(name, data_type, ctx.start.line, self.scope)
            self.symbol_table.add(name, newSymbol, None, None, self.getByte(data_type), None)
            print("Let ", name, "type", data_type)
        self.visitChildren(ctx)
    
    def visitIf(self, ctx: grammarYaplParser.IfContext):
        print("_____If_____")
        # Visit children before validating
        self.visitChildren(ctx)

        # Get symbol and expression
        symbol_text = ctx.IF().getText()
        expr = ctx.expr(0).getText()

        # Obtain type from symbol table
        type = self.symbol_table.getType(expr, self.scope)

        # Check if expr is a type
        for key, value in self.symbol_table.records.items():
            if type == key.split(".")[1]:
                print("If: Symbol is of type " + type)
                expr = type

        # if type in self.symbol_table.symbolTable:
        #     print("If: Symbol is of type " + type)
        #     expr = type

        # Check if the symbol exists in the symbol table
        found_symbol = self.symbol_table.getSymbol(expr, self.scope)

        if found_symbol:
            print("If: Symbol found " + expr)
            symbolType = found_symbol.dataType
            newSymbol = symbol(symbol_text, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbol_text, newSymbol, None, None, self.getByte(symbolType), None)
            print("If ", symbol_text)
        else:
            print("If: Symbol not found " + expr)

    def visitAssign(self, ctx: grammarYaplParser.AssignContext):
        print("_____Assign_____")
        # Visit children before validating
        self.visitChildren(ctx)

        currentSymbol = str(ctx.OBJECT_ID())
        symbolType = self.symbol_table.getType(currentSymbol, self.scope)
        type = self.symbol_table.getType(ctx.expr().getText(), self.scope)
        print(ctx.expr().getText())
        # Check if the current symbol is in the symbol table
        if symbolType == None:
            # Add error to the symbol table
            self.symbol_table.addError("Assign: Symbol not found " + currentSymbol)
            return

        # Implicit casting validation
        if (symbolType == "Bool" and type == "Int") or (symbolType == "Int" and type == "Bool"):
            print("Assign: Implicit casting")
        elif symbolType != type and type != "SELF_TYPE":
            symbolTypeInstance = self.symbol_table.getSymbol(symbolType, self.scope)
            print(type)
            print(self.scope)
            typeInstance = self.symbol_table.getSymbol(type, self.scope)

            # Check if there's any inheritance relationship that can be used for casting
            if type != None:
                if (type in symbolTypeInstance.inherit) or (symbolType in typeInstance.inherit):
                    print("Assign: Implicit casting with inheritance")
                else:
                    # Add error to the symbol table
                    error_msg = f"Invalid type for {currentSymbol}: {symbolType} trying to assign {type}"
                    self.symbol_table.addError(error_msg)

    def visitAnd(self, ctx:grammarYaplParser.AndContext):
        print("_____And_____")
        # Visit children before validating
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
                types.append(self.symbol_table.getType(expr.getText(), self.scope))

        same = all(t in expected for t in types)
        
        symbolGet = ctx.getText()

        if same:
            print("And: Same type")
            newSymbol = symbol(symbolGet, "Bool", ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, None, None)
            print("And ", symbolGet)
        else:
            self.symbol_table.addError("And operation with different or invalid types")
        
    def visitOr(self, ctx:grammarYaplParser.OrContext):
        print("_____Or_____")
        # Visit children before validating
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
                types.append(self.symbol_table.getType(expr.getText(), self.scope))
        
        same = all(t in expected for t in types)
        
        symbolGet = ctx.getText()

        if same:
            print("Or: Same type")
            newSymbol = symbol(symbolGet, "Bool", ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, None, None)
            print("Or ", symbolGet)
        else:
            self.symbol_table.addError("Or operation with different or invalid types")
