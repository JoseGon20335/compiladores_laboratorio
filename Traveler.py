from antlr_build.grammarYaplVisitor import grammarYaplVisitor

from antlr4 import *
from antlr_build.grammarYaplVisitor import grammarYaplVisitor
from antlr_build.grammarYaplParser import grammarYaplParser


"""prueba = TablaSimbolos()
print(prueba.empty())
prueba.enter()
print(prueba.empty())
print('-'*50)
prueba.bind("a", "int")
prueba.bind("b", "int")
prueba.bind("c", "int")
print(prueba.look_up("a"))
#prueba.print()
print(prueba.get_table_current_scope())
print('-'*50)

prueba.enter()
prueba.bind("a", "bool")
prueba.bind("b", "bool")
prueba.bind("c", "bool")
print(prueba.look_up("a"))
print(prueba.get_table_current_scope())
print('-'*50)

prueba.exit()
print(prueba.look_up("a"))
print(prueba.get_table_current_scope())
print('-'*50)
prueba.print()"""


class STable:
    
    def __init__(self):
        self.table = []
        self.current_scope = 0

    def empty(self):
        return len(self.table) == 0
    
    def enter(self):
        self.current_scope = self.current_scope + 1

    def exit(self):
        if self.current_scope == 0:
            #raise Exception("No se puede salir del scope global")
            print("No se puede salir del scope global")
        else:
            self.current_scope = self.current_scope - 1

    def look_up(self, symbol):
        #print(self.current_scope)
        #print(' Largo de la tabla: ', len(self.table))
        for e in self.table:
            #print(e, e['id'], e['scope'])
            if e['id'] == symbol and e['scope'] == self.current_scope:
                #print(' - llegue')
                return e
        return None
    

    
    def bind(self, id, type, scope):
        new_entry = {
            'id': id,
            'type': type,
            'scope': scope
        }
        if self.look_up(id) is None:
            self.table.append(new_entry)
        else:
            #raise Exception("Identifier already exists in current scope")
            print(f"Identifier {id} already exists in current scope")
        
    def print(self):
        for e in self.table:
            print(f"ID: {e['id']}, Type: {e['type']}, Scope: {e['scope']}")




class TheTraveler(grammarYaplVisitor):
    
    def __init__(self):
        self.symbol_table = STable()  # Use your STable class as the symbol table

    def get_symbol_table(self):
        return self.symbol_table

    def visitProgram(self, ctx: grammarYaplParser.ProgramContext):
        self.visitChildren(ctx)
        return None

    def visitClass_def(self, ctx: grammarYaplParser.Class_defContext):
        self.symbol_table.bind(ctx.TYPE().getText(), "class", self.symbol_table.current_scope)

        if len(ctx.TYPE_ID()) > 0:
            self.symbol_table.bind(ctx.TYPE_ID().getText(), "TYPE_ID", self.symbol_table.current_scope)

        self.visitChildren(ctx)
        return None

    def visitFeature(self, ctx: grammarYaplParser.FeatureContext):
        self.symbol_table.bind(ctx.OBJECT_ID().getText(), "OBJECT_ID", self.symbol_table.current_scope)

        if len(ctx.TYPE_ID()) == 1:
            self.symbol_table.bind(ctx.TYPE_ID().getText(), "TYPE_ID", self.symbol_table.current_scope)

        self.visitChildren(ctx)
        return None

    def visitFormal(self, ctx: grammarYaplParser.FormalContext):
        self.symbol_table.bind(ctx.OBJECT_ID().getText(), "OBJECT_ID", self.symbol_table.current_scope)

        if len(ctx.TYPE_ID()) == 1:
            self.symbol_table.bind(ctx.TYPE_ID().getText(), "TYPE_ID", self.symbol_table.current_scope)

        self.visitChildren(ctx)
        return None

    def visitDeclaration(self, ctx: grammarYaplParser.DeclarationContext):
        type = ctx.TYPE().getText()
        id = ctx.ID().getText()
        self.symbol_table.bind(id, type, self.symbol_table.current_scope)
        self.visitChildren(ctx)
        return None

    def visitExpr(self, ctx: grammarYaplParser.ExprContext):
        if ctx.INT():
            # Example: Handling integer literals
            # Note: Here, you may also bind the literal value with its type in the symbol table
            self.symbol_table.bind(ctx.INT().getText(), "INT", self.symbol_table.current_scope)

        if ctx.STRING():
            # Example: Handling string literals
            # Note: Here, you may also bind the literal value with its type in the symbol table
            self.symbol_table.bind(ctx.STRING().getText(), "STRING", self.symbol_table.current_scope)

        if ctx.TRUE() or ctx.FALSE():
            # Example: Handling boolean literals
            # Note: Here, you may also bind the literal value with its type in the symbol table
            self.symbol_table.bind(ctx.start.text, "BOOLEAN", self.symbol_table.current_scope)

        if ctx.SELF():
            # Example: Handling 'self'
            # Note: Here, you may also bind "self" with its type (class name) in the symbol table
            self.symbol_table.bind("self", "SELF", self.symbol_table.current_scope)

        if ctx.expr():
            # Example: Handling binary expressions (e.g., x + y)
            left_type = self.visit(ctx.expr(0))
            right_type = self.visit(ctx.expr(1))

            # Assuming you have methods to check the type of an expression (e.g., is_integer, is_string, is_boolean)
    

            # Handle other valid binary operation cases (e.g., integer - integer, string + integer, etc.)
            # Return appropriate type based on the binary operation's rules

        # Handle other expressions and return their types accordingly
        # ...

        return None