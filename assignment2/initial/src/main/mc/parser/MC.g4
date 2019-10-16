grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
    language=Python3;
}
//Huynh Quoc Phu - 1712638
// PROGRAM STRUCTURE
program: declarates+ EOF;

declarates: (var_declarate | func_declarate);



//2.1 Variable Declaration :
var_declarate: primitive_type  var (COMA var)* SEMI; // With SEMI 
primitive_type: BOOLEAN | INT | FLOAT | STRING;
var: ID | ID LSB INTLIT RSB;

//2.2 Function Declaration:
func_declarate: func_type ID LB (para (COMA para)*)* RB block_statement;

func_type: primitive_type | VOID | array_pointer_type;
array_pointer_type: primitive_type LSB RSB;
para: primitive_type (ID | ID LSB RSB);


// LEXICAL SPECIFICATION
//STATEMENTS AND CONTROL FLOW:
statement
    : if_statement
    | do_while_statement
    | for_statement
    | break_statement
    | continue_statement
    | return_statement
    | exp_statement
    | block_statement
    ;

//IF - ELSE STATEMENTS:
if_statement
    : IF LB exp RB statement (else_statement)?
    ;

else_statement
    : ELSE statement
    ;

//DO - WHILE STATEMENT:
do_while_statement
    : DO statement* WHILE exp SEMI
    ;

//FOR STATEMENT:
for_statement
    : FOR LB exp SEMI exp SEMI exp RB statement
    ;

//BREAK STATEMENT:
break_statement
    : BREAK SEMI
    ;

//CONTINUE STATEMENT:
continue_statement
    : CONTINUE SEMI
    ;

//RETURN STATEMENT:
return_statement
    : RETURN (exp)? SEMI
    ;

//EXPRESSION STATEMENT:
exp_statement
    : exp SEMI
    ;

//BLOCK STATEMENT:
block_statement
    : LP stmt_vardecl* RP
    ;
stmt_vardecl
    : statement
    | var_declarate
    ;

//LITERALS:
literals
    : INTLIT
    | FLOATLIT
    | boolean_literals
    | STRINGLIT
    ;
//INTERGER LITERALS:
INTLIT: Digit+;


//FLOATING-POINT LITERAL:
FLOATLIT
    :   Digit+ Dot (Digit* | Exponent?)
    |   Digit* Dot Digit+ Exponent?
    |   Digit+ Exponent
    ;

fragment
Dot : '.';
fragment 
Exponent: [eE] SUB? Digit+ ;

//BOOLEAN LITERAL:
boolean_literals
    : TRUE | FALSE;

//STRING LITERAL: 
STRINGLIT: '"' STR_CHAR* '"'
    {
        y = str(self.text)
        self.text = y[1:-1]
    }
    ;
fragment STR_CHAR: ~[\b\t\n\f\r"\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr"\\] ;

//KEYWORDS:
BOOLEAN: 'boolean';

BREAK: 'break';

CONTINUE: 'continue';

ELSE: 'else';

FOR: 'for';

FLOAT: 'float';

IF: 'if';

INT: 'int';

RETURN: 'return';

VOID: 'void';

DO: 'do';

WHILE: 'while';

TRUE: 'true';

FALSE: 'false';

STRING: 'string';

//EXPRESSION : 
exp : exp1 ASSIGN exp |exp1;

exp1: exp1 OR exp2 | exp2;

exp2: exp2 AND exp3 | exp3;

exp3: exp4 (EQ | NEQ) exp4 | exp4;

exp4: exp5 (LT | LTE | GT | GTE) exp5 | exp5;

exp5: exp5 (ADD | SUB) exp6 | exp6;

exp6: exp6 (DIV | MUL | MOD) exp7 |exp7;

exp7: (SUB | NOT) exp7 | exp8;

exp8: operand LSB RSB | operand;

operand
    : literals 
    | ID 
    | func_call
    | sub_exp
    | index_exp
    ;

sub_exp: LB exp RB;

func_call: ID LB exp (COMA exp)* RB;

index_exp: (ID|func_call) LSB exp RSB;


fragment
Letter
    :   [a-zA-Z]
    ;

fragment
Digit: [0-9];

//IDENTIFIERS:
ID
    :   (Letter 
    |   '_')
        (Letter
    |   Digit
    |   '_')*
    ;


//COMMENT:
BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;

//OPERATORS:
ADD: '+';

SUB: '-';

MUL: '*';

DIV: '/';

MOD: '%';


NOT: '!';

OR : '||';

AND: '&&';


ASSIGN: '=';

LTE: '<=';

GTE: '>=';

NEQ: '!=';

EQ : '==' ;

LT : '<' ;

GT : '>' ;

//SEPARATORS:
LSB: '[';

RSB: ']';

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';';
COMA: ',';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
UNCLOSE_STRING: '"'(STR_CHAR)*; 
ERROR_CHAR: .;
ILLEGAL_ESCAPE
    :  '"' (~[\b\t\n\f\r"\\] 
    | '\\' ~[btnfr"\\])* '"'
    {
        position = self.text.find("\\")
        y = str(self.text)
        self.text = y[1:position + 2]
    }
    ;

