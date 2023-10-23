grammar grammarYapl;

// Tokens
CLASS: 'class' | 'CLASS';
ELSE: 'else' | 'ELSE';
FI: 'fi' | 'FI';
IF: 'if' | 'IF';
IN: 'in' | 'IN';
INHERITS: 'inherits' | 'INHERITS';
ISVOID: 'isvoid' | 'ISVOID';
LOOP: 'loop' | 'LOOP';
POOL: 'pool' | 'POOL';
THEN: 'then' | 'THEN';
WHILE: 'while' | 'WHILE';
NEW: 'new' | 'NEW';
NOT: 'not' | 'NOT';
LET: 'let';

TYPE_ID: [A-Z][a-zA-Z0-9_]* | 'SELF_TYPE';
OBJECT_ID: [a-z][a-zA-Z0-9_]*;
INTEGER: [0-9]+;
BOOL: 'true' | 'false';
STRING: '"' (~["\r\n] | '\\' .)* '"';

WHITESPACE: (' ' | '\n' | '\f' | '\r' | '\t') -> skip;
NEWLINE: [\r\n]+ -> skip;
COMMENT: '--' .*? NEWLINE -> skip;
COMMENT_BLOCK: '(*' .*? '*)' -> skip;

LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACE  : '{' ;
RBRACE  : '}' ;
LBRACKET : '[' ;
RBRACKET : ']' ;

COLON   : ':' ;
SEMICOLON : ';' ;
COMMA   : ',' ;

DOT     : '.' ;
NEG     : '~' ;
AT      : '@' ;

MULT    : '*' ;
DIV     : '/' ;
PLUS    : '+' ;
MINUS   : '-' ;

LE      : '<=' ;
LT      : '<' ;
EQ      : '=' ;

INCR    : '++' ;
DECR    : '--' ;
ASSIGN_MULT : '=*' ;
ASSIGN_DIV  : '=/' ;
ASSIGN_PLUS : '=+' ;
ASSIGN_MINUS : '=-' ;
ASSIGN  : '<-' ;

// Grammar rules
program: (class_def SEMICOLON)+;

class_def: CLASS TYPE_ID (INHERITS TYPE_ID)? LBRACE (feature SEMICOLON)* RBRACE;

feature: OBJECT_ID (LPAREN (formal (COMMA formal)*)? RPAREN)? COLON TYPE_ID LBRACE expr RBRACE #method
    | (TYPE_ID | OBJECT_ID) COLON TYPE_ID (ASSIGN expr)? #attribute
;

formal: OBJECT_ID COLON TYPE_ID;

expr: expr (AT TYPE_ID)? DOT (TYPE_ID | OBJECT_ID) LPAREN (expr (COMMA expr)*)? RPAREN #dispatch
    | (TYPE_ID | OBJECT_ID) LPAREN (expr (COMMA expr)*)? RPAREN #static_dispatch
    | IF expr THEN expr ELSE expr FI #if
    | WHILE expr LOOP expr POOL #while
    | LBRACE (expr SEMICOLON)+ RBRACE #block
    | LET (TYPE_ID | OBJECT_ID) COLON TYPE_ID (ASSIGN expr)? (COMMA (TYPE_ID | OBJECT_ID) COLON TYPE_ID (ASSIGN expr)?)* IN expr #let
    | NEW TYPE_ID #new
    | NEG expr #neg
    | ISVOID expr #isvoid
    | expr (MULT|DIV) expr #mulDiv
    | expr (PLUS|MINUS) expr #addSub
    | MINUS expr #minus
    | expr (LE|LT) expr #comparison
    | expr '&' expr #and
    | expr '|' expr #or
    | expr EQ expr #eq
    | NOT expr #not
    | (TYPE_ID | OBJECT_ID) ASSIGN expr #assign
    | LPAREN expr RPAREN #parenthesis
    | OBJECT_ID #object_id
    | INTEGER #integer
    | STRING #string
    | BOOL #bool
    | TYPE_ID #type_id
    | 'self' #self
;
