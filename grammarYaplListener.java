// Generated from antlr_build/grammarYapl.g4 by ANTLR 4.13.0
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link grammarYaplParser}.
 */
public interface grammarYaplListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link grammarYaplParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(grammarYaplParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarYaplParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(grammarYaplParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarYaplParser#class_def}.
	 * @param ctx the parse tree
	 */
	void enterClass_def(grammarYaplParser.Class_defContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarYaplParser#class_def}.
	 * @param ctx the parse tree
	 */
	void exitClass_def(grammarYaplParser.Class_defContext ctx);
	/**
	 * Enter a parse tree produced by the {@code method}
	 * labeled alternative in {@link grammarYaplParser#feature}.
	 * @param ctx the parse tree
	 */
	void enterMethod(grammarYaplParser.MethodContext ctx);
	/**
	 * Exit a parse tree produced by the {@code method}
	 * labeled alternative in {@link grammarYaplParser#feature}.
	 * @param ctx the parse tree
	 */
	void exitMethod(grammarYaplParser.MethodContext ctx);
	/**
	 * Enter a parse tree produced by the {@code attribute}
	 * labeled alternative in {@link grammarYaplParser#feature}.
	 * @param ctx the parse tree
	 */
	void enterAttribute(grammarYaplParser.AttributeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code attribute}
	 * labeled alternative in {@link grammarYaplParser#feature}.
	 * @param ctx the parse tree
	 */
	void exitAttribute(grammarYaplParser.AttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link grammarYaplParser#formal}.
	 * @param ctx the parse tree
	 */
	void enterFormal(grammarYaplParser.FormalContext ctx);
	/**
	 * Exit a parse tree produced by {@link grammarYaplParser#formal}.
	 * @param ctx the parse tree
	 */
	void exitFormal(grammarYaplParser.FormalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code new}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNew(grammarYaplParser.NewContext ctx);
	/**
	 * Exit a parse tree produced by the {@code new}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNew(grammarYaplParser.NewContext ctx);
	/**
	 * Enter a parse tree produced by the {@code minus}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMinus(grammarYaplParser.MinusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code minus}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMinus(grammarYaplParser.MinusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comparison}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterComparison(grammarYaplParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comparison}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitComparison(grammarYaplParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by the {@code or}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOr(grammarYaplParser.OrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code or}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOr(grammarYaplParser.OrContext ctx);
	/**
	 * Enter a parse tree produced by the {@code dispatch}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDispatch(grammarYaplParser.DispatchContext ctx);
	/**
	 * Exit a parse tree produced by the {@code dispatch}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDispatch(grammarYaplParser.DispatchContext ctx);
	/**
	 * Enter a parse tree produced by the {@code string}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterString(grammarYaplParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code string}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitString(grammarYaplParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code bool}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBool(grammarYaplParser.BoolContext ctx);
	/**
	 * Exit a parse tree produced by the {@code bool}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBool(grammarYaplParser.BoolContext ctx);
	/**
	 * Enter a parse tree produced by the {@code isvoid}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIsvoid(grammarYaplParser.IsvoidContext ctx);
	/**
	 * Exit a parse tree produced by the {@code isvoid}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIsvoid(grammarYaplParser.IsvoidContext ctx);
	/**
	 * Enter a parse tree produced by the {@code type_id}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterType_id(grammarYaplParser.Type_idContext ctx);
	/**
	 * Exit a parse tree produced by the {@code type_id}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitType_id(grammarYaplParser.Type_idContext ctx);
	/**
	 * Enter a parse tree produced by the {@code addSub}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(grammarYaplParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code addSub}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(grammarYaplParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code integer}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterInteger(grammarYaplParser.IntegerContext ctx);
	/**
	 * Exit a parse tree produced by the {@code integer}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitInteger(grammarYaplParser.IntegerContext ctx);
	/**
	 * Enter a parse tree produced by the {@code static_dispatch}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterStatic_dispatch(grammarYaplParser.Static_dispatchContext ctx);
	/**
	 * Exit a parse tree produced by the {@code static_dispatch}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitStatic_dispatch(grammarYaplParser.Static_dispatchContext ctx);
	/**
	 * Enter a parse tree produced by the {@code while}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterWhile(grammarYaplParser.WhileContext ctx);
	/**
	 * Exit a parse tree produced by the {@code while}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitWhile(grammarYaplParser.WhileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenthesis}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParenthesis(grammarYaplParser.ParenthesisContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenthesis}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParenthesis(grammarYaplParser.ParenthesisContext ctx);
	/**
	 * Enter a parse tree produced by the {@code object_id}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterObject_id(grammarYaplParser.Object_idContext ctx);
	/**
	 * Exit a parse tree produced by the {@code object_id}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitObject_id(grammarYaplParser.Object_idContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mulDiv}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(grammarYaplParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mulDiv}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(grammarYaplParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code neg}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNeg(grammarYaplParser.NegContext ctx);
	/**
	 * Exit a parse tree produced by the {@code neg}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNeg(grammarYaplParser.NegContext ctx);
	/**
	 * Enter a parse tree produced by the {@code not}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNot(grammarYaplParser.NotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code not}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNot(grammarYaplParser.NotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code and}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAnd(grammarYaplParser.AndContext ctx);
	/**
	 * Exit a parse tree produced by the {@code and}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAnd(grammarYaplParser.AndContext ctx);
	/**
	 * Enter a parse tree produced by the {@code self}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterSelf(grammarYaplParser.SelfContext ctx);
	/**
	 * Exit a parse tree produced by the {@code self}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitSelf(grammarYaplParser.SelfContext ctx);
	/**
	 * Enter a parse tree produced by the {@code block}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBlock(grammarYaplParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by the {@code block}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBlock(grammarYaplParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by the {@code let}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLet(grammarYaplParser.LetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code let}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLet(grammarYaplParser.LetContext ctx);
	/**
	 * Enter a parse tree produced by the {@code if}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIf(grammarYaplParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by the {@code if}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIf(grammarYaplParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assign}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAssign(grammarYaplParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assign}
	 * labeled alternative in {@link grammarYaplParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAssign(grammarYaplParser.AssignContext ctx);
}