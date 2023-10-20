import subprocess
import os
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
from antlr_build.grammarYaplLexer import grammarYaplLexer
from antlr_build.grammarYaplParser import grammarYaplParser

# Ejemplo basado en el ejemplo de la clase, pero con un mismatch de tipos
entrada = """
class Number {
    var : Int;
 
    set_value(value: Int) : Number {
       {
          var <- value;
          self;
       }
    };
 
    value() : Int {
       var
    };
};

class Example {
    a : Number;
    b : Number;
    c : Number;
    d : Bool;
 
    main() : Int {
       {
          a <- Number.set_value(1);
          b <- Number.set_value(2);
          c <- Number.set_value(3);
          a.set_value(a.value() + b.value() * c.value());
          a.value();
          d <- a.value();
       }
    };
};
"""

#print(entrada)

lexer = grammarYaplLexer(InputStream(entrada))
token_stream = CommonTokenStream(lexer)
parser = grammarYaplParser(token_stream)
tree = parser.program()

# loop through the tre


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


dummy = STable()
print('-' * 50)
print(dummy.empty())
print(' - ', dummy.current_scope)
dummy.bind("a", "int", 0)
dummy.bind("b", "int", 0)
dummy.bind("c", "int", 0)
print('-' * 50)
dummy.print()
print('-' * 50)
print(dummy.look_up("a"))
print('-' * 50)
dummy.enter()
print(' - ', dummy.current_scope)
dummy.bind("a", "bool", 1)
dummy.bind("b", "bool", 1)
dummy.bind("c", "bool", 1)
dummy.bind("d", "bool", 1)
print(dummy.look_up("a"))
print(dummy.look_up("d"))
print('-' * 50)
dummy.exit()
print(' - ', dummy.current_scope)
print(dummy.look_up("d"))
dummy.bind("a", "bool", 0)
dummy.print()
dummy.exit()
            