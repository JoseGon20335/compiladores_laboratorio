# Custom Error Listener
from antlr4.error.ErrorListener import ErrorListener
import subprocess
import os
from antlr4 import *
import antlr4
from prettytable import PrettyTable
from antlr_build.grammarYaplLexer import grammarYaplLexer
from antlr_build.grammarYaplParser import grammarYaplParser
from antlr_build.grammarYaplVisitor import grammarYaplVisitor

# Custom error listener class
class CustomErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_errors = False
        self.error_messages = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True
        error_message = f"Syntax error at line {line}, column {column}: {msg}"
        self.error_messages.append(error_message)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

    def get_all_errors(self):
        return self.error_messages
    
    def return_errors(self):
        temp = ""
        for i in self.error_messages:
            temp += i + "\n"
        return temp
