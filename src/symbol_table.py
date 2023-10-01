from recognized import Token

class SymbolTable:
    _symbols = {
        "program": { "token": "program", "value": None,    "type": None },
        "(":       { "token": "(",       "value": None,    "type": None },
        ")":       { "token": ")",       "value": None,    "type": None },
        "begin":   { "token": "begin",   "value": None,    "type": None },
        "end":     { "token": "end",     "value": None,    "type": None },
        "if":      { "token": "if",      "value": None,    "type": None },
        "then":    { "token": "then",    "value": None,    "type": None },
        "else":    { "token": "else",    "value": None,    "type": None },
        "int":     { "token": "tipo",    "value": "INT",   "type": None },
        "char":    { "token": "tipo",    "value": "CHAR",  "type": None },
        "float":   { "token": "tipo",    "value": "FLOAT", "type": None },
        "while":   { "token": "while",   "value": None,    "type": None },
        "repeat":  { "token": "repeat",  "value": None,    "type": None },
        "until":   { "token": "until",   "value": None,    "type": None },
        ",":       { "token": ",",       "value": None,    "type": None },
        ":":       { "token": ":",       "value": None,    "type": None },
        ";":       { "token": ";",       "value": None,    "type": None },
        ":=":      { "token": ":=",      "value": None,    "type": None },
        "<":       { "token": "op_rel",  "value": "LT",    "type": None },
        "<=":      { "token": "op_rel",  "value": "LE",    "type": None },
        "=":       { "token": "op_rel",  "value": "EQ",    "type": None },
        "!=":      { "token": "op_rel",  "value": "NE",    "type": None },
        ">":       { "token": "op_rel",  "value": "GT",    "type": None },
        ">=":      { "token": "op_rel",  "value": "GE",    "type": None },
        "+":       { "token": "op_rel",  "value": None,    "type": None },
        "*":       { "token": "op_rel",  "value": None,    "type": None },
        "/":       { "token": "op_rel",  "value": None,    "type": None },
        "^":       { "token": "op_rel",  "value": None,    "type": None },
    }

    def get_token(self, lexeme: str) -> Token | None:
        token_exists = self._was_token_registered(lexeme)

        if token_exists:
            symbol = self._symbols[lexeme]
            return Token(symbol["token"], symbol["value"])
        
        return None

    def set_id(self, lexeme: str) -> Token:
        token = self.get_token(lexeme)

        if token != None:
            return token
        else:
            self._symbols[lexeme] = { "token": "id", "value": None, "type": None }
            return Token("id", None)

    def _was_token_registered(self, lexeme: str) -> bool:
        return lexeme in self._symbols
        