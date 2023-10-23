// Generated from antlr_build/grammarYapl.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class grammarYaplParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, CLASS=4, ELSE=5, FI=6, IF=7, IN=8, INHERITS=9, 
		ISVOID=10, LOOP=11, POOL=12, THEN=13, WHILE=14, NEW=15, NOT=16, LET=17, 
		TYPE_ID=18, OBJECT_ID=19, INTEGER=20, BOOL=21, STRING=22, WHITESPACE=23, 
		NEWLINE=24, COMMENT=25, COMMENT_BLOCK=26, LPAREN=27, RPAREN=28, LBRACE=29, 
		RBRACE=30, LBRACKET=31, RBRACKET=32, COLON=33, SEMICOLON=34, COMMA=35, 
		DOT=36, NEG=37, AT=38, MULT=39, DIV=40, PLUS=41, MINUS=42, LE=43, LT=44, 
		EQ=45, INCR=46, DECR=47, ASSIGN_MULT=48, ASSIGN_DIV=49, ASSIGN_PLUS=50, 
		ASSIGN_MINUS=51, ASSIGN=52;
	public static final int
		RULE_program = 0, RULE_class_def = 1, RULE_feature = 2, RULE_formal = 3, 
		RULE_expr = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "class_def", "feature", "formal", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'&'", "'|'", "'self'", null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "'let'", null, null, null, null, 
			null, null, null, null, null, "'('", "')'", "'{'", "'}'", "'['", "']'", 
			"':'", "';'", "','", "'.'", "'~'", "'@'", "'*'", "'/'", "'+'", "'-'", 
			"'<='", "'<'", "'='", "'++'", "'--'", "'=*'", "'=/'", "'=+'", "'=-'", 
			"'<-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "CLASS", "ELSE", "FI", "IF", "IN", "INHERITS", 
			"ISVOID", "LOOP", "POOL", "THEN", "WHILE", "NEW", "NOT", "LET", "TYPE_ID", 
			"OBJECT_ID", "INTEGER", "BOOL", "STRING", "WHITESPACE", "NEWLINE", "COMMENT", 
			"COMMENT_BLOCK", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
			"RBRACKET", "COLON", "SEMICOLON", "COMMA", "DOT", "NEG", "AT", "MULT", 
			"DIV", "PLUS", "MINUS", "LE", "LT", "EQ", "INCR", "DECR", "ASSIGN_MULT", 
			"ASSIGN_DIV", "ASSIGN_PLUS", "ASSIGN_MINUS", "ASSIGN"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "grammarYapl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public grammarYaplParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public List<Class_defContext> class_def() {
			return getRuleContexts(Class_defContext.class);
		}
		public Class_defContext class_def(int i) {
			return getRuleContext(Class_defContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(grammarYaplParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(grammarYaplParser.SEMICOLON, i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(10);
				class_def();
				setState(11);
				match(SEMICOLON);
				}
				}
				setState(15); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CLASS );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Class_defContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(grammarYaplParser.CLASS, 0); }
		public List<TerminalNode> TYPE_ID() { return getTokens(grammarYaplParser.TYPE_ID); }
		public TerminalNode TYPE_ID(int i) {
			return getToken(grammarYaplParser.TYPE_ID, i);
		}
		public TerminalNode LBRACE() { return getToken(grammarYaplParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(grammarYaplParser.RBRACE, 0); }
		public TerminalNode INHERITS() { return getToken(grammarYaplParser.INHERITS, 0); }
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(grammarYaplParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(grammarYaplParser.SEMICOLON, i);
		}
		public Class_defContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_def; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterClass_def(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitClass_def(this);
		}
	}

	public final Class_defContext class_def() throws RecognitionException {
		Class_defContext _localctx = new Class_defContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_class_def);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17);
			match(CLASS);
			setState(18);
			match(TYPE_ID);
			setState(21);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITS) {
				{
				setState(19);
				match(INHERITS);
				setState(20);
				match(TYPE_ID);
				}
			}

			setState(23);
			match(LBRACE);
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==TYPE_ID || _la==OBJECT_ID) {
				{
				{
				setState(24);
				feature();
				setState(25);
				match(SEMICOLON);
				}
				}
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(32);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FeatureContext extends ParserRuleContext {
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	 
		public FeatureContext() { }
		public void copyFrom(FeatureContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MethodContext extends FeatureContext {
		public TerminalNode OBJECT_ID() { return getToken(grammarYaplParser.OBJECT_ID, 0); }
		public TerminalNode COLON() { return getToken(grammarYaplParser.COLON, 0); }
		public TerminalNode TYPE_ID() { return getToken(grammarYaplParser.TYPE_ID, 0); }
		public TerminalNode LBRACE() { return getToken(grammarYaplParser.LBRACE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(grammarYaplParser.RBRACE, 0); }
		public TerminalNode LPAREN() { return getToken(grammarYaplParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(grammarYaplParser.RPAREN, 0); }
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(grammarYaplParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(grammarYaplParser.COMMA, i);
		}
		public MethodContext(FeatureContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterMethod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitMethod(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AttributeContext extends FeatureContext {
		public TerminalNode COLON() { return getToken(grammarYaplParser.COLON, 0); }
		public List<TerminalNode> TYPE_ID() { return getTokens(grammarYaplParser.TYPE_ID); }
		public TerminalNode TYPE_ID(int i) {
			return getToken(grammarYaplParser.TYPE_ID, i);
		}
		public TerminalNode OBJECT_ID() { return getToken(grammarYaplParser.OBJECT_ID, 0); }
		public TerminalNode ASSIGN() { return getToken(grammarYaplParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AttributeContext(FeatureContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterAttribute(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitAttribute(this);
		}
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_feature);
		int _la;
		try {
			setState(62);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				_localctx = new MethodContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(34);
				match(OBJECT_ID);
				setState(47);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LPAREN) {
					{
					setState(35);
					match(LPAREN);
					setState(44);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==OBJECT_ID) {
						{
						setState(36);
						formal();
						setState(41);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==COMMA) {
							{
							{
							setState(37);
							match(COMMA);
							setState(38);
							formal();
							}
							}
							setState(43);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						}
					}

					setState(46);
					match(RPAREN);
					}
				}

				setState(49);
				match(COLON);
				setState(50);
				match(TYPE_ID);
				setState(51);
				match(LBRACE);
				setState(52);
				expr(0);
				setState(53);
				match(RBRACE);
				}
				break;
			case 2:
				_localctx = new AttributeContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				_la = _input.LA(1);
				if ( !(_la==TYPE_ID || _la==OBJECT_ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(56);
				match(COLON);
				setState(57);
				match(TYPE_ID);
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(58);
					match(ASSIGN);
					setState(59);
					expr(0);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FormalContext extends ParserRuleContext {
		public TerminalNode OBJECT_ID() { return getToken(grammarYaplParser.OBJECT_ID, 0); }
		public TerminalNode COLON() { return getToken(grammarYaplParser.COLON, 0); }
		public TerminalNode TYPE_ID() { return getToken(grammarYaplParser.TYPE_ID, 0); }
		public FormalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterFormal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitFormal(this);
		}
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_formal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(OBJECT_ID);
			setState(65);
			match(COLON);
			setState(66);
			match(TYPE_ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MinusContext extends ExprContext {
		public TerminalNode MINUS() { return getToken(grammarYaplParser.MINUS, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public MinusContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterMinus(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitMinus(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DispatchContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode DOT() { return getToken(grammarYaplParser.DOT, 0); }
		public TerminalNode LPAREN() { return getToken(grammarYaplParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(grammarYaplParser.RPAREN, 0); }
		public List<TerminalNode> TYPE_ID() { return getTokens(grammarYaplParser.TYPE_ID); }
		public TerminalNode TYPE_ID(int i) {
			return getToken(grammarYaplParser.TYPE_ID, i);
		}
		public TerminalNode OBJECT_ID() { return getToken(grammarYaplParser.OBJECT_ID, 0); }
		public TerminalNode AT() { return getToken(grammarYaplParser.AT, 0); }
		public List<TerminalNode> COMMA() { return getTokens(grammarYaplParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(grammarYaplParser.COMMA, i);
		}
		public DispatchContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterDispatch(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitDispatch(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringContext extends ExprContext {
		public TerminalNode STRING() { return getToken(grammarYaplParser.STRING, 0); }
		public StringContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitString(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BoolContext extends ExprContext {
		public TerminalNode BOOL() { return getToken(grammarYaplParser.BOOL, 0); }
		public BoolContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterBool(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitBool(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IsvoidContext extends ExprContext {
		public TerminalNode ISVOID() { return getToken(grammarYaplParser.ISVOID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public IsvoidContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterIsvoid(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitIsvoid(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntegerContext extends ExprContext {
		public TerminalNode INTEGER() { return getToken(grammarYaplParser.INTEGER, 0); }
		public IntegerContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterInteger(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitInteger(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WhileContext extends ExprContext {
		public TerminalNode WHILE() { return getToken(grammarYaplParser.WHILE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LOOP() { return getToken(grammarYaplParser.LOOP, 0); }
		public TerminalNode POOL() { return getToken(grammarYaplParser.POOL, 0); }
		public WhileContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterWhile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitWhile(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulDivContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MULT() { return getToken(grammarYaplParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(grammarYaplParser.DIV, 0); }
		public MulDivContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterMulDiv(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitMulDiv(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NegContext extends ExprContext {
		public TerminalNode NEG() { return getToken(grammarYaplParser.NEG, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NegContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterNeg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitNeg(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NotContext extends ExprContext {
		public TerminalNode NOT() { return getToken(grammarYaplParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NotContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterNot(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitNot(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AndContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public AndContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterAnd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitAnd(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ExprContext {
		public TerminalNode LBRACE() { return getToken(grammarYaplParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(grammarYaplParser.RBRACE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(grammarYaplParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(grammarYaplParser.SEMICOLON, i);
		}
		public BlockContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitBlock(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LetContext extends ExprContext {
		public TerminalNode LET() { return getToken(grammarYaplParser.LET, 0); }
		public List<TerminalNode> COLON() { return getTokens(grammarYaplParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(grammarYaplParser.COLON, i);
		}
		public List<TerminalNode> TYPE_ID() { return getTokens(grammarYaplParser.TYPE_ID); }
		public TerminalNode TYPE_ID(int i) {
			return getToken(grammarYaplParser.TYPE_ID, i);
		}
		public TerminalNode IN() { return getToken(grammarYaplParser.IN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> OBJECT_ID() { return getTokens(grammarYaplParser.OBJECT_ID); }
		public TerminalNode OBJECT_ID(int i) {
			return getToken(grammarYaplParser.OBJECT_ID, i);
		}
		public List<TerminalNode> ASSIGN() { return getTokens(grammarYaplParser.ASSIGN); }
		public TerminalNode ASSIGN(int i) {
			return getToken(grammarYaplParser.ASSIGN, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(grammarYaplParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(grammarYaplParser.COMMA, i);
		}
		public LetContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterLet(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitLet(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfContext extends ExprContext {
		public TerminalNode IF() { return getToken(grammarYaplParser.IF, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode THEN() { return getToken(grammarYaplParser.THEN, 0); }
		public TerminalNode ELSE() { return getToken(grammarYaplParser.ELSE, 0); }
		public TerminalNode FI() { return getToken(grammarYaplParser.FI, 0); }
		public IfContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterIf(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitIf(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NewContext extends ExprContext {
		public TerminalNode NEW() { return getToken(grammarYaplParser.NEW, 0); }
		public TerminalNode TYPE_ID() { return getToken(grammarYaplParser.TYPE_ID, 0); }
		public NewContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterNew(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitNew(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LE() { return getToken(grammarYaplParser.LE, 0); }
		public TerminalNode LT() { return getToken(grammarYaplParser.LT, 0); }
		public ComparisonContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterComparison(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitComparison(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OrContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public OrContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterOr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitOr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Type_idContext extends ExprContext {
		public TerminalNode TYPE_ID() { return getToken(grammarYaplParser.TYPE_ID, 0); }
		public Type_idContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterType_id(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitType_id(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddSubContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(grammarYaplParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(grammarYaplParser.MINUS, 0); }
		public AddSubContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterAddSub(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitAddSub(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Static_dispatchContext extends ExprContext {
		public TerminalNode LPAREN() { return getToken(grammarYaplParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(grammarYaplParser.RPAREN, 0); }
		public TerminalNode TYPE_ID() { return getToken(grammarYaplParser.TYPE_ID, 0); }
		public TerminalNode OBJECT_ID() { return getToken(grammarYaplParser.OBJECT_ID, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(grammarYaplParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(grammarYaplParser.COMMA, i);
		}
		public Static_dispatchContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterStatic_dispatch(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitStatic_dispatch(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class EqContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode EQ() { return getToken(grammarYaplParser.EQ, 0); }
		public EqContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterEq(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitEq(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenthesisContext extends ExprContext {
		public TerminalNode LPAREN() { return getToken(grammarYaplParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(grammarYaplParser.RPAREN, 0); }
		public ParenthesisContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterParenthesis(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitParenthesis(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Object_idContext extends ExprContext {
		public TerminalNode OBJECT_ID() { return getToken(grammarYaplParser.OBJECT_ID, 0); }
		public Object_idContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterObject_id(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitObject_id(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SelfContext extends ExprContext {
		public SelfContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterSelf(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitSelf(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ExprContext {
		public TerminalNode ASSIGN() { return getToken(grammarYaplParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode TYPE_ID() { return getToken(grammarYaplParser.TYPE_ID, 0); }
		public TerminalNode OBJECT_ID() { return getToken(grammarYaplParser.OBJECT_ID, 0); }
		public AssignContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).enterAssign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarYaplListener ) ((grammarYaplListener)listener).exitAssign(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				_localctx = new Static_dispatchContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(69);
				_la = _input.LA(1);
				if ( !(_la==TYPE_ID || _la==OBJECT_ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(70);
				match(LPAREN);
				setState(79);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4536164926600L) != 0)) {
					{
					setState(71);
					expr(0);
					setState(76);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(72);
						match(COMMA);
						setState(73);
						expr(0);
						}
						}
						setState(78);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(81);
				match(RPAREN);
				}
				break;
			case 2:
				{
				_localctx = new IfContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(82);
				match(IF);
				setState(83);
				expr(0);
				setState(84);
				match(THEN);
				setState(85);
				expr(0);
				setState(86);
				match(ELSE);
				setState(87);
				expr(0);
				setState(88);
				match(FI);
				}
				break;
			case 3:
				{
				_localctx = new WhileContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(90);
				match(WHILE);
				setState(91);
				expr(0);
				setState(92);
				match(LOOP);
				setState(93);
				expr(0);
				setState(94);
				match(POOL);
				}
				break;
			case 4:
				{
				_localctx = new BlockContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(96);
				match(LBRACE);
				setState(100); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(97);
					expr(0);
					setState(98);
					match(SEMICOLON);
					}
					}
					setState(102); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 4536164926600L) != 0) );
				setState(104);
				match(RBRACE);
				}
				break;
			case 5:
				{
				_localctx = new LetContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(106);
				match(LET);
				setState(107);
				_la = _input.LA(1);
				if ( !(_la==TYPE_ID || _la==OBJECT_ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(108);
				match(COLON);
				setState(109);
				match(TYPE_ID);
				setState(112);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(110);
					match(ASSIGN);
					setState(111);
					expr(0);
					}
				}

				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(114);
					match(COMMA);
					setState(115);
					_la = _input.LA(1);
					if ( !(_la==TYPE_ID || _la==OBJECT_ID) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(116);
					match(COLON);
					setState(117);
					match(TYPE_ID);
					setState(120);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==ASSIGN) {
						{
						setState(118);
						match(ASSIGN);
						setState(119);
						expr(0);
						}
					}

					}
					}
					setState(126);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(127);
				match(IN);
				setState(128);
				expr(20);
				}
				break;
			case 6:
				{
				_localctx = new NewContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(129);
				match(NEW);
				setState(130);
				match(TYPE_ID);
				}
				break;
			case 7:
				{
				_localctx = new NegContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(131);
				match(NEG);
				setState(132);
				expr(18);
				}
				break;
			case 8:
				{
				_localctx = new IsvoidContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(133);
				match(ISVOID);
				setState(134);
				expr(17);
				}
				break;
			case 9:
				{
				_localctx = new MinusContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(135);
				match(MINUS);
				setState(136);
				expr(14);
				}
				break;
			case 10:
				{
				_localctx = new NotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(137);
				match(NOT);
				setState(138);
				expr(9);
				}
				break;
			case 11:
				{
				_localctx = new AssignContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(139);
				_la = _input.LA(1);
				if ( !(_la==TYPE_ID || _la==OBJECT_ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(140);
				match(ASSIGN);
				setState(141);
				expr(8);
				}
				break;
			case 12:
				{
				_localctx = new ParenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(142);
				match(LPAREN);
				setState(143);
				expr(0);
				setState(144);
				match(RPAREN);
				}
				break;
			case 13:
				{
				_localctx = new Object_idContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(146);
				match(OBJECT_ID);
				}
				break;
			case 14:
				{
				_localctx = new IntegerContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(147);
				match(INTEGER);
				}
				break;
			case 15:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(148);
				match(STRING);
				}
				break;
			case 16:
				{
				_localctx = new BoolContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(149);
				match(BOOL);
				}
				break;
			case 17:
				{
				_localctx = new Type_idContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(150);
				match(TYPE_ID);
				}
				break;
			case 18:
				{
				_localctx = new SelfContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(151);
				match(T__2);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(193);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(191);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(154);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(155);
						_la = _input.LA(1);
						if ( !(_la==MULT || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(156);
						expr(17);
						}
						break;
					case 2:
						{
						_localctx = new AddSubContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(157);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(158);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(159);
						expr(16);
						}
						break;
					case 3:
						{
						_localctx = new ComparisonContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(160);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(161);
						_la = _input.LA(1);
						if ( !(_la==LE || _la==LT) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(162);
						expr(14);
						}
						break;
					case 4:
						{
						_localctx = new AndContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(163);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(164);
						match(T__0);
						setState(165);
						expr(13);
						}
						break;
					case 5:
						{
						_localctx = new OrContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(166);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(167);
						match(T__1);
						setState(168);
						expr(12);
						}
						break;
					case 6:
						{
						_localctx = new EqContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(169);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(170);
						match(EQ);
						setState(171);
						expr(11);
						}
						break;
					case 7:
						{
						_localctx = new DispatchContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(172);
						if (!(precpred(_ctx, 25))) throw new FailedPredicateException(this, "precpred(_ctx, 25)");
						setState(175);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==AT) {
							{
							setState(173);
							match(AT);
							setState(174);
							match(TYPE_ID);
							}
						}

						setState(177);
						match(DOT);
						setState(178);
						_la = _input.LA(1);
						if ( !(_la==TYPE_ID || _la==OBJECT_ID) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(179);
						match(LPAREN);
						setState(188);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4536164926600L) != 0)) {
							{
							setState(180);
							expr(0);
							setState(185);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==COMMA) {
								{
								{
								setState(181);
								match(COMMA);
								setState(182);
								expr(0);
								}
								}
								setState(187);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(190);
						match(RPAREN);
						}
						break;
					}
					} 
				}
				setState(195);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 16);
		case 1:
			return precpred(_ctx, 15);
		case 2:
			return precpred(_ctx, 13);
		case 3:
			return precpred(_ctx, 12);
		case 4:
			return precpred(_ctx, 11);
		case 5:
			return precpred(_ctx, 10);
		case 6:
			return precpred(_ctx, 25);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00014\u00c5\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u000e\b\u0000\u000b\u0000\f"+
		"\u0000\u000f\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"\u0016\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001"+
		"\u001c\b\u0001\n\u0001\f\u0001\u001f\t\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002(\b"+
		"\u0002\n\u0002\f\u0002+\t\u0002\u0003\u0002-\b\u0002\u0001\u0002\u0003"+
		"\u00020\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u0002=\b\u0002\u0003\u0002?\b\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0005\u0004K\b\u0004\n\u0004\f\u0004N\t\u0004"+
		"\u0003\u0004P\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0004\u0004e\b\u0004\u000b\u0004"+
		"\f\u0004f\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004q\b\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004"+
		"y\b\u0004\u0005\u0004{\b\u0004\n\u0004\f\u0004~\t\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004\u0099\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u00b0"+
		"\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0005\u0004\u00b8\b\u0004\n\u0004\f\u0004\u00bb\t\u0004\u0003\u0004"+
		"\u00bd\b\u0004\u0001\u0004\u0005\u0004\u00c0\b\u0004\n\u0004\f\u0004\u00c3"+
		"\t\u0004\u0001\u0004\u0000\u0001\b\u0005\u0000\u0002\u0004\u0006\b\u0000"+
		"\u0004\u0001\u0000\u0012\u0013\u0001\u0000\'(\u0001\u0000)*\u0001\u0000"+
		"+,\u00e8\u0000\r\u0001\u0000\u0000\u0000\u0002\u0011\u0001\u0000\u0000"+
		"\u0000\u0004>\u0001\u0000\u0000\u0000\u0006@\u0001\u0000\u0000\u0000\b"+
		"\u0098\u0001\u0000\u0000\u0000\n\u000b\u0003\u0002\u0001\u0000\u000b\f"+
		"\u0005\"\u0000\u0000\f\u000e\u0001\u0000\u0000\u0000\r\n\u0001\u0000\u0000"+
		"\u0000\u000e\u000f\u0001\u0000\u0000\u0000\u000f\r\u0001\u0000\u0000\u0000"+
		"\u000f\u0010\u0001\u0000\u0000\u0000\u0010\u0001\u0001\u0000\u0000\u0000"+
		"\u0011\u0012\u0005\u0004\u0000\u0000\u0012\u0015\u0005\u0012\u0000\u0000"+
		"\u0013\u0014\u0005\t\u0000\u0000\u0014\u0016\u0005\u0012\u0000\u0000\u0015"+
		"\u0013\u0001\u0000\u0000\u0000\u0015\u0016\u0001\u0000\u0000\u0000\u0016"+
		"\u0017\u0001\u0000\u0000\u0000\u0017\u001d\u0005\u001d\u0000\u0000\u0018"+
		"\u0019\u0003\u0004\u0002\u0000\u0019\u001a\u0005\"\u0000\u0000\u001a\u001c"+
		"\u0001\u0000\u0000\u0000\u001b\u0018\u0001\u0000\u0000\u0000\u001c\u001f"+
		"\u0001\u0000\u0000\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d\u001e"+
		"\u0001\u0000\u0000\u0000\u001e \u0001\u0000\u0000\u0000\u001f\u001d\u0001"+
		"\u0000\u0000\u0000 !\u0005\u001e\u0000\u0000!\u0003\u0001\u0000\u0000"+
		"\u0000\"/\u0005\u0013\u0000\u0000#,\u0005\u001b\u0000\u0000$)\u0003\u0006"+
		"\u0003\u0000%&\u0005#\u0000\u0000&(\u0003\u0006\u0003\u0000\'%\u0001\u0000"+
		"\u0000\u0000(+\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000)*\u0001"+
		"\u0000\u0000\u0000*-\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000"+
		",$\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000"+
		"\u0000.0\u0005\u001c\u0000\u0000/#\u0001\u0000\u0000\u0000/0\u0001\u0000"+
		"\u0000\u000001\u0001\u0000\u0000\u000012\u0005!\u0000\u000023\u0005\u0012"+
		"\u0000\u000034\u0005\u001d\u0000\u000045\u0003\b\u0004\u000056\u0005\u001e"+
		"\u0000\u00006?\u0001\u0000\u0000\u000078\u0007\u0000\u0000\u000089\u0005"+
		"!\u0000\u00009<\u0005\u0012\u0000\u0000:;\u00054\u0000\u0000;=\u0003\b"+
		"\u0004\u0000<:\u0001\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=?\u0001"+
		"\u0000\u0000\u0000>\"\u0001\u0000\u0000\u0000>7\u0001\u0000\u0000\u0000"+
		"?\u0005\u0001\u0000\u0000\u0000@A\u0005\u0013\u0000\u0000AB\u0005!\u0000"+
		"\u0000BC\u0005\u0012\u0000\u0000C\u0007\u0001\u0000\u0000\u0000DE\u0006"+
		"\u0004\uffff\uffff\u0000EF\u0007\u0000\u0000\u0000FO\u0005\u001b\u0000"+
		"\u0000GL\u0003\b\u0004\u0000HI\u0005#\u0000\u0000IK\u0003\b\u0004\u0000"+
		"JH\u0001\u0000\u0000\u0000KN\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000"+
		"\u0000LM\u0001\u0000\u0000\u0000MP\u0001\u0000\u0000\u0000NL\u0001\u0000"+
		"\u0000\u0000OG\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000PQ\u0001"+
		"\u0000\u0000\u0000Q\u0099\u0005\u001c\u0000\u0000RS\u0005\u0007\u0000"+
		"\u0000ST\u0003\b\u0004\u0000TU\u0005\r\u0000\u0000UV\u0003\b\u0004\u0000"+
		"VW\u0005\u0005\u0000\u0000WX\u0003\b\u0004\u0000XY\u0005\u0006\u0000\u0000"+
		"Y\u0099\u0001\u0000\u0000\u0000Z[\u0005\u000e\u0000\u0000[\\\u0003\b\u0004"+
		"\u0000\\]\u0005\u000b\u0000\u0000]^\u0003\b\u0004\u0000^_\u0005\f\u0000"+
		"\u0000_\u0099\u0001\u0000\u0000\u0000`d\u0005\u001d\u0000\u0000ab\u0003"+
		"\b\u0004\u0000bc\u0005\"\u0000\u0000ce\u0001\u0000\u0000\u0000da\u0001"+
		"\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000fd\u0001\u0000\u0000\u0000"+
		"fg\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000hi\u0005\u001e\u0000"+
		"\u0000i\u0099\u0001\u0000\u0000\u0000jk\u0005\u0011\u0000\u0000kl\u0007"+
		"\u0000\u0000\u0000lm\u0005!\u0000\u0000mp\u0005\u0012\u0000\u0000no\u0005"+
		"4\u0000\u0000oq\u0003\b\u0004\u0000pn\u0001\u0000\u0000\u0000pq\u0001"+
		"\u0000\u0000\u0000q|\u0001\u0000\u0000\u0000rs\u0005#\u0000\u0000st\u0007"+
		"\u0000\u0000\u0000tu\u0005!\u0000\u0000ux\u0005\u0012\u0000\u0000vw\u0005"+
		"4\u0000\u0000wy\u0003\b\u0004\u0000xv\u0001\u0000\u0000\u0000xy\u0001"+
		"\u0000\u0000\u0000y{\u0001\u0000\u0000\u0000zr\u0001\u0000\u0000\u0000"+
		"{~\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000"+
		"\u0000}\u007f\u0001\u0000\u0000\u0000~|\u0001\u0000\u0000\u0000\u007f"+
		"\u0080\u0005\b\u0000\u0000\u0080\u0099\u0003\b\u0004\u0014\u0081\u0082"+
		"\u0005\u000f\u0000\u0000\u0082\u0099\u0005\u0012\u0000\u0000\u0083\u0084"+
		"\u0005%\u0000\u0000\u0084\u0099\u0003\b\u0004\u0012\u0085\u0086\u0005"+
		"\n\u0000\u0000\u0086\u0099\u0003\b\u0004\u0011\u0087\u0088\u0005*\u0000"+
		"\u0000\u0088\u0099\u0003\b\u0004\u000e\u0089\u008a\u0005\u0010\u0000\u0000"+
		"\u008a\u0099\u0003\b\u0004\t\u008b\u008c\u0007\u0000\u0000\u0000\u008c"+
		"\u008d\u00054\u0000\u0000\u008d\u0099\u0003\b\u0004\b\u008e\u008f\u0005"+
		"\u001b\u0000\u0000\u008f\u0090\u0003\b\u0004\u0000\u0090\u0091\u0005\u001c"+
		"\u0000\u0000\u0091\u0099\u0001\u0000\u0000\u0000\u0092\u0099\u0005\u0013"+
		"\u0000\u0000\u0093\u0099\u0005\u0014\u0000\u0000\u0094\u0099\u0005\u0016"+
		"\u0000\u0000\u0095\u0099\u0005\u0015\u0000\u0000\u0096\u0099\u0005\u0012"+
		"\u0000\u0000\u0097\u0099\u0005\u0003\u0000\u0000\u0098D\u0001\u0000\u0000"+
		"\u0000\u0098R\u0001\u0000\u0000\u0000\u0098Z\u0001\u0000\u0000\u0000\u0098"+
		"`\u0001\u0000\u0000\u0000\u0098j\u0001\u0000\u0000\u0000\u0098\u0081\u0001"+
		"\u0000\u0000\u0000\u0098\u0083\u0001\u0000\u0000\u0000\u0098\u0085\u0001"+
		"\u0000\u0000\u0000\u0098\u0087\u0001\u0000\u0000\u0000\u0098\u0089\u0001"+
		"\u0000\u0000\u0000\u0098\u008b\u0001\u0000\u0000\u0000\u0098\u008e\u0001"+
		"\u0000\u0000\u0000\u0098\u0092\u0001\u0000\u0000\u0000\u0098\u0093\u0001"+
		"\u0000\u0000\u0000\u0098\u0094\u0001\u0000\u0000\u0000\u0098\u0095\u0001"+
		"\u0000\u0000\u0000\u0098\u0096\u0001\u0000\u0000\u0000\u0098\u0097\u0001"+
		"\u0000\u0000\u0000\u0099\u00c1\u0001\u0000\u0000\u0000\u009a\u009b\n\u0010"+
		"\u0000\u0000\u009b\u009c\u0007\u0001\u0000\u0000\u009c\u00c0\u0003\b\u0004"+
		"\u0011\u009d\u009e\n\u000f\u0000\u0000\u009e\u009f\u0007\u0002\u0000\u0000"+
		"\u009f\u00c0\u0003\b\u0004\u0010\u00a0\u00a1\n\r\u0000\u0000\u00a1\u00a2"+
		"\u0007\u0003\u0000\u0000\u00a2\u00c0\u0003\b\u0004\u000e\u00a3\u00a4\n"+
		"\f\u0000\u0000\u00a4\u00a5\u0005\u0001\u0000\u0000\u00a5\u00c0\u0003\b"+
		"\u0004\r\u00a6\u00a7\n\u000b\u0000\u0000\u00a7\u00a8\u0005\u0002\u0000"+
		"\u0000\u00a8\u00c0\u0003\b\u0004\f\u00a9\u00aa\n\n\u0000\u0000\u00aa\u00ab"+
		"\u0005-\u0000\u0000\u00ab\u00c0\u0003\b\u0004\u000b\u00ac\u00af\n\u0019"+
		"\u0000\u0000\u00ad\u00ae\u0005&\u0000\u0000\u00ae\u00b0\u0005\u0012\u0000"+
		"\u0000\u00af\u00ad\u0001\u0000\u0000\u0000\u00af\u00b0\u0001\u0000\u0000"+
		"\u0000\u00b0\u00b1\u0001\u0000\u0000\u0000\u00b1\u00b2\u0005$\u0000\u0000"+
		"\u00b2\u00b3\u0007\u0000\u0000\u0000\u00b3\u00bc\u0005\u001b\u0000\u0000"+
		"\u00b4\u00b9\u0003\b\u0004\u0000\u00b5\u00b6\u0005#\u0000\u0000\u00b6"+
		"\u00b8\u0003\b\u0004\u0000\u00b7\u00b5\u0001\u0000\u0000\u0000\u00b8\u00bb"+
		"\u0001\u0000\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00b9\u00ba"+
		"\u0001\u0000\u0000\u0000\u00ba\u00bd\u0001\u0000\u0000\u0000\u00bb\u00b9"+
		"\u0001\u0000\u0000\u0000\u00bc\u00b4\u0001\u0000\u0000\u0000\u00bc\u00bd"+
		"\u0001\u0000\u0000\u0000\u00bd\u00be\u0001\u0000\u0000\u0000\u00be\u00c0"+
		"\u0005\u001c\u0000\u0000\u00bf\u009a\u0001\u0000\u0000\u0000\u00bf\u009d"+
		"\u0001\u0000\u0000\u0000\u00bf\u00a0\u0001\u0000\u0000\u0000\u00bf\u00a3"+
		"\u0001\u0000\u0000\u0000\u00bf\u00a6\u0001\u0000\u0000\u0000\u00bf\u00a9"+
		"\u0001\u0000\u0000\u0000\u00bf\u00ac\u0001\u0000\u0000\u0000\u00c0\u00c3"+
		"\u0001\u0000\u0000\u0000\u00c1\u00bf\u0001\u0000\u0000\u0000\u00c1\u00c2"+
		"\u0001\u0000\u0000\u0000\u00c2\t\u0001\u0000\u0000\u0000\u00c3\u00c1\u0001"+
		"\u0000\u0000\u0000\u0014\u000f\u0015\u001d),/<>LOfpx|\u0098\u00af\u00b9"+
		"\u00bc\u00bf\u00c1";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}