# Generated from antlr_build/grammarYapl.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,50,186,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,3,1,22,8,1,1,1,1,1,1,1,1,1,
        5,1,28,8,1,10,1,12,1,31,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,5,2,40,8,
        2,10,2,12,2,43,9,2,3,2,45,8,2,1,2,3,2,48,8,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,61,8,2,3,2,63,8,2,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,78,8,4,10,4,12,4,81,9,4,3,
        4,83,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,4,4,104,8,4,11,4,12,4,105,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,3,4,116,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,124,8,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,148,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,165,8,4,1,4,1,4,1,4,1,4,1,4,1,
        4,5,4,173,8,4,10,4,12,4,176,9,4,3,4,178,8,4,1,4,5,4,181,8,4,10,4,
        12,4,184,9,4,1,4,0,1,8,5,0,2,4,6,8,0,4,1,0,16,17,1,0,37,38,1,0,39,
        40,1,0,41,42,218,0,13,1,0,0,0,2,17,1,0,0,0,4,62,1,0,0,0,6,64,1,0,
        0,0,8,147,1,0,0,0,10,11,3,2,1,0,11,12,5,32,0,0,12,14,1,0,0,0,13,
        10,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,
        0,17,18,5,2,0,0,18,21,5,16,0,0,19,20,5,7,0,0,20,22,5,16,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,29,5,27,0,0,24,25,3,4,2,0,
        25,26,5,32,0,0,26,28,1,0,0,0,27,24,1,0,0,0,28,31,1,0,0,0,29,27,1,
        0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,28,0,0,33,
        3,1,0,0,0,34,47,5,17,0,0,35,44,5,25,0,0,36,41,3,6,3,0,37,38,5,33,
        0,0,38,40,3,6,3,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,44,36,1,0,0,0,44,45,1,0,0,0,
        45,46,1,0,0,0,46,48,5,26,0,0,47,35,1,0,0,0,47,48,1,0,0,0,48,49,1,
        0,0,0,49,50,5,31,0,0,50,51,5,16,0,0,51,52,5,27,0,0,52,53,3,8,4,0,
        53,54,5,28,0,0,54,63,1,0,0,0,55,56,7,0,0,0,56,57,5,31,0,0,57,60,
        5,16,0,0,58,59,5,50,0,0,59,61,3,8,4,0,60,58,1,0,0,0,60,61,1,0,0,
        0,61,63,1,0,0,0,62,34,1,0,0,0,62,55,1,0,0,0,63,5,1,0,0,0,64,65,5,
        17,0,0,65,66,5,31,0,0,66,67,5,16,0,0,67,7,1,0,0,0,68,69,6,4,-1,0,
        69,70,7,0,0,0,70,71,5,50,0,0,71,148,3,8,4,23,72,73,7,0,0,0,73,82,
        5,25,0,0,74,79,3,8,4,0,75,76,5,33,0,0,76,78,3,8,4,0,77,75,1,0,0,
        0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,83,1,0,0,0,81,79,
        1,0,0,0,82,74,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,148,5,26,0,
        0,85,86,5,5,0,0,86,87,3,8,4,0,87,88,5,11,0,0,88,89,3,8,4,0,89,90,
        5,3,0,0,90,91,3,8,4,0,91,92,5,4,0,0,92,148,1,0,0,0,93,94,5,12,0,
        0,94,95,3,8,4,0,95,96,5,9,0,0,96,97,3,8,4,0,97,98,5,10,0,0,98,148,
        1,0,0,0,99,103,5,27,0,0,100,101,3,8,4,0,101,102,5,32,0,0,102,104,
        1,0,0,0,103,100,1,0,0,0,104,105,1,0,0,0,105,103,1,0,0,0,105,106,
        1,0,0,0,106,107,1,0,0,0,107,108,5,28,0,0,108,148,1,0,0,0,109,110,
        5,15,0,0,110,111,7,0,0,0,111,112,5,31,0,0,112,115,5,16,0,0,113,114,
        5,50,0,0,114,116,3,8,4,0,115,113,1,0,0,0,115,116,1,0,0,0,116,117,
        1,0,0,0,117,118,5,33,0,0,118,119,7,0,0,0,119,120,5,31,0,0,120,123,
        5,16,0,0,121,122,5,50,0,0,122,124,3,8,4,0,123,121,1,0,0,0,123,124,
        1,0,0,0,124,125,1,0,0,0,125,126,5,6,0,0,126,148,3,8,4,17,127,128,
        5,13,0,0,128,148,5,16,0,0,129,130,5,8,0,0,130,148,3,8,4,15,131,132,
        5,40,0,0,132,148,3,8,4,12,133,134,5,35,0,0,134,148,3,8,4,11,135,
        136,5,14,0,0,136,148,3,8,4,8,137,138,5,25,0,0,138,139,3,8,4,0,139,
        140,5,26,0,0,140,148,1,0,0,0,141,148,5,16,0,0,142,148,5,17,0,0,143,
        148,5,18,0,0,144,148,5,20,0,0,145,148,5,19,0,0,146,148,5,1,0,0,147,
        68,1,0,0,0,147,72,1,0,0,0,147,85,1,0,0,0,147,93,1,0,0,0,147,99,1,
        0,0,0,147,109,1,0,0,0,147,127,1,0,0,0,147,129,1,0,0,0,147,131,1,
        0,0,0,147,133,1,0,0,0,147,135,1,0,0,0,147,137,1,0,0,0,147,141,1,
        0,0,0,147,142,1,0,0,0,147,143,1,0,0,0,147,144,1,0,0,0,147,145,1,
        0,0,0,147,146,1,0,0,0,148,182,1,0,0,0,149,150,10,14,0,0,150,151,
        7,1,0,0,151,181,3,8,4,15,152,153,10,13,0,0,153,154,7,2,0,0,154,181,
        3,8,4,14,155,156,10,10,0,0,156,157,7,3,0,0,157,181,3,8,4,11,158,
        159,10,9,0,0,159,160,5,43,0,0,160,181,3,8,4,10,161,164,10,22,0,0,
        162,163,5,36,0,0,163,165,5,16,0,0,164,162,1,0,0,0,164,165,1,0,0,
        0,165,166,1,0,0,0,166,167,5,34,0,0,167,168,7,0,0,0,168,177,5,25,
        0,0,169,174,3,8,4,0,170,171,5,33,0,0,171,173,3,8,4,0,172,170,1,0,
        0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,178,1,0,
        0,0,176,174,1,0,0,0,177,169,1,0,0,0,177,178,1,0,0,0,178,179,1,0,
        0,0,179,181,5,26,0,0,180,149,1,0,0,0,180,152,1,0,0,0,180,155,1,0,
        0,0,180,158,1,0,0,0,180,161,1,0,0,0,181,184,1,0,0,0,182,180,1,0,
        0,0,182,183,1,0,0,0,183,9,1,0,0,0,184,182,1,0,0,0,19,15,21,29,41,
        44,47,60,62,79,82,105,115,123,147,164,174,177,180,182
    ]

class grammarYaplParser ( Parser ):

    grammarFileName = "grammarYapl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'self'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'let'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "':'", "';'", "','", "'.'", 
                     "'~'", "'@'", "'*'", "'/'", "'+'", "'-'", "'<='", "'<'", 
                     "'='", "'++'", "'--'", "'=*'", "'=/'", "'=+'", "'=-'", 
                     "'<-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "CLASS", "ELSE", "FI", "IF", 
                      "IN", "INHERITS", "ISVOID", "LOOP", "POOL", "THEN", 
                      "WHILE", "NEW", "NOT", "LET", "TYPE_ID", "OBJECT_ID", 
                      "INTEGER", "BOOL", "STRING", "WHITESPACE", "NEWLINE", 
                      "COMMENT", "COMMENT_BLOCK", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LBRACKET", "RBRACKET", "COLON", "SEMICOLON", 
                      "COMMA", "DOT", "NEG", "AT", "MULT", "DIV", "PLUS", 
                      "MINUS", "LE", "LT", "EQ", "INCR", "DECR", "ASSIGN_MULT", 
                      "ASSIGN_DIV", "ASSIGN_PLUS", "ASSIGN_MINUS", "ASSIGN" ]

    RULE_program = 0
    RULE_class_def = 1
    RULE_feature = 2
    RULE_formal = 3
    RULE_expr = 4

    ruleNames =  [ "program", "class_def", "feature", "formal", "expr" ]

    EOF = Token.EOF
    T__0=1
    CLASS=2
    ELSE=3
    FI=4
    IF=5
    IN=6
    INHERITS=7
    ISVOID=8
    LOOP=9
    POOL=10
    THEN=11
    WHILE=12
    NEW=13
    NOT=14
    LET=15
    TYPE_ID=16
    OBJECT_ID=17
    INTEGER=18
    BOOL=19
    STRING=20
    WHITESPACE=21
    NEWLINE=22
    COMMENT=23
    COMMENT_BLOCK=24
    LPAREN=25
    RPAREN=26
    LBRACE=27
    RBRACE=28
    LBRACKET=29
    RBRACKET=30
    COLON=31
    SEMICOLON=32
    COMMA=33
    DOT=34
    NEG=35
    AT=36
    MULT=37
    DIV=38
    PLUS=39
    MINUS=40
    LE=41
    LT=42
    EQ=43
    INCR=44
    DECR=45
    ASSIGN_MULT=46
    ASSIGN_DIV=47
    ASSIGN_PLUS=48
    ASSIGN_MINUS=49
    ASSIGN=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.Class_defContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.Class_defContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.SEMICOLON)
            else:
                return self.getToken(grammarYaplParser.SEMICOLON, i)

        def getRuleIndex(self):
            return grammarYaplParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = grammarYaplParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.class_def()
                self.state = 11
                self.match(grammarYaplParser.SEMICOLON)
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(grammarYaplParser.CLASS, 0)

        def TYPE_ID(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.TYPE_ID)
            else:
                return self.getToken(grammarYaplParser.TYPE_ID, i)

        def LBRACE(self):
            return self.getToken(grammarYaplParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(grammarYaplParser.RBRACE, 0)

        def INHERITS(self):
            return self.getToken(grammarYaplParser.INHERITS, 0)

        def feature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.FeatureContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.FeatureContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.SEMICOLON)
            else:
                return self.getToken(grammarYaplParser.SEMICOLON, i)

        def getRuleIndex(self):
            return grammarYaplParser.RULE_class_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_def" ):
                listener.enterClass_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_def" ):
                listener.exitClass_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_def" ):
                return visitor.visitClass_def(self)
            else:
                return visitor.visitChildren(self)




    def class_def(self):

        localctx = grammarYaplParser.Class_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(grammarYaplParser.CLASS)
            self.state = 18
            self.match(grammarYaplParser.TYPE_ID)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 19
                self.match(grammarYaplParser.INHERITS)
                self.state = 20
                self.match(grammarYaplParser.TYPE_ID)


            self.state = 23
            self.match(grammarYaplParser.LBRACE)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 24
                self.feature()
                self.state = 25
                self.match(grammarYaplParser.SEMICOLON)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(grammarYaplParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_ID(self):
            return self.getToken(grammarYaplParser.OBJECT_ID, 0)

        def COLON(self):
            return self.getToken(grammarYaplParser.COLON, 0)

        def TYPE_ID(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.TYPE_ID)
            else:
                return self.getToken(grammarYaplParser.TYPE_ID, i)

        def LBRACE(self):
            return self.getToken(grammarYaplParser.LBRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(grammarYaplParser.ExprContext,0)


        def RBRACE(self):
            return self.getToken(grammarYaplParser.RBRACE, 0)

        def LPAREN(self):
            return self.getToken(grammarYaplParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(grammarYaplParser.RPAREN, 0)

        def formal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.FormalContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.FormalContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.COMMA)
            else:
                return self.getToken(grammarYaplParser.COMMA, i)

        def ASSIGN(self):
            return self.getToken(grammarYaplParser.ASSIGN, 0)

        def getRuleIndex(self):
            return grammarYaplParser.RULE_feature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature" ):
                listener.enterFeature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature" ):
                listener.exitFeature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeature" ):
                return visitor.visitFeature(self)
            else:
                return visitor.visitChildren(self)




    def feature(self):

        localctx = grammarYaplParser.FeatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_feature)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(grammarYaplParser.OBJECT_ID)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 35
                    self.match(grammarYaplParser.LPAREN)
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==17:
                        self.state = 36
                        self.formal()
                        self.state = 41
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==33:
                            self.state = 37
                            self.match(grammarYaplParser.COMMA)
                            self.state = 38
                            self.formal()
                            self.state = 43
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)



                    self.state = 46
                    self.match(grammarYaplParser.RPAREN)


                self.state = 49
                self.match(grammarYaplParser.COLON)
                self.state = 50
                self.match(grammarYaplParser.TYPE_ID)
                self.state = 51
                self.match(grammarYaplParser.LBRACE)
                self.state = 52
                self.expr(0)
                self.state = 53
                self.match(grammarYaplParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 56
                self.match(grammarYaplParser.COLON)
                self.state = 57
                self.match(grammarYaplParser.TYPE_ID)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==50:
                    self.state = 58
                    self.match(grammarYaplParser.ASSIGN)
                    self.state = 59
                    self.expr(0)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT_ID(self):
            return self.getToken(grammarYaplParser.OBJECT_ID, 0)

        def COLON(self):
            return self.getToken(grammarYaplParser.COLON, 0)

        def TYPE_ID(self):
            return self.getToken(grammarYaplParser.TYPE_ID, 0)

        def getRuleIndex(self):
            return grammarYaplParser.RULE_formal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal" ):
                listener.enterFormal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal" ):
                listener.exitFormal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal" ):
                return visitor.visitFormal(self)
            else:
                return visitor.visitChildren(self)




    def formal(self):

        localctx = grammarYaplParser.FormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_formal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(grammarYaplParser.OBJECT_ID)
            self.state = 65
            self.match(grammarYaplParser.COLON)
            self.state = 66
            self.match(grammarYaplParser.TYPE_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarYaplParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NewContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(grammarYaplParser.NEW, 0)
        def TYPE_ID(self):
            return self.getToken(grammarYaplParser.TYPE_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNew" ):
                listener.enterNew(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNew" ):
                listener.exitNew(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew" ):
                return visitor.visitNew(self)
            else:
                return visitor.visitChildren(self)


    class MinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(grammarYaplParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(grammarYaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinus" ):
                listener.enterMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinus" ):
                listener.exitMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinus" ):
                return visitor.visitMinus(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)

        def LE(self):
            return self.getToken(grammarYaplParser.LE, 0)
        def LT(self):
            return self.getToken(grammarYaplParser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)


    class DispatchContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)

        def DOT(self):
            return self.getToken(grammarYaplParser.DOT, 0)
        def LPAREN(self):
            return self.getToken(grammarYaplParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(grammarYaplParser.RPAREN, 0)
        def TYPE_ID(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.TYPE_ID)
            else:
                return self.getToken(grammarYaplParser.TYPE_ID, i)
        def OBJECT_ID(self):
            return self.getToken(grammarYaplParser.OBJECT_ID, 0)
        def AT(self):
            return self.getToken(grammarYaplParser.AT, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.COMMA)
            else:
                return self.getToken(grammarYaplParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDispatch" ):
                listener.enterDispatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDispatch" ):
                listener.exitDispatch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDispatch" ):
                return visitor.visitDispatch(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(grammarYaplParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(grammarYaplParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class IsvoidContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ISVOID(self):
            return self.getToken(grammarYaplParser.ISVOID, 0)
        def expr(self):
            return self.getTypedRuleContext(grammarYaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsvoid" ):
                listener.enterIsvoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsvoid" ):
                listener.exitIsvoid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsvoid" ):
                return visitor.visitIsvoid(self)
            else:
                return visitor.visitChildren(self)


    class Type_idContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE_ID(self):
            return self.getToken(grammarYaplParser.TYPE_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_id" ):
                listener.enterType_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_id" ):
                listener.exitType_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_id" ):
                return visitor.visitType_id(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(grammarYaplParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(grammarYaplParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class IntegerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(grammarYaplParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class Static_dispatchContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(grammarYaplParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(grammarYaplParser.RPAREN, 0)
        def TYPE_ID(self):
            return self.getToken(grammarYaplParser.TYPE_ID, 0)
        def OBJECT_ID(self):
            return self.getToken(grammarYaplParser.OBJECT_ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.COMMA)
            else:
                return self.getToken(grammarYaplParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic_dispatch" ):
                listener.enterStatic_dispatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic_dispatch" ):
                listener.exitStatic_dispatch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_dispatch" ):
                return visitor.visitStatic_dispatch(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(grammarYaplParser.WHILE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)

        def LOOP(self):
            return self.getToken(grammarYaplParser.LOOP, 0)
        def POOL(self):
            return self.getToken(grammarYaplParser.POOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class EqContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)

        def EQ(self):
            return self.getToken(grammarYaplParser.EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq" ):
                listener.enterEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq" ):
                listener.exitEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq" ):
                return visitor.visitEq(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(grammarYaplParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(grammarYaplParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(grammarYaplParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class Object_idContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJECT_ID(self):
            return self.getToken(grammarYaplParser.OBJECT_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_id" ):
                listener.enterObject_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_id" ):
                listener.exitObject_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_id" ):
                return visitor.visitObject_id(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)

        def MULT(self):
            return self.getToken(grammarYaplParser.MULT, 0)
        def DIV(self):
            return self.getToken(grammarYaplParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class NegContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEG(self):
            return self.getToken(grammarYaplParser.NEG, 0)
        def expr(self):
            return self.getTypedRuleContext(grammarYaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeg" ):
                listener.enterNeg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeg" ):
                listener.exitNeg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg" ):
                return visitor.visitNeg(self)
            else:
                return visitor.visitChildren(self)


    class NotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(grammarYaplParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(grammarYaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class SelfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelf" ):
                listener.enterSelf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelf" ):
                listener.exitSelf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelf" ):
                return visitor.visitSelf(self)
            else:
                return visitor.visitChildren(self)


    class BlockContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(grammarYaplParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(grammarYaplParser.RBRACE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.SEMICOLON)
            else:
                return self.getToken(grammarYaplParser.SEMICOLON, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)


    class LetContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(grammarYaplParser.LET, 0)
        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.COLON)
            else:
                return self.getToken(grammarYaplParser.COLON, i)
        def TYPE_ID(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.TYPE_ID)
            else:
                return self.getToken(grammarYaplParser.TYPE_ID, i)
        def IN(self):
            return self.getToken(grammarYaplParser.IN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)

        def OBJECT_ID(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.OBJECT_ID)
            else:
                return self.getToken(grammarYaplParser.OBJECT_ID, i)
        def COMMA(self):
            return self.getToken(grammarYaplParser.COMMA, 0)
        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.ASSIGN)
            else:
                return self.getToken(grammarYaplParser.ASSIGN, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet" ):
                return visitor.visitLet(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(grammarYaplParser.IF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)

        def THEN(self):
            return self.getToken(grammarYaplParser.THEN, 0)
        def ELSE(self):
            return self.getToken(grammarYaplParser.ELSE, 0)
        def FI(self):
            return self.getToken(grammarYaplParser.FI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ASSIGN(self):
            return self.getToken(grammarYaplParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(grammarYaplParser.ExprContext,0)

        def TYPE_ID(self):
            return self.getToken(grammarYaplParser.TYPE_ID, 0)
        def OBJECT_ID(self):
            return self.getToken(grammarYaplParser.OBJECT_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = grammarYaplParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = grammarYaplParser.AssignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 69
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self.match(grammarYaplParser.ASSIGN)
                self.state = 71
                self.expr(23)
                pass

            elif la_ == 2:
                localctx = grammarYaplParser.Static_dispatchContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 73
                self.match(grammarYaplParser.LPAREN)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134041231650) != 0):
                    self.state = 74
                    self.expr(0)
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==33:
                        self.state = 75
                        self.match(grammarYaplParser.COMMA)
                        self.state = 76
                        self.expr(0)
                        self.state = 81
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 84
                self.match(grammarYaplParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = grammarYaplParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 85
                self.match(grammarYaplParser.IF)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(grammarYaplParser.THEN)
                self.state = 88
                self.expr(0)
                self.state = 89
                self.match(grammarYaplParser.ELSE)
                self.state = 90
                self.expr(0)
                self.state = 91
                self.match(grammarYaplParser.FI)
                pass

            elif la_ == 4:
                localctx = grammarYaplParser.WhileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                self.match(grammarYaplParser.WHILE)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(grammarYaplParser.LOOP)
                self.state = 96
                self.expr(0)
                self.state = 97
                self.match(grammarYaplParser.POOL)
                pass

            elif la_ == 5:
                localctx = grammarYaplParser.BlockContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.match(grammarYaplParser.LBRACE)
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 100
                    self.expr(0)
                    self.state = 101
                    self.match(grammarYaplParser.SEMICOLON)
                    self.state = 105 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1134041231650) != 0)):
                        break

                self.state = 107
                self.match(grammarYaplParser.RBRACE)
                pass

            elif la_ == 6:
                localctx = grammarYaplParser.LetContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(grammarYaplParser.LET)
                self.state = 110
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 111
                self.match(grammarYaplParser.COLON)
                self.state = 112
                self.match(grammarYaplParser.TYPE_ID)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==50:
                    self.state = 113
                    self.match(grammarYaplParser.ASSIGN)
                    self.state = 114
                    self.expr(0)


                self.state = 117
                self.match(grammarYaplParser.COMMA)
                self.state = 118
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.match(grammarYaplParser.COLON)
                self.state = 120
                self.match(grammarYaplParser.TYPE_ID)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==50:
                    self.state = 121
                    self.match(grammarYaplParser.ASSIGN)
                    self.state = 122
                    self.expr(0)


                self.state = 125
                self.match(grammarYaplParser.IN)
                self.state = 126
                self.expr(17)
                pass

            elif la_ == 7:
                localctx = grammarYaplParser.NewContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 127
                self.match(grammarYaplParser.NEW)
                self.state = 128
                self.match(grammarYaplParser.TYPE_ID)
                pass

            elif la_ == 8:
                localctx = grammarYaplParser.IsvoidContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 129
                self.match(grammarYaplParser.ISVOID)
                self.state = 130
                self.expr(15)
                pass

            elif la_ == 9:
                localctx = grammarYaplParser.MinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(grammarYaplParser.MINUS)
                self.state = 132
                self.expr(12)
                pass

            elif la_ == 10:
                localctx = grammarYaplParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(grammarYaplParser.NEG)
                self.state = 134
                self.expr(11)
                pass

            elif la_ == 11:
                localctx = grammarYaplParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(grammarYaplParser.NOT)
                self.state = 136
                self.expr(8)
                pass

            elif la_ == 12:
                localctx = grammarYaplParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(grammarYaplParser.LPAREN)
                self.state = 138
                self.expr(0)
                self.state = 139
                self.match(grammarYaplParser.RPAREN)
                pass

            elif la_ == 13:
                localctx = grammarYaplParser.Type_idContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 141
                self.match(grammarYaplParser.TYPE_ID)
                pass

            elif la_ == 14:
                localctx = grammarYaplParser.Object_idContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.match(grammarYaplParser.OBJECT_ID)
                pass

            elif la_ == 15:
                localctx = grammarYaplParser.IntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 143
                self.match(grammarYaplParser.INTEGER)
                pass

            elif la_ == 16:
                localctx = grammarYaplParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(grammarYaplParser.STRING)
                pass

            elif la_ == 17:
                localctx = grammarYaplParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.match(grammarYaplParser.BOOL)
                pass

            elif la_ == 18:
                localctx = grammarYaplParser.SelfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(grammarYaplParser.T__0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 182
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 180
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = grammarYaplParser.MulDivContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 149
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 150
                        _la = self._input.LA(1)
                        if not(_la==37 or _la==38):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 151
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = grammarYaplParser.AddSubContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 152
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 153
                        _la = self._input.LA(1)
                        if not(_la==39 or _la==40):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 154
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = grammarYaplParser.ComparisonContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 155
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 156
                        _la = self._input.LA(1)
                        if not(_la==41 or _la==42):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 157
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = grammarYaplParser.EqContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 158
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 159
                        self.match(grammarYaplParser.EQ)
                        self.state = 160
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = grammarYaplParser.DispatchContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 161
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 164
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==36:
                            self.state = 162
                            self.match(grammarYaplParser.AT)
                            self.state = 163
                            self.match(grammarYaplParser.TYPE_ID)


                        self.state = 166
                        self.match(grammarYaplParser.DOT)
                        self.state = 167
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 168
                        self.match(grammarYaplParser.LPAREN)
                        self.state = 177
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1134041231650) != 0):
                            self.state = 169
                            self.expr(0)
                            self.state = 174
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==33:
                                self.state = 170
                                self.match(grammarYaplParser.COMMA)
                                self.state = 171
                                self.expr(0)
                                self.state = 176
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 179
                        self.match(grammarYaplParser.RPAREN)
                        pass

             
                self.state = 184
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 22)
         




