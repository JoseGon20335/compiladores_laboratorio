#visitor_yapl.py
from antlr4 import *
from symbol_table import symbol_table, symbol
from antlr_build.grammarYaplVisitor import grammarYaplVisitor
from antlr_build.grammarYaplParser import grammarYaplParser
    
class visitor_bottom(grammarYaplVisitor):

    def __init__(self):
        self.symbol_table = symbol_table()
        self.scope = "GLOBAL"
        self.defaultMethods = {
            "IO": {"out_string": [["String"], "IO"], "out_int": [["Int"], "IO"], "in_string": [[], "String"], "in_int": [[], "Int"]},
            "Object": {"abort": [[], "Object"], "type_name": [[], "String"], "copy": [[], "SELF_TYPE"]},
            "String": {"length": [[], "Int"], "concat": [["String"], "String"], "substr": [["Int", "Int"], "String"]}
        }

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
