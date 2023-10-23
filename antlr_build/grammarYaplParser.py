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
        4,1,52,197,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,3,1,22,8,1,1,1,1,1,1,1,1,1,
        5,1,28,8,1,10,1,12,1,31,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,5,2,40,8,
        2,10,2,12,2,43,9,2,3,2,45,8,2,1,2,3,2,48,8,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,61,8,2,3,2,63,8,2,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,3,4,80,8,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,4,4,101,8,4,11,4,12,4,102,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,3,4,113,8,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,121,8,4,5,4,123,8,4,10,
        4,12,4,126,9,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,153,8,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,3,4,176,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,184,8,
        4,10,4,12,4,187,9,4,3,4,189,8,4,1,4,5,4,192,8,4,10,4,12,4,195,9,
        4,1,4,0,1,8,5,0,2,4,6,8,0,4,1,0,18,19,1,0,39,40,1,0,41,42,1,0,43,
        44,232,0,13,1,0,0,0,2,17,1,0,0,0,4,62,1,0,0,0,6,64,1,0,0,0,8,152,
        1,0,0,0,10,11,3,2,1,0,11,12,5,34,0,0,12,14,1,0,0,0,13,10,1,0,0,0,
        14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,18,5,4,
        0,0,18,21,5,18,0,0,19,20,5,9,0,0,20,22,5,18,0,0,21,19,1,0,0,0,21,
        22,1,0,0,0,22,23,1,0,0,0,23,29,5,29,0,0,24,25,3,4,2,0,25,26,5,34,
        0,0,26,28,1,0,0,0,27,24,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,
        1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,30,0,0,33,3,1,0,0,0,
        34,47,5,19,0,0,35,44,5,27,0,0,36,41,3,6,3,0,37,38,5,35,0,0,38,40,
        3,6,3,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,
        42,45,1,0,0,0,43,41,1,0,0,0,44,36,1,0,0,0,44,45,1,0,0,0,45,46,1,
        0,0,0,46,48,5,28,0,0,47,35,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,
        50,5,33,0,0,50,51,5,18,0,0,51,52,5,29,0,0,52,53,3,8,4,0,53,54,5,
        30,0,0,54,63,1,0,0,0,55,56,7,0,0,0,56,57,5,33,0,0,57,60,5,18,0,0,
        58,59,5,52,0,0,59,61,3,8,4,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,
        0,0,0,62,34,1,0,0,0,62,55,1,0,0,0,63,5,1,0,0,0,64,65,5,19,0,0,65,
        66,5,33,0,0,66,67,5,18,0,0,67,7,1,0,0,0,68,69,6,4,-1,0,69,70,7,0,
        0,0,70,79,5,27,0,0,71,76,3,8,4,0,72,73,5,35,0,0,73,75,3,8,4,0,74,
        72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,80,1,0,0,
        0,78,76,1,0,0,0,79,71,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,153,
        5,28,0,0,82,83,5,7,0,0,83,84,3,8,4,0,84,85,5,13,0,0,85,86,3,8,4,
        0,86,87,5,5,0,0,87,88,3,8,4,0,88,89,5,6,0,0,89,153,1,0,0,0,90,91,
        5,14,0,0,91,92,3,8,4,0,92,93,5,11,0,0,93,94,3,8,4,0,94,95,5,12,0,
        0,95,153,1,0,0,0,96,100,5,29,0,0,97,98,3,8,4,0,98,99,5,34,0,0,99,
        101,1,0,0,0,100,97,1,0,0,0,101,102,1,0,0,0,102,100,1,0,0,0,102,103,
        1,0,0,0,103,104,1,0,0,0,104,105,5,30,0,0,105,153,1,0,0,0,106,107,
        5,17,0,0,107,108,7,0,0,0,108,109,5,33,0,0,109,112,5,18,0,0,110,111,
        5,52,0,0,111,113,3,8,4,0,112,110,1,0,0,0,112,113,1,0,0,0,113,124,
        1,0,0,0,114,115,5,35,0,0,115,116,7,0,0,0,116,117,5,33,0,0,117,120,
        5,18,0,0,118,119,5,52,0,0,119,121,3,8,4,0,120,118,1,0,0,0,120,121,
        1,0,0,0,121,123,1,0,0,0,122,114,1,0,0,0,123,126,1,0,0,0,124,122,
        1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,
        5,8,0,0,128,153,3,8,4,20,129,130,5,15,0,0,130,153,5,18,0,0,131,132,
        5,37,0,0,132,153,3,8,4,18,133,134,5,10,0,0,134,153,3,8,4,17,135,
        136,5,42,0,0,136,153,3,8,4,14,137,138,5,16,0,0,138,153,3,8,4,9,139,
        140,7,0,0,0,140,141,5,52,0,0,141,153,3,8,4,8,142,143,5,27,0,0,143,
        144,3,8,4,0,144,145,5,28,0,0,145,153,1,0,0,0,146,153,5,19,0,0,147,
        153,5,20,0,0,148,153,5,22,0,0,149,153,5,21,0,0,150,153,5,18,0,0,
        151,153,5,3,0,0,152,68,1,0,0,0,152,82,1,0,0,0,152,90,1,0,0,0,152,
        96,1,0,0,0,152,106,1,0,0,0,152,129,1,0,0,0,152,131,1,0,0,0,152,133,
        1,0,0,0,152,135,1,0,0,0,152,137,1,0,0,0,152,139,1,0,0,0,152,142,
        1,0,0,0,152,146,1,0,0,0,152,147,1,0,0,0,152,148,1,0,0,0,152,149,
        1,0,0,0,152,150,1,0,0,0,152,151,1,0,0,0,153,193,1,0,0,0,154,155,
        10,16,0,0,155,156,7,1,0,0,156,192,3,8,4,17,157,158,10,15,0,0,158,
        159,7,2,0,0,159,192,3,8,4,16,160,161,10,13,0,0,161,162,7,3,0,0,162,
        192,3,8,4,14,163,164,10,12,0,0,164,165,5,1,0,0,165,192,3,8,4,13,
        166,167,10,11,0,0,167,168,5,2,0,0,168,192,3,8,4,12,169,170,10,10,
        0,0,170,171,5,45,0,0,171,192,3,8,4,11,172,175,10,25,0,0,173,174,
        5,38,0,0,174,176,5,18,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,177,
        1,0,0,0,177,178,5,36,0,0,178,179,7,0,0,0,179,188,5,27,0,0,180,185,
        3,8,4,0,181,182,5,35,0,0,182,184,3,8,4,0,183,181,1,0,0,0,184,187,
        1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,189,1,0,0,0,187,185,
        1,0,0,0,188,180,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,192,
        5,28,0,0,191,154,1,0,0,0,191,157,1,0,0,0,191,160,1,0,0,0,191,163,
        1,0,0,0,191,166,1,0,0,0,191,169,1,0,0,0,191,172,1,0,0,0,192,195,
        1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,9,1,0,0,0,195,193,1,
        0,0,0,20,15,21,29,41,44,47,60,62,76,79,102,112,120,124,152,175,185,
        188,191,193
    ]

class grammarYaplParser ( Parser ):

    grammarFileName = "grammarYapl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'&'", "'|'", "'self'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'let'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", "';'", 
                     "','", "'.'", "'~'", "'@'", "'*'", "'/'", "'+'", "'-'", 
                     "'<='", "'<'", "'='", "'++'", "'--'", "'=*'", "'=/'", 
                     "'=+'", "'=-'", "'<-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CLASS", "ELSE", "FI", "IF", "IN", "INHERITS", "ISVOID", 
                      "LOOP", "POOL", "THEN", "WHILE", "NEW", "NOT", "LET", 
                      "TYPE_ID", "OBJECT_ID", "INTEGER", "BOOL", "STRING", 
                      "WHITESPACE", "NEWLINE", "COMMENT", "COMMENT_BLOCK", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "COLON", "SEMICOLON", "COMMA", "DOT", 
                      "NEG", "AT", "MULT", "DIV", "PLUS", "MINUS", "LE", 
                      "LT", "EQ", "INCR", "DECR", "ASSIGN_MULT", "ASSIGN_DIV", 
                      "ASSIGN_PLUS", "ASSIGN_MINUS", "ASSIGN" ]

    RULE_program = 0
    RULE_class_def = 1
    RULE_feature = 2
    RULE_formal = 3
    RULE_expr = 4

    ruleNames =  [ "program", "class_def", "feature", "formal", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    CLASS=4
    ELSE=5
    FI=6
    IF=7
    IN=8
    INHERITS=9
    ISVOID=10
    LOOP=11
    POOL=12
    THEN=13
    WHILE=14
    NEW=15
    NOT=16
    LET=17
    TYPE_ID=18
    OBJECT_ID=19
    INTEGER=20
    BOOL=21
    STRING=22
    WHITESPACE=23
    NEWLINE=24
    COMMENT=25
    COMMENT_BLOCK=26
    LPAREN=27
    RPAREN=28
    LBRACE=29
    RBRACE=30
    LBRACKET=31
    RBRACKET=32
    COLON=33
    SEMICOLON=34
    COMMA=35
    DOT=36
    NEG=37
    AT=38
    MULT=39
    DIV=40
    PLUS=41
    MINUS=42
    LE=43
    LT=44
    EQ=45
    INCR=46
    DECR=47
    ASSIGN_MULT=48
    ASSIGN_DIV=49
    ASSIGN_PLUS=50
    ASSIGN_MINUS=51
    ASSIGN=52

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
                if not (_la==4):
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
            if _la==9:
                self.state = 19
                self.match(grammarYaplParser.INHERITS)
                self.state = 20
                self.match(grammarYaplParser.TYPE_ID)


            self.state = 23
            self.match(grammarYaplParser.LBRACE)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
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


        def getRuleIndex(self):
            return grammarYaplParser.RULE_feature

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MethodContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBJECT_ID(self):
            return self.getToken(grammarYaplParser.OBJECT_ID, 0)
        def COLON(self):
            return self.getToken(grammarYaplParser.COLON, 0)
        def TYPE_ID(self):
            return self.getToken(grammarYaplParser.TYPE_ID, 0)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)


    class AttributeContext(FeatureContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.FeatureContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COLON(self):
            return self.getToken(grammarYaplParser.COLON, 0)
        def TYPE_ID(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.TYPE_ID)
            else:
                return self.getToken(grammarYaplParser.TYPE_ID, i)
        def OBJECT_ID(self):
            return self.getToken(grammarYaplParser.OBJECT_ID, 0)
        def ASSIGN(self):
            return self.getToken(grammarYaplParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(grammarYaplParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
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
                localctx = grammarYaplParser.MethodContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(grammarYaplParser.OBJECT_ID)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 35
                    self.match(grammarYaplParser.LPAREN)
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==19:
                        self.state = 36
                        self.formal()
                        self.state = 41
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==35:
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
                localctx = grammarYaplParser.AttributeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
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
                if _la==52:
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


    class AndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
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
        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.ASSIGN)
            else:
                return self.getToken(grammarYaplParser.ASSIGN, i)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarYaplParser.COMMA)
            else:
                return self.getToken(grammarYaplParser.COMMA, i)

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


    class OrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammarYaplParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarYaplParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarYaplParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
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
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = grammarYaplParser.Static_dispatchContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 69
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self.match(grammarYaplParser.LPAREN)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4536164926600) != 0):
                    self.state = 71
                    self.expr(0)
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==35:
                        self.state = 72
                        self.match(grammarYaplParser.COMMA)
                        self.state = 73
                        self.expr(0)
                        self.state = 78
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 81
                self.match(grammarYaplParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = grammarYaplParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.match(grammarYaplParser.IF)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(grammarYaplParser.THEN)
                self.state = 85
                self.expr(0)
                self.state = 86
                self.match(grammarYaplParser.ELSE)
                self.state = 87
                self.expr(0)
                self.state = 88
                self.match(grammarYaplParser.FI)
                pass

            elif la_ == 3:
                localctx = grammarYaplParser.WhileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                self.match(grammarYaplParser.WHILE)
                self.state = 91
                self.expr(0)
                self.state = 92
                self.match(grammarYaplParser.LOOP)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(grammarYaplParser.POOL)
                pass

            elif la_ == 4:
                localctx = grammarYaplParser.BlockContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                self.match(grammarYaplParser.LBRACE)
                self.state = 100 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 97
                    self.expr(0)
                    self.state = 98
                    self.match(grammarYaplParser.SEMICOLON)
                    self.state = 102 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4536164926600) != 0)):
                        break

                self.state = 104
                self.match(grammarYaplParser.RBRACE)
                pass

            elif la_ == 5:
                localctx = grammarYaplParser.LetContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(grammarYaplParser.LET)
                self.state = 107
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 108
                self.match(grammarYaplParser.COLON)
                self.state = 109
                self.match(grammarYaplParser.TYPE_ID)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52:
                    self.state = 110
                    self.match(grammarYaplParser.ASSIGN)
                    self.state = 111
                    self.expr(0)


                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 114
                    self.match(grammarYaplParser.COMMA)
                    self.state = 115
                    _la = self._input.LA(1)
                    if not(_la==18 or _la==19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 116
                    self.match(grammarYaplParser.COLON)
                    self.state = 117
                    self.match(grammarYaplParser.TYPE_ID)
                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 118
                        self.match(grammarYaplParser.ASSIGN)
                        self.state = 119
                        self.expr(0)


                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 127
                self.match(grammarYaplParser.IN)
                self.state = 128
                self.expr(20)
                pass

            elif la_ == 6:
                localctx = grammarYaplParser.NewContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 129
                self.match(grammarYaplParser.NEW)
                self.state = 130
                self.match(grammarYaplParser.TYPE_ID)
                pass

            elif la_ == 7:
                localctx = grammarYaplParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(grammarYaplParser.NEG)
                self.state = 132
                self.expr(18)
                pass

            elif la_ == 8:
                localctx = grammarYaplParser.IsvoidContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(grammarYaplParser.ISVOID)
                self.state = 134
                self.expr(17)
                pass

            elif la_ == 9:
                localctx = grammarYaplParser.MinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(grammarYaplParser.MINUS)
                self.state = 136
                self.expr(14)
                pass

            elif la_ == 10:
                localctx = grammarYaplParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(grammarYaplParser.NOT)
                self.state = 138
                self.expr(9)
                pass

            elif la_ == 11:
                localctx = grammarYaplParser.AssignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 139
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 140
                self.match(grammarYaplParser.ASSIGN)
                self.state = 141
                self.expr(8)
                pass

            elif la_ == 12:
                localctx = grammarYaplParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.match(grammarYaplParser.LPAREN)
                self.state = 143
                self.expr(0)
                self.state = 144
                self.match(grammarYaplParser.RPAREN)
                pass

            elif la_ == 13:
                localctx = grammarYaplParser.Object_idContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(grammarYaplParser.OBJECT_ID)
                pass

            elif la_ == 14:
                localctx = grammarYaplParser.IntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.match(grammarYaplParser.INTEGER)
                pass

            elif la_ == 15:
                localctx = grammarYaplParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(grammarYaplParser.STRING)
                pass

            elif la_ == 16:
                localctx = grammarYaplParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.match(grammarYaplParser.BOOL)
                pass

            elif la_ == 17:
                localctx = grammarYaplParser.Type_idContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(grammarYaplParser.TYPE_ID)
                pass

            elif la_ == 18:
                localctx = grammarYaplParser.SelfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(grammarYaplParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 191
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = grammarYaplParser.MulDivContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 154
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 155
                        _la = self._input.LA(1)
                        if not(_la==39 or _la==40):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 156
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = grammarYaplParser.AddSubContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 157
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 158
                        _la = self._input.LA(1)
                        if not(_la==41 or _la==42):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 159
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = grammarYaplParser.ComparisonContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 160
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 161
                        _la = self._input.LA(1)
                        if not(_la==43 or _la==44):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 162
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = grammarYaplParser.AndContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 163
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 164
                        self.match(grammarYaplParser.T__0)
                        self.state = 165
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = grammarYaplParser.OrContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 166
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 167
                        self.match(grammarYaplParser.T__1)
                        self.state = 168
                        self.expr(12)
                        pass

                    elif la_ == 6:
                        localctx = grammarYaplParser.EqContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 169
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 170
                        self.match(grammarYaplParser.EQ)
                        self.state = 171
                        self.expr(11)
                        pass

                    elif la_ == 7:
                        localctx = grammarYaplParser.DispatchContext(self, grammarYaplParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 172
                        if not self.precpred(self._ctx, 25):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 25)")
                        self.state = 175
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==38:
                            self.state = 173
                            self.match(grammarYaplParser.AT)
                            self.state = 174
                            self.match(grammarYaplParser.TYPE_ID)


                        self.state = 177
                        self.match(grammarYaplParser.DOT)
                        self.state = 178
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 179
                        self.match(grammarYaplParser.LPAREN)
                        self.state = 188
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4536164926600) != 0):
                            self.state = 180
                            self.expr(0)
                            self.state = 185
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==35:
                                self.state = 181
                                self.match(grammarYaplParser.COMMA)
                                self.state = 182
                                self.expr(0)
                                self.state = 187
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 190
                        self.match(grammarYaplParser.RPAREN)
                        pass

             
                self.state = 195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 25)
         




