# Generated from antlr_build/grammarYapl.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .grammarYaplParser import grammarYaplParser
else:
    from grammarYaplParser import grammarYaplParser

# This class defines a complete generic visitor for a parse tree produced by grammarYaplParser.

class grammarYaplVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammarYaplParser#program.
    def visitProgram(self, ctx:grammarYaplParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#class_def.
    def visitClass_def(self, ctx:grammarYaplParser.Class_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#method.
    def visitMethod(self, ctx:grammarYaplParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#attribute.
    def visitAttribute(self, ctx:grammarYaplParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#formal.
    def visitFormal(self, ctx:grammarYaplParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#minus.
    def visitMinus(self, ctx:grammarYaplParser.MinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#dispatch.
    def visitDispatch(self, ctx:grammarYaplParser.DispatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#string.
    def visitString(self, ctx:grammarYaplParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#bool.
    def visitBool(self, ctx:grammarYaplParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#isvoid.
    def visitIsvoid(self, ctx:grammarYaplParser.IsvoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#integer.
    def visitInteger(self, ctx:grammarYaplParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#while.
    def visitWhile(self, ctx:grammarYaplParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#mulDiv.
    def visitMulDiv(self, ctx:grammarYaplParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#neg.
    def visitNeg(self, ctx:grammarYaplParser.NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#not.
    def visitNot(self, ctx:grammarYaplParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#and.
    def visitAnd(self, ctx:grammarYaplParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#block.
    def visitBlock(self, ctx:grammarYaplParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#let.
    def visitLet(self, ctx:grammarYaplParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#if.
    def visitIf(self, ctx:grammarYaplParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#new.
    def visitNew(self, ctx:grammarYaplParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#comparison.
    def visitComparison(self, ctx:grammarYaplParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#or.
    def visitOr(self, ctx:grammarYaplParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#type_id.
    def visitType_id(self, ctx:grammarYaplParser.Type_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#addSub.
    def visitAddSub(self, ctx:grammarYaplParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#static_dispatch.
    def visitStatic_dispatch(self, ctx:grammarYaplParser.Static_dispatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#eq.
    def visitEq(self, ctx:grammarYaplParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#parenthesis.
    def visitParenthesis(self, ctx:grammarYaplParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#object_id.
    def visitObject_id(self, ctx:grammarYaplParser.Object_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#self.
    def visitSelf(self, ctx:grammarYaplParser.SelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarYaplParser#assign.
    def visitAssign(self, ctx:grammarYaplParser.AssignContext):
        return self.visitChildren(ctx)



del grammarYaplParser