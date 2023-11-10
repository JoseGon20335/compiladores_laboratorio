# Generated from antlr_build/grammarYapl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .grammarYaplParser import grammarYaplParser
else:
    from grammarYaplParser import grammarYaplParser

# This class defines a complete listener for a parse tree produced by grammarYaplParser.
class grammarYaplListener(ParseTreeListener):

    # Enter a parse tree produced by grammarYaplParser#program.
    def enterProgram(self, ctx:grammarYaplParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#program.
    def exitProgram(self, ctx:grammarYaplParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#class_def.
    def enterClass_def(self, ctx:grammarYaplParser.Class_defContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#class_def.
    def exitClass_def(self, ctx:grammarYaplParser.Class_defContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#method.
    def enterMethod(self, ctx:grammarYaplParser.MethodContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#method.
    def exitMethod(self, ctx:grammarYaplParser.MethodContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#attribute.
    def enterAttribute(self, ctx:grammarYaplParser.AttributeContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#attribute.
    def exitAttribute(self, ctx:grammarYaplParser.AttributeContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#formal.
    def enterFormal(self, ctx:grammarYaplParser.FormalContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#formal.
    def exitFormal(self, ctx:grammarYaplParser.FormalContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#new.
    def enterNew(self, ctx:grammarYaplParser.NewContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#new.
    def exitNew(self, ctx:grammarYaplParser.NewContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#minus.
    def enterMinus(self, ctx:grammarYaplParser.MinusContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#minus.
    def exitMinus(self, ctx:grammarYaplParser.MinusContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#comparison.
    def enterComparison(self, ctx:grammarYaplParser.ComparisonContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#comparison.
    def exitComparison(self, ctx:grammarYaplParser.ComparisonContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#or.
    def enterOr(self, ctx:grammarYaplParser.OrContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#or.
    def exitOr(self, ctx:grammarYaplParser.OrContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#dispatch.
    def enterDispatch(self, ctx:grammarYaplParser.DispatchContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#dispatch.
    def exitDispatch(self, ctx:grammarYaplParser.DispatchContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#string.
    def enterString(self, ctx:grammarYaplParser.StringContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#string.
    def exitString(self, ctx:grammarYaplParser.StringContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#bool.
    def enterBool(self, ctx:grammarYaplParser.BoolContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#bool.
    def exitBool(self, ctx:grammarYaplParser.BoolContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#isvoid.
    def enterIsvoid(self, ctx:grammarYaplParser.IsvoidContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#isvoid.
    def exitIsvoid(self, ctx:grammarYaplParser.IsvoidContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#type_id.
    def enterType_id(self, ctx:grammarYaplParser.Type_idContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#type_id.
    def exitType_id(self, ctx:grammarYaplParser.Type_idContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#addSub.
    def enterAddSub(self, ctx:grammarYaplParser.AddSubContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#addSub.
    def exitAddSub(self, ctx:grammarYaplParser.AddSubContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#integer.
    def enterInteger(self, ctx:grammarYaplParser.IntegerContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#integer.
    def exitInteger(self, ctx:grammarYaplParser.IntegerContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#static_dispatch.
    def enterStatic_dispatch(self, ctx:grammarYaplParser.Static_dispatchContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#static_dispatch.
    def exitStatic_dispatch(self, ctx:grammarYaplParser.Static_dispatchContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#while.
    def enterWhile(self, ctx:grammarYaplParser.WhileContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#while.
    def exitWhile(self, ctx:grammarYaplParser.WhileContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#parenthesis.
    def enterParenthesis(self, ctx:grammarYaplParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#parenthesis.
    def exitParenthesis(self, ctx:grammarYaplParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#object_id.
    def enterObject_id(self, ctx:grammarYaplParser.Object_idContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#object_id.
    def exitObject_id(self, ctx:grammarYaplParser.Object_idContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#mulDiv.
    def enterMulDiv(self, ctx:grammarYaplParser.MulDivContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#mulDiv.
    def exitMulDiv(self, ctx:grammarYaplParser.MulDivContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#neg.
    def enterNeg(self, ctx:grammarYaplParser.NegContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#neg.
    def exitNeg(self, ctx:grammarYaplParser.NegContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#not.
    def enterNot(self, ctx:grammarYaplParser.NotContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#not.
    def exitNot(self, ctx:grammarYaplParser.NotContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#and.
    def enterAnd(self, ctx:grammarYaplParser.AndContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#and.
    def exitAnd(self, ctx:grammarYaplParser.AndContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#self.
    def enterSelf(self, ctx:grammarYaplParser.SelfContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#self.
    def exitSelf(self, ctx:grammarYaplParser.SelfContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#block.
    def enterBlock(self, ctx:grammarYaplParser.BlockContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#block.
    def exitBlock(self, ctx:grammarYaplParser.BlockContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#let.
    def enterLet(self, ctx:grammarYaplParser.LetContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#let.
    def exitLet(self, ctx:grammarYaplParser.LetContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#if.
    def enterIf(self, ctx:grammarYaplParser.IfContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#if.
    def exitIf(self, ctx:grammarYaplParser.IfContext):
        pass


    # Enter a parse tree produced by grammarYaplParser#assign.
    def enterAssign(self, ctx:grammarYaplParser.AssignContext):
        pass

    # Exit a parse tree produced by grammarYaplParser#assign.
    def exitAssign(self, ctx:grammarYaplParser.AssignContext):
        pass



del grammarYaplParser