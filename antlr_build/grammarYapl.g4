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
formal: OBJECT_ID COLON TYPE_ID;
feature: OBJECT_ID (LPAREN (formal (COMMA formal)*)? RPAREN)? COLON TYPE_ID LBRACE expr RBRACE #method
    | OBJECT_ID COLON TYPE_ID (ASSIGN expr)? #attribute
;

expr: expr (AT TYPE_ID)? DOT OBJECT_ID LPAREN (expr (COMMA expr)*)? RPAREN #dispatch
    | NEG expr #neg
    | ISVOID expr #isvoid
    | expr (MULT|DIV) expr #mulDiv
    | expr (PLUS|MINUS) expr #addSub
    | expr (LE|LT|EQ) expr #comparison
    | expr '&' expr #and
    | expr '|' expr #or
    | NOT expr #not
    | OBJECT_ID ASSIGN expr #assign
    | OBJECT_ID LPAREN (expr (COMMA expr)*)? RPAREN #static_dispatch
    | IF expr THEN expr ELSE expr FI #if
    | WHILE expr LOOP expr POOL #while
    | LBRACE (expr SEMICOLON)+ RBRACE #block
    | LET OBJECT_ID COLON TYPE_ID (ASSIGN expr)? (COMMA OBJECT_ID COLON TYPE_ID (ASSIGN expr)?)* IN expr #let
    | NEW TYPE_ID #new
    | MINUS expr #minus
    | LPAREN expr RPAREN #parenthesis
    | TYPE_ID #type_id
    | OBJECT_ID #object_id
    | INTEGER #integer
    | STRING #string
    | BOOL #bool
    | 'self' #self
;
