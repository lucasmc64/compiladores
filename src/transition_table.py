class TransitionTable:
    transitions = {
        "-1": { "is_final": True,  "movements": {  } },
        "0":  { "is_final": False, "movements": { "p": "1", "(": "8", ")": "9", "b": "10", "e": "15" } },
        "1":  { "is_final": False, "movements": { "r": "2" } },
        "2":  { "is_final": False, "movements": { "o": "3" } },
        "3":  { "is_final": False, "movements": { "g": "4" } },
        "4":  { "is_final": False, "movements": { "r": "5" } },
        "5":  { "is_final": False, "movements": { "a": "6" } },
        "6":  { "is_final": False, "movements": { "m": "7" } },
        "7":  { "is_final": True,  "movements": {  } },
        "8":  { "is_final": True,  "movements": {  } },
        "9":  { "is_final": True,  "movements": {  } },
        "10": { "is_final": False, "movements": { "e": "11" } },
        "11": { "is_final": False, "movements": { "g": "12" } },
        "12": { "is_final": False, "movements": { "i": "13" } },
        "13": { "is_final": False, "movements": { "n": "14" } },
        "14": { "is_final": True,  "movements": {  } },
        "15": { "is_final": False, "movements": { "n": "16" } },
        "16": { "is_final": False, "movements": { "d": "17" } },
        "17": { "is_final": True,  "movements": {  } },
    }

    def __init__(self, symbol_table) -> None:
        self.symbol_table = symbol_table

    def move(self, state: str, char) -> str:
        has_movement = char in self.transitions[state]["movements"]
        return self.transitions[state]["movements"][char] if has_movement else "-1"
    
    def is_final(self, state: str) -> bool:
        return self.transitions[state]["is_final"]

    def get_initial_state(self) ->  str:
        return "0"
    
    def execute_actions(self, state: str, position: { "line": str, "column": str }, lexeme):
        if state == "-1":
            print(f"Error (invalid token): Token não reconhecido")
            print(position)
            exit(1)
        elif state == "7":
            return self.symbol_table.get_token(lexeme)
        elif state == "8":
            return self.symbol_table.get_token(lexeme)
        elif state == "9":
            return self.symbol_table.get_token(lexeme)
        elif state == "14":
            return self.symbol_table.get_token(lexeme)
        elif state == "17":
            return self.symbol_table.get_token(lexeme)

