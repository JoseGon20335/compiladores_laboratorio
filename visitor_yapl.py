#visitor_yapl.py
from antlr4 import *
from symbol_table import symbol_table, symbol
from antlr_build.grammarYaplVisitor import grammarYaplVisitor
from antlr_build.grammarYaplParser import grammarYaplParser
from prettytable import PrettyTable
import re

class visitor_yapl(grammarYaplVisitor):

    def __init__(self):
        self.symbol_table = symbol_table()
        self.scope = "global"
        self.defaultMethods = {
            "IO": {"out_string": [["String"], "IO"], "out_int": [["Int"], "IO"], "in_string": [[], "String"], "in_int": [[], "Int"]},
            "Object": {"abort": [[], "Object"], "type_name": [[], "String"], "copy": [[], "SELF_TYPE"]},
            "String": {"length": [[], "Int"], "concat": [["String"], "String"], "substr": [["Int", "Int"], "String"]}
        }

    def define_symbol_table(self, symbol_table):
        self.symbol_table = symbol_table

    def diagnosis(self, ctx:grammarYaplParser.ProgramContext):
        print(type(ctx))
        print(dir(ctx))

    def visitProgram(self, ctx:grammarYaplParser.ProgramContext):
        # define default 
        print("_____Program_____")
        for value in self.defaultMethods:
            for method in self.defaultMethods[value]:
                newSymbol = symbol(method, self.defaultMethods[value][method][1], ctx.start.line, value)
                newSymbol.defineAsFunction = True
                newSymbol.paramsName = [self.defaultMethods[value][method][1]]
                self.symbol_table.add(method, newSymbol, None, self.defaultMethods[value][method][0], None, None)
                
                print("CLASS " + method)

        reservados = ["Int", "Bool", "String", "IO", "Object"]
        for value in reservados:
            newSymbol = symbol(value, "class", ctx.start.line, "global")
            self.symbol_table.add(value, newSymbol, None, None, None, None)
            print("CLASS " + value)

        for i in ctx.children:
            if hasattr(i, "CLASS"):
                currentSymbol = i.TYPE_ID(0).getText()
                type = i.CLASS().getText()
                line = i.start.line

                newSymbol = symbol(currentSymbol, type, line, self.scope)
                self.symbol_table.add(currentSymbol, newSymbol, None, None, -1, None)
                print("Program child: " + currentSymbol)
                tempScope = currentSymbol

                for j in i.children:
                    if isinstance(j, grammarYaplParser.MethodContext):
                        currentSymbol = j.OBJECT_ID().symbol.text
                        type = j.TYPE_ID().getText()
                        line = j.start.line

                        inputTypes = []
                        inputNames = []
                        for k in j.formal():
                            inputTypes.append(k.TYPE_ID().symbol.text)
                            inputNames.append(k.OBJECT_ID().symbol.text)

                        newSymbol = symbol(currentSymbol, type, line, tempScope)
                        newSymbol.defineAsFunction = True
                        newSymbol.paramsName = inputNames
                        self.symbol_table.add(currentSymbol, newSymbol, None, inputTypes, -1, None)
                        print("Program class child: " + currentSymbol)

        for i in ctx.children:
            if hasattr(i, 'CLASS') and i.INHERITS():
                type = i.TYPE_ID(1).getText()
                up = self.symbol_table.getSymbol(type, "global")

                if up != None:
                    upInScopre = self.symbol_table.getAllInScope(type) 

                    for j in upInScopre:
                        newSymbol = symbol(j.id, j.type, j.line, i.TYPE_ID(0).getText())
                        newSymbol.defineAsFunction = j.defineAsFunction
                        params = self.symbol_table.getParams(j.id)
                        paramsNameT = self.symbol_table.getParamsNames(j.id)
                        newSymbol.paramsName = paramsNameT
                        self.symbol_table.add(j.id, newSymbol, None, params, -1, None)
                        print("Program inherits: " + j.id)

        # Add program to symbol table
        self.visitChildren(ctx)

    def print_symbol_table(self):
        myTab = PrettyTable(["ID", "Type", "Line", "Scope", "Inherit", "Params", "Byte", "Offset"])
        myTab.max_width['ID'] = 30

        for key, value in self.symbol_table.records.items():
            print(key, value.id, value.type, value.line, value.scope, value.inherit, value.params, value.byte, value.offset)

        for key, value in self.symbol_table.records.items():
            if value.byte != -1:
                myTab.add_row([
                    value.id, 
                    str(value.type) if value.type is not None else "Unknown",
                    str(value.line) if value.line is not None else "Unknown",
                    str(value.scope) if value.scope is not None else "Unknown",
                    str(value.inherit) if value.inherit is not None else "Unknown",
                    str(value.params) if value.params is not None else "Unknown",
                    str(value.byte) if value.byte is not None else "Unknown",
                    str(value.offset) if value.offset is not None else "Unknown"
                ])

        print(myTab.get_string(title="Symbol Table"))
    
    def get_symbol_table(self):
        new_symbol_table = symbol_table()

        for key, value in self.symbol_table.records.items():
            if value.byte != -1:
                newSymbol = symbol(value.id, value.type, value.line, value.scope)
                newSymbol.inherit = value.inherit
                newSymbol.params = value.params
                newSymbol.byte = value.byte
                newSymbol.offset = value.offset
                newSymbol.defineAsFunction = value.defineAsFunction
                newSymbol.paramsName = value.paramsName

                new_symbol_table.add(value.id, newSymbol, value.inherit, value.params, value.byte, value.offset)

        # Return the new symbol table instead of temp
        return new_symbol_table

    def addOffset(self):
        scopes = []
        for key in self.symbol_table.records:
            if self.symbol_table.records[key].scope not in scopes and "." not in self.symbol_table.records[key].scope:
                scopes.append(self.symbol_table.records[key].scope)

        for temp in scopes:
            offsetTemp = 0
            allScopes = self.symbol_table.getAllInScope(temp)

            for temp2 in allScopes:
                if temp2.defineAsFunction:
                    temp2.offset = 0
                else:
                    temp2.offset = offsetTemp
                    offsetTemp += temp2.byte

    def fixable(self):
        for key in self.symbol_table.records:
            if self.symbol_table.records[key].scope == "global":
                print("byte: ", self.symbol_table.records[key].id)
                self.symbol_table.records[key].byte = 0
                self.defineFixable(self.symbol_table.records[key])

    def defineFixable(self, nameType):
        scopes = self.symbol_table.getAllInScope(nameType.id)
        # newScopesVal = self.leftOvers(scopes)
        # scopes += newScopesVal
        sizeOrNone = self.getSizeOrNone(nameType.id)
        if nameType.type == "class" and sizeOrNone != None:
            nameType.byte = sizeOrNone
            if len(scopes) > 0:
                for temp in scopes:
                    if temp.defineAsFunction:
                        self.defineFixable(temp)
                    else:
                        temp.byte = self.defineSize(temp.type)
                        nameType.byte += temp.byte
        else:
            if len(scopes) == 0:
                if nameType.type != "class":
                    nameType.byte = self.defineSize(nameType.type)
                else:
                    nameType.byte = 0
            else:
                for temp in scopes:
                    if temp.defineAsFunction:
                        self.defineFixable(temp)
                    else:
                        temp.byte = self.defineSize(temp.type)
                        nameType.byte += temp.byte

    def defineSize(self, temp):
        sizeOrNone = self.getSizeOrNone(temp)
        if sizeOrNone != None:
            return sizeOrNone
        elif "global." + temp in self.symbol_table.records:
            if self.symbol_table.records["global." + temp].byte != -1:
                return self.symbol_table.records["global." + temp].byte
            else:
                self.symbol_table.records["global." + temp].byte = 0
                self.defineFixable(self.symbol_table.records["global." + temp])
                return self.symbol_table.records["global." + temp].byte
        else:
            return 8
    
    def getSizeOrNone(self, nameType):
        if nameType == "Int":
            return 4
        elif nameType == "String":
            return 128
        elif nameType == "Bool":
            return 1
        elif nameType == "SELF_TYPE":
            return 8
        elif nameType == "Object":
            return 8
        elif nameType == "IO":
            return 14
        else:
            return None

    # def getByte(self, type):
    #     if type == "Int":
    #         return 8
    #     elif type == "String":
    #         return 1
    #     elif type == "Bool":
    #         return 1
    #     elif type == "SELF_TYPE" or type == "class":
    #         return 8
    #     else:
    #         return 8

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
                inheritsFrom = [parentClass.id]

                tempParent = parentClass
                while tempParent.inherit != []:
                    inheritsFrom.append(tempParent.inherit[0])
                    tempParent = self.symbol_table.getSymbol(tempParent.inherit[0], self.scope)

                parentMethods = self.symbol_table.getAllInScope(parent_name)
                for method in parentMethods:
                    print("Class " + self.scope + " inherits method " + method.id)
                    newSymbol = symbol(method.id, method.type, method.line, self.scope)
                    newSymbol.defineAsFunction = method.defineAsFunction
                    newSymbol.paramsName = method.paramsName
                    self.symbol_table.add(method.id, newSymbol, None, method.params, method.byte, None)
                    print("Class " + method.id)

        newSymbol = symbol(ctx.TYPE_ID(0).getText(), ctx.CLASS().getText(), ctx.start.line, "global")
        self.symbol_table.add(ctx.TYPE_ID(0).getText(), newSymbol, inheritsFrom, None, None, None)
        print("Class " + ctx.TYPE_ID(0).getText())

        # Visit children after validating class
        self.visitChildren(ctx)
    
    def visitMethod(self, ctx:grammarYaplParser.FeatureContext):
        print("_____Method_____")
        currentSymbol = str(ctx.OBJECT_ID().getText())
        data_type = str(ctx.TYPE_ID().getText())
        line = ctx.start.line
        params = []
        types = []
        tempScope = self.scope + "." + currentSymbol
        oldScope = self.scope

        if ctx.formal():
            for formal_ctx in ctx.formal():
                params.append(str(formal_ctx.OBJECT_ID().getText()))
                types.append(str(formal_ctx.TYPE_ID().getText()))

        newSymbol = symbol(currentSymbol, data_type, line, self.scope)
        newSymbol.defineAsFunction = True
        newSymbol.paramsName = params
        self.symbol_table.add(currentSymbol, newSymbol, None, types, -1, None)
        print("Method: " + currentSymbol)
        self.scope = tempScope
        print("Method: " + currentSymbol)

        # Visit children after validating attribute/method
        self.visitChildren(ctx)

        # Return to old scope after visiting children of attribute/method
        self.scope = oldScope

    def visitAttribute(self, ctx:grammarYaplParser.AttributeContext):
        print("_____Attribute_____")
        currentSymbol = ctx.OBJECT_ID().symbol.text
        type = ctx.TYPE_ID().getText()
        line = ctx.TYPE_ID().symbol.line

        newSymbol = symbol(currentSymbol, type, line, self.scope)
        self.symbol_table.add(currentSymbol, newSymbol, None, None, -1, None)
        print("Attribute: " + currentSymbol)

        # Visit children after validating attribute
        self.visitChildren(ctx)

    def visitFormal(self, ctx:grammarYaplParser.FormalContext):
        print("_____Formal_____")
        name = ctx.OBJECT_ID().getText()
        data_type = ctx.TYPE_ID().getText()
        newSymbol = symbol(name, data_type, ctx.start.line, self.scope)
        self.symbol_table.add(name, newSymbol, None, None, -1, None)
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
                self.symbol_table.add(symbolGet, newSymbol, None, None, -1, None)
                print("Add ", symbolGet)
            else:
                print("Substract: Same type")
                print(symbolGet)
                print(ctx.start.line)
                newSymbol = symbol(symbolGet, "Int", ctx.start.line, self.scope)
                self.symbol_table.add(symbolGet, newSymbol, None, None, -1, None)
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
                self.symbol_table.add(inheritedSymbol.id, newSymbol, None, None, -1, None)

            print("New: Symbol found " + symbolType)
            newSymbol = symbol(symbolGet, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, -1, None)
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
            print("Dispatch: Symbol found " + symbolGet)

            symbolType = self.symbol_table.getSymbol(symbolGet, searchScope).type
            callingMethod = self.symbol_table.getSymbol(symbolGet, searchScope)

            if callingMethod == None:
                print("Dispatch: Symbol not found " + symbolGet)
                self.symbol_table.addError("Dispatch: Symbol not found " + symbolGet + " in line " + str(ctx.start.line))
            else:
                same = True
                if len(inputTypes) != len(callingMethod.params):
                    self.symbol_table.addError("Dispatch: Invalid number of parameters for " + symbolGet)
                    same = False
                else:
                    for i in range(len(callingMethod.params)):
                        if callingMethod.params[i] not in inputTypes and inputTypes[i] != "self":
                            same = False
                            self.symbol_table.addError("Dispatch: Invalid parameter type for " + symbolGet)

                if same:
                    print("Dispatch: Symbol found " + symbolGet + " with valid input types")
                    newSymbol = symbol(completeExpr, symbolType, ctx.start.line, self.scope)
                    self.symbol_table.add(completeExpr, newSymbol, None, None, -1, None)
                    print("Dispatch ", completeExpr)
                else:
                    print("Dispatch: Symbol not found " + symbolGet)
        else:
            print("Dispatch: Symbol not found " + symbolGet)

    
    def visitString(self, ctx:grammarYaplParser.StringContext):
        print("_____String_____")
        name = ctx.STRING().getText()
        type = "String"
        print("String ", name)
        newSymbol = symbol(name, type, ctx.start.line, self.scope)
        self.symbol_table.add(ctx.STRING().getText(), newSymbol, None, None, -1, None)
        print("String ", name)
        self.visitChildren(ctx)
    
    def visitBool(self, ctx:grammarYaplParser.BoolContext):
        print("_____Bool_____")
        name = ctx.BOOL().getText()
        type = "Bool"
        print("Bool ", name)
        newSymbol = symbol(name, type, ctx.start.line, self.scope)
        self.symbol_table.add(ctx.TYPE_ID(0), newSymbol, None, None, -1, None)
        print("Bool ", name)
        self.visitChildren(ctx)
        
    def visitMulDiv(self, ctx:grammarYaplParser.MulDivContext):
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
            self.symbol_table.add(symbolGet, newSymbol, None, None, -1, None)
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
            symbolType = self.symbol_table.getSymbol(expr, self.scope).type
            newSymbol = symbol(symbolGet, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, -1, None)
            print("Isvoid ", symbolGet)
        else:
            print("Isvoid: Symbol not found " + expr)

    def visitInteger(self, ctx:grammarYaplParser.IntegerContext):
        print("_____Integer_____")
        name = ctx.getText()
        newSymbol = symbol(ctx.getText(), "Int", ctx.start.line, self.scope)
        self.symbol_table.add(name, newSymbol, None, None, -1, None)
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
            if len(inputTypes) != len(callingMethod.params):
                same = False
                self.symbol_table.addError("Static Dispatch: Invalid number of parameters for " + symbolGet)
            else:
                for i in range(len(callingMethod.params)):
                    if callingMethod.params[i] not in inputTypes:
                        same = False
                        self.symbol_table.addError("Static Dispatch: Invalid parameter type for " + symbolGet)

            if same:
                print("Static Dispatch: Symbol found " + symbolGet + " with valid input types")
                symbolType = callingMethod.type
                newSymbol = symbol(symbolGet, symbolType, ctx.start.line, self.scope)
                self.symbol_table.add(symbolGet, newSymbol, None, None, -1, None)
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

            symbolType = self.symbol_table.getSymbol(expr, self.scope).type
            newSymbol = symbol(symbolGet, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, -1, None)
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
            self.symbol_table.add(symbolGet, newSymbol, None, None, -1, None)
            print("Compare ", symbolGet)
        else:
            self.symbol_table.addError("Compare operation with different or invalid types")
    
    def visitParenthesis(self, ctx:grammarYaplParser.ParenthesisContext):
        print("_____Parenthesis_____")
        self.visitChildren(ctx)
        name = ctx.getText()
        type = self.symbol_table.getSymbol(ctx.expr().getText(), self.scope)

        if type != None:
            isFuncType = type.defineAsFunction
            theParamsName = type.paramsName
            theParams = type.params
            type = type.type
            print("Parenthesis: Symbol found " + ctx.expr().getText())
            newSymbol = symbol(name, type, ctx.start.line, self.scope)
            newSymbol.defineAsFunction = isFuncType
            newSymbol.paramsName = theParamsName
            self.symbol_table.add(name, newSymbol, None, theParams, -1, None)
            print("Parenthesis ", name)
        else:
            print("Parenthesis: Symbol not found " + name)

    
    def visitObject_id(self, ctx:grammarYaplParser.Object_idContext):
        print("_____Object_id_____")
        print("Object_id ", ctx.OBJECT_ID().getText())
        if(ctx.OBJECT_ID().getText() == 'true' or ctx.OBJECT_ID().getText() == 'false'):
            type = "Bool"
            name = ctx.OBJECT_ID().getText()
            print("Bool ", name)
            newSymbol = symbol(name, type, ctx.start.line, self.scope)
            self.symbol_table.add(name, newSymbol, None, None, -1, None)

    
    def visitNeg(self, ctx:grammarYaplParser.NegContext):
        print("_____Neg_____")
        # Visit children before validating
        self.visitChildren(ctx)

        symbolGet = ctx.getText()
        expr = ctx.expr().getText()
        type = self.symbol_table.getType(expr, self.scope)

        # for key, value in self.symbol_table.records.items():
        #     if type == key.split(".")[1]:
        #         print("Neg: Symbol is of type " + type)
        #         expr = type

        if type in self.symbol_table.records:
            print("Neg: Symbol is of type " + type)
            expr = type

        if self.symbol_table.getSymbol(expr, self.scope) != None:
            print("Neg: Symbol found " + expr)
            symbolType = self.symbol_table.getSymbol(expr, self.scope).type
            newSymbol = symbol(symbolGet, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbolGet, newSymbol, None, None, -1, None)
            print("Neg ", symbolGet)
        else:
            print("Neg: Symbol not found " + expr)

    def visitNot(self, ctx:grammarYaplParser.NotContext):
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
            symbolType = found_symbol.type
            newSymbol = symbol(symbol_text, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbol_text, newSymbol, None, None, -1, None)
            print("Not ", symbol_text)
        else:
            print("Not: Symbol not found " + expr)

    def visitSelf(self, ctx:grammarYaplParser.SelfContext):
        print("_____Self_____")
        name = ctx.getText()
        type = "SELF_TYPE"
        print("Self ", name)
        newSymbol = symbol(name, type, ctx.start.line, self.scope)
        self.symbol_table.add(name, newSymbol, None, None, -1, None)
        print("Self ", name)
        self.visitChildren(ctx)
    
    def visitBlock(self, ctx:grammarYaplParser.BlockContext):
        print("_____Block_____")
        self.visitChildren(ctx)
        print("Block ", ctx.getText())
    
    def visitLet(self, ctx:grammarYaplParser.LetContext):
        print("_____Let_____")
        name = ctx.getText()
        newSymbol = symbol(name, "LET", ctx.start.line, self.scope)
        print("Let ", ctx.getText())
        self.symbol_table.add(name, newSymbol, None, None, -1, None)
        
        scopeLegacy = self.scope
        tempScope = self.scope + "." + "LET"
        self.scope = tempScope
        
        for i in range(len(ctx.OBJECT_ID())):
            name = ctx.OBJECT_ID(i).getText()
            data_type = ctx.TYPE_ID(i).getText()
            newSymbol = symbol(name, data_type, ctx.start.line, self.scope)
            self.symbol_table.add(name, newSymbol, None, None, -1, None)
            print("Let ", name, "type", data_type)
        self.visitChildren(ctx)

        self.scope = scopeLegacy
    
    def visitIf(self, ctx:grammarYaplParser.IfContext):
        print("_____If_____")
        # Visit children before validating
        self.visitChildren(ctx)

        # Get symbol and expression
        symbol_text = ctx.getText()
        expr = ctx.expr(0).getText()

        # Obtain type from symbol table
        type = self.symbol_table.getType(expr, self.scope)

        # Check if expr is a type
        # for key, value in self.symbol_table.records.items():
        #     if type == key.split(".")[1]:
        #         print("If: Symbol is of type " + type)
        #         expr = type

        if type in self.symbol_table.records:
            print("If: Symbol is of type " + type)
            expr = type

        # Check if the symbol exists in the symbol table
        found_symbol = self.symbol_table.getSymbol(expr, self.scope)

        if found_symbol:
            print("If: Symbol found " + expr)
            symbolType = found_symbol.type
            newSymbol = symbol(symbol_text, symbolType, ctx.start.line, self.scope)
            self.symbol_table.add(symbol_text, newSymbol, None, None, -1, None)
            print("If ", symbol_text)
        else:
            print("If: Symbol not found " + expr)

    def visitAssign(self, ctx:grammarYaplParser.AssignContext):
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
