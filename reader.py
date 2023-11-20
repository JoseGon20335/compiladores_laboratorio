#reader.py
from antlr4 import *
import antlr4
from prettytable import PrettyTable
from antlr_build.grammarYaplLexer import grammarYaplLexer
from antlr_build.grammarYaplParser import grammarYaplParser
from antlr_build.grammarYaplVisitor import grammarYaplVisitor
from visitor_yapl import visitor_yapl
from CustomErrorListener import CustomErrorListener
from codigo_intermedio import codigo_intermedio

class reader():

    def __init__(self, input):
        self.input = input
        self.token = None
        self.errors = []

    def getErrors(self):
        return self.errors

    def readTokensSintaxis(self):
        
        # Generar el lexer
        gramLexer = grammarYaplLexer(self.input)
        gramLexer.removeErrorListeners()
        customError = CustomErrorListener()
        gramLexer.addErrorListener(customError)

        stream = antlr4.CommonTokenStream(gramLexer)
        stream.fill()

        print("CUSTOM ERROR LISTENER_________________________________________________________")
        for i in customError.return_errors():
            self.errors.append(i)
            print(i)

        #print("TOKENS_________________________________________________________")
        self.token = stream
        #for token in stream.getTokens(start=0, stop=stream.tokens.__len__()):
        #    # self.tokenNames.append(token)
        #    print("Token:" + str(token.type) + " Line:" + str(token.line) + " Column:" + str(token.column) + " Text:" + str(token.text))


    def readSymbolTable(self):
        print("SYMBOL TABLE_________________________________________________________")

        parser = grammarYaplParser(self.token)
        tree = parser.program()
        visitorInstance = visitor_yapl()
        # Este visit llamado es el que pertenece a la calse Tree, el cual llama al método accfept que pertenece al parser (aclaración por ambigüedad)
        visitorInstance.visit(tree)
        visitorInstance.fixable()
        retornable = visitorInstance.get_symbol_table()

        print("BOTTOMUP VALIDATOR_________________________________________________________")

        # validator = bottomUpValidator(retornable)
        # validator.visitDeep(tree)

        print("CODIGO INTERMEIDO_________________________________________________________")

        visitorInstance2 = codigo_intermedio("codigo_intermedio", retornable, grammarYaplLexer.symbolicNames)
        visitorInstance2.visit(tree)
        codigoIntermedio = visitorInstance2.write_to_file()

        return codigoIntermedio