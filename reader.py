#reader.py
from antlr4 import *
import antlr4
from prettytable import PrettyTable
from antlr_build.grammarYaplLexer import grammarYaplLexer
from antlr_build.grammarYaplParser import grammarYaplParser
from antlr_build.grammarYaplVisitor import grammarYaplVisitor
from visitor_yapl import visitor_yapl, bottomUpValidator
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
        retornable = visitorInstance.get_symbol_table()
        #visitorInstance.diagnosis(tree)

        print(retornable)

        myTab = PrettyTable(["ID", "Type", "Line", "Scope", "Inherit", "Params", "Byte", "Offset"])
        # Add rows
        for i in retornable:
            # Splitting the 'keyId' on the dot and taking the last part
            symbol_name = i['keyId'].split('.')[-1]
            myTab.add_row([symbol_name, i['type'], i['line'], i['scope'], i['inherit'], i['params'], i['byte'], i['offset']])

        print(myTab)
        # print("BOTTOMUP VALIDATOR_________________________________________________________")

        # validator = bottomUpValidator(visitorInstance.symbol_table)
        # validator.visitDeep(tree)

        print("CODIGO INTERMEIDO_________________________________________________________")

        visitorInstance2 = codigo_intermedio("codigo_intermedio", visitorInstance.symbol_table, grammarYaplLexer.symbolicNames)
        visitorInstance2.visit(tree)
        codigoIntermedio = visitorInstance2.write_to_file()

        return codigoIntermedio