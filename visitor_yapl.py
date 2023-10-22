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
        self.scope = ctx.TYPE_ID(0).getText()
        #print("Scope: " + self.scope)
        if ctx.INHERITS() and ctx.TYPE_ID(1):
            # This class inherits from another class
            parent_name = ctx.TYPE_ID(1).getText()
            newSymbol = symbol(ctx.TYPE_ID(0).getText(), ctx.CLASS().getText(), ctx.start.line, self.scope)
            #self.symbol_table.addScope(self.scope)
            self.symbol_table.add(ctx.TYPE_ID(0).getText(), newSymbol, parent_name, None, None, None)
        else:
            # This class does not inherit from another class
            newSymbol = symbol(ctx.TYPE_ID(0).getText(), ctx.CLASS().getText(), ctx.start.line, self.scope)
            #self.symbol_table.addScope(self.scope)
            self.symbol_table.add(ctx.TYPE_ID(0).getText(), newSymbol, None, None, None, None)
        self.visitChildren(ctx)
    
    def visitFeature(self, ctx:grammarYaplParser.FeatureContext):
        ### AQUÍ DEFINIMOS UN CONTEXTO
        if ctx.OBJECT_ID() and ctx.TYPE_ID():
            # This is an attribute definition
            name = ctx.OBJECT_ID().getText()
            data_type = ctx.TYPE_ID(0).getText()
            temporalScope = name
            #print("name: " + name + " data_type: " + data_type)
            parameters = []
            newSymbol = symbol(name, data_type, ctx.start.line, self.scope)
            byte = self.getByte(data_type)
            if ctx.formal():
                for formal_ctx in ctx.formal():
                    param_name = formal_ctx.OBJECT_ID().getText()
                    param_type = formal_ctx.TYPE_ID().getText()
                    parameters.append(param_type)
                    internalParam = symbol(param_name, param_type, ctx.start.line, temporalScope)
                    byteInternal = self.getByte(param_type)
                    #self.symbol_table.addChildScope(self.scope, temporalScope)
                    #self.scope = temporalScope
                    self.symbol_table.add(param_name, internalParam, None, None, byteInternal, None)
            self.symbol_table.add(name, newSymbol, None, parameters, byte, None)
            #self.scope = temporalScope
        else:
            # This is a method definition
            name = ctx.TYPE_ID(0).getText()
            #print("AQUI ESTAMOS EN METHOD")
            #print("name: " + name)
            #print("scope: " + self.scope)
            newSymbol = symbol(name, "FEATURE", ctx.start.line, self.scope)
            parameters = []
            # Handle the method's parameters
            if ctx.formal():
                for formal_ctx in ctx.formal():
                    param_name = formal_ctx.OBJECT_ID().getText()
                    param_type = formal_ctx.TYPE_ID().getText()
                    parameters.append(param_type)
            self.symbol_table.add(name, newSymbol, None, parameters, 8, None)
            self.scope = name
        self.visitChildren(ctx)


    def visitFormal(self, ctx:grammarYaplParser.FormalContext):
        name = ctx.OBJECT_ID().getText()
        data_type = ctx.TYPE_ID().getText()
        newSymbol = symbol(name, data_type, ctx.start.line, self.scope)
        self.symbol_table.add(name, newSymbol, None, None, self.getByte(data_type), None)
        self.visitChildren(ctx)
    
    def visitAddSub(self, ctx:grammarYaplParser.AddSubContext):
        self.visitChildren(ctx)
    
    def visitMinus(self, ctx:grammarYaplParser.MinusContext):
        self.visitChildren(ctx)
    
    def visitNew(self, ctx:grammarYaplParser.NewContext):
        newSymbol = symbol("NEW", "NEW", ctx.start.line, self.scope)
        # self.symbol_table.add("NEW", newSymbol, None)
        self.visitChildren(ctx)
    
    def visitDispatch(self, ctx:grammarYaplParser.DispatchContext):
        self.visitChildren(ctx)
    
    def visitString(self, ctx:grammarYaplParser.StringContext):
        newSymbol = symbol(ctx.STRING().getText(), "STRING", ctx.start.line, self.scope)
        # self.symbol_table.add(ctx.STRING().getText(), newSymbol, None)
        self.visitChildren(ctx)
    
    def visitBool(self, ctx:grammarYaplParser.BoolContext):
        # newSymbol = symbol(ctx.TYPE_ID(0), ctx.expr(), ctx.start.line, self.scope)
        newSymbol = symbol(ctx.TYPE_ID(0), "BOOL", ctx.start.line, self.scope)
        # self.symbol_table.add(ctx.TYPE_ID(0), newSymbol, None)
        self.visitChildren(ctx)
        
    def visitMulDiv(self, ctx:grammarYaplParser.MulDivContext):
        self.visitChildren(ctx)

    def visitIsvoid(self, ctx:grammarYaplParser.IsvoidContext):
        # newSymbol = symbol(ctx.TYPE_ID(0), "IS VOID", ctx.start.line, ctx.TYPE_ID(0))
        # self.symbol_table.add(ctx.TYPE_ID(0), newSymbol, None)
        self.visitChildren(ctx)
    
    def visitType_id(self, ctx:grammarYaplParser.Type_idContext):        
        newSymbol = symbol(ctx.TYPE_ID().getText(), "TYPE", ctx.start.line, self.scope)
        # self.symbol_table.add(ctx.TYPE_ID().getText(), newSymbol, None)
        self.visitChildren(ctx)
    
    def visitInteger(self, ctx:grammarYaplParser.IntegerContext):
        newSymbol = symbol(ctx.INTEGER().getText(), "INTEGER", ctx.start.line, self.scope)
        # self.symbol_table.add(ctx.INTEGER().getText(), newSymbol, None)
        self.visitChildren(ctx)
    
    def visitStatic_dispatch(self, ctx:grammarYaplParser.Static_dispatchContext):
        self.visitChildren(ctx)
    
    def visitWhile(self, ctx:grammarYaplParser.WhileContext):
        # #self.symbol_table.add(ctx.WHILE().getText(), None, None)
        self.visitChildren(ctx)
    
    def visitEq(self, ctx:grammarYaplParser.EqContext):
        self.visitChildren(ctx)
    
    def visitParenthesis(self, ctx:grammarYaplParser.ParenthesisContext):
        self.visitChildren(ctx)
    
    def visitObject_id(self, ctx:grammarYaplParser.Object_idContext):
        # newSymbol = symbol(ctx.TYPE_ID, str(ctx.expr()), ctx.start.line, ctx.TYPE_ID(0))
        # # self.symbol_table.add(ctx.TYPE_ID(0), newSymbol, None)
        self.visitChildren(ctx)
    
    def visitNeg(self, ctx:grammarYaplParser.NegContext):
        self.visitChildren(ctx)
    
    def visitNot(self, ctx:grammarYaplParser.NotContext):
        print(dir(ctx))
        # This line assumes that ctx.NOT() gives you the intended information.
        newSymbol = symbol(ctx.NOT(), "NOT", ctx.start.line, self.scope) 
        # self.symbol_table.add(ctx.NOT(), newSymbol, None)
        self.visitChildren(ctx)
    
    def visitSelf(self, ctx:grammarYaplParser.SelfContext):
        # newSymbol = symbol(ctx.self().getText(), str(ctx.expr()), ctx.start.line, ctx.self().getText())
        # # self.symbol_table.add(ctx.self().getText(), newSymbol, None)
        self.visitChildren(ctx)
    
    def visitBlock(self, ctx:grammarYaplParser.BlockContext):
        self.visitChildren(ctx)
    
    def visitLet(self, ctx:grammarYaplParser.LetContext):
        newSymbol = symbol(ctx.LET().getText(), "LET", ctx.start.line, self.scope)
        self.symbol_table.add(ctx.LET().getText(), newSymbol, None, None, self.getByte("Let"), None)
        for i in range(len(ctx.OBJECT_ID())):
            if(ctx.TYPE_ID(i) != None):
                print(ctx)
                name = ctx.OBJECT_ID(i).getText()
                print(name)
                data_type = ctx.TYPE_ID(i).getText()
                print(data_type)
                newSymbol = symbol(name, data_type, ctx.start.line, self.scope)
                self.symbol_table.add(name, newSymbol, None, None, self.getByte(data_type), None)
        self.visitChildren(ctx)
    
    def visitIf(self, ctx:grammarYaplParser.IfContext):
        newSymbol = symbol(ctx.IF().getText(), "IF", ctx.start.line, self.scope)
        # self.symbol_table.add(ctx.IF().getText(), newSymbol, None)
        self.visitChildren(ctx)
    
    def visitAssign(self, ctx:grammarYaplParser.AssignContext):
        self.visitChildren(ctx)

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
        #print('*' * 50)
        #print("LLEGAMOS A ADD!")
        #print(ctx.getText())
        #print('     * ',ctx.__class__)

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

        #print('     * ',ctx.__class__)
        #print('*' * 50)


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
