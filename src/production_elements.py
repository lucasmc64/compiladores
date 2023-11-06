class ProductionElement:
    def __init__(self, value, is_terminal) -> None:
        self.value = value
        self.is_terminal = is_terminal

# Terminals
P_PROGRAM              = ProductionElement(value="program",       is_terminal=True)
P_OPEN_PARENTHESES     = ProductionElement(value="(",             is_terminal=True)
P_CLOSE_PARENTHESES    = ProductionElement(value=")",             is_terminal=True)
P_BEGIN                = ProductionElement(value="begin",         is_terminal=True)
P_END                  = ProductionElement(value="end",           is_terminal=True)
P_IF                   = ProductionElement(value="if",            is_terminal=True)
P_THEN                 = ProductionElement(value="then",          is_terminal=True)
P_ELSE                 = ProductionElement(value="else",          is_terminal=True)
P_SEMICOLON            = ProductionElement(value=";",             is_terminal=True)
P_TYPE                 = ProductionElement(value="tipo",          is_terminal=True)
P_TYPE_INT             = ProductionElement(value="int",           is_terminal=True)
P_TYPE_CHAR            = ProductionElement(value="char",          is_terminal=True)
P_TYPE_FLOAT           = ProductionElement(value="float",         is_terminal=True)
P_STMT_WHILE           = ProductionElement(value="while",         is_terminal=True)
P_STMT_REPEAT          = ProductionElement(value="repeat",        is_terminal=True)
P_STMT_UNTIL           = ProductionElement(value="until",         is_terminal=True)
P_COMMA                = ProductionElement(value=",",             is_terminal=True)
P_COLON                = ProductionElement(value=":",             is_terminal=True)
P_SEMICOLON            = ProductionElement(value=";",             is_terminal=True)
P_ASSIGNMENT           = ProductionElement(value=":=",            is_terminal=True)
P_OP_REL               = ProductionElement(value="op_rel",        is_terminal=True)
P_PLUS                 = ProductionElement(value="+",             is_terminal=True)
P_MINUS                = ProductionElement(value="-",             is_terminal=True)
P_TIMES                = ProductionElement(value="*",             is_terminal=True)
P_DIVIDE               = ProductionElement(value="/",             is_terminal=True)
P_EXPONENTIATION       = ProductionElement(value="^",             is_terminal=True)
P_ID                   = ProductionElement(value="id",            is_terminal=True)
P_NUMBER               = ProductionElement(value="number",        is_terminal=True)
P_CHAR                 = ProductionElement(value="char",          is_terminal=True)

# Non Terminals
P_FUNCTIONS            = ProductionElement(value="funcoes",       is_terminal=False)
P_FUNCTIONS_2          = ProductionElement(value="funcoes'",      is_terminal=False)
P_FUNCTION             = ProductionElement(value="funcao",        is_terminal=False)
P_BLOCK                = ProductionElement(value="bloco",         is_terminal=False)
P_VARIABLES            = ProductionElement(value="variaveis",     is_terminal=False)
P_COMMANDS             = ProductionElement(value="comandos",      is_terminal=False)
P_COMMAND              = ProductionElement(value="comando",       is_terminal=False)
P_DECLARATION          = ProductionElement(value="declaracao",    is_terminal=False)
P_IDS                  = ProductionElement(value="ids",           is_terminal=False)
P_ASSIGNMENT           = ProductionElement(value="atribuicao",    is_terminal=False)
P_WHILE                = ProductionElement(value="enquanto",      is_terminal=False)
P_REPEAT               = ProductionElement(value="repetição",     is_terminal=False)
P_CONTROL              = ProductionElement(value="controle",      is_terminal=False)
P_EXPRESSION           = ProductionElement(value="expressao",     is_terminal=False)
P_EXPRESSION_2         = ProductionElement(value="expressao'",    is_terminal=False)
P_COMMAND_BLOCK        = ProductionElement(value="comando_bloco", is_terminal=False)
P_CONDITION            = ProductionElement(value="condicao",      is_terminal=False)
P_CONTROL_2            = ProductionElement(value="controle'",     is_terminal=False)
P_EXPRESSION_P2        = ProductionElement(value="expressao_p2",  is_terminal=False)
P_EXPRESSION_P2_2      = ProductionElement(value="expressao_p2'", is_terminal=False)
P_EXPRESSION_P3        = ProductionElement(value="expressao_p3",  is_terminal=False)
P_EXPRESSION_P_3       = ProductionElement(value="expressao_p3'", is_terminal=False)
P_EXPRESSION_P4        = ProductionElement(value="expressao_p4",  is_terminal=False)
