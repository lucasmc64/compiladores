import production_elements as pe
from recognized import Token

class Productions:
    productions = {
        "funcoes"       : [[pe.P_FUNCTION, pe.P_FUNCTIONS_2], []],
        "funcoes'"      : [[pe.P_FUNCTIONS, []]],
        "funcao"        : [[pe.P_PROGRAM, pe.P_ID, pe.P_OPEN_PARENTHESES, pe.P_CLOSE_PARENTHESES, pe.P_BLOCK]],
        "bloco"         : [[pe.P_BEGIN, pe.P_VARIABLES, pe.P_COMMANDS, pe.P_END]],
        "variaveis"     : [[pe.P_DECLARATION], [pe.P_DECLARATION, pe.P_VARIABLES]],
        "comandos"      : [[pe.P_COMMAND], [pe.P_COMMANDS]],
        "comando"       : [[pe.P_ASSIGNMENT], [pe.P_WHILE], [pe.P_REPEAT], [pe.P_CONTROL], []],
        "declaracao"    : [[pe.P_TYPE, pe.P_COLON, pe.P_IDS, pe.P_SEMICOLON], []],
        "ids"           : [[pe.P_ID], [pe.P_ID, pe.P_COMMA, pe.P_IDS]],
        "atribuicao"    : [[pe.P_ID, pe.P_ASSIGNMENT, pe.P_EXPRESSION]],
        "enquanto"      : [[pe.P_STMT_WHILE, pe.P_CONDITION, pe.P_COMMAND_BLOCK]],
        "repeticao"     : [[pe.P_STMT_REPEAT, pe.P_COMMAND_BLOCK, pe.P_STMT_UNTIL, pe.P_CONDITION]],
        "controle"      : [[pe.P_IF, pe.P_CONDITION, pe.P_COMMAND_BLOCK, pe.P_CONTROL_2]],
        "expressao"     : [[pe.P_EXPRESSION_P2, pe.P_EXPRESSION_2]],
        "expressao'"    : [[pe.P_PLUS, pe.P_EXPRESSION_P2, pe.P_EXPRESSION_2], [pe.P_MINUS, pe.P_EXPRESSION_P2, pe.P_EXPRESSION_2], []],
        "comando_bloco" : [[pe.P_COMMAND], [pe.P_BLOCK]],
        "condicao"      : [[pe.P_EXPRESSION, pe.P_OP_REL, pe.P_EXPRESSION]],
        "controle'"     : [[pe.P_ELSE, pe.P_COMMAND_BLOCK], []],
        "expressao_p2"  : [[pe.P_EXPRESSION_P3, pe.P_EXPRESSION_P2_2]],
        "expressao_p2'" : [[pe.P_TIMES, pe.P_EXPRESSION_P3, pe.P_EXPRESSION_P2_2], [pe.P_DIVIDE, pe.P_EXPRESSION_P3, pe.P_EXPRESSION_P2_2], []],
        "expressao_p3"  : [[pe.P_EXPRESSION_P4, pe.P_EXPRESSION_P3_2]],
        "expressao_p3'" : [[pe.P_EXPONENTIATION, pe.P_EXPRESSION_P4, pe.P_EXPRESSION_P3_2], []],
        "expressao_p4"  : [[pe.P_ID], [pe.P_NUMBER], [pe.P_CHAR], [pe.P_OPEN_PARENTHESES, pe.P_EXPRESSION, pe.P_CLOSE_PARENTHESES], [pe.P_MINUS, pe.P_EXPRESSION_P4]],
    }

    def choose_production(self, token: Token):
        tk_productions = self.productions[token.name]

        for tk_production in tk_productions:
            pass
