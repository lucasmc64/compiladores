import re as regex

from colors import RED, RESET
from stack import Stack

BUFFER_SIZE=4096
# BUFFER_SIZE=4

class Lexer():
    _file_position = { "line": 1, "column": 0 }
    buffer_position = { "start": 0, "end": 0 }
    _next_buffer = None
    _stack = Stack()
    
    def __init__(self, file_path, transition_table):
        self._file = open(file_path)
        self._current_buffer = self._file.read(BUFFER_SIZE)
        self.transition_table = transition_table
        
    def get_next_token(self):
        state = self.transition_table.get_initial_state()

        char = self._get_next_char()

        if char == "{":
            self._stack.push(char)

        # print(f"A - char: '{char}'")

        # Ignore white spaces and line breaks

        while char != None and (regex.search("[\s\t\n]", char) != None or self._stack.size() > 0):
            self._restore_buffer_positioning()
            char = self._get_next_char()

            if char == "{":
                self._stack.push(char)
            elif char == "}":
                self._stack.pop()

                if self._stack.size() == 0:
                    char = self._get_next_char()

            # print(char, is_comment)
            # print(char != None or char == "{", regex.search('[\s\t\n]', char) != None, is_comment)

        # print(f"{state}, '{char}'")
        while char != None:
            if self.buffer_position["end"] >= 2 * BUFFER_SIZE:
                print(f"{RED}Error (stack overflow): Token muito grande{RESET}")
                print(self._file_position)
                exit(1)

            # print(f"{state}, '{char}'")
            state = self.transition_table.move(state, char)
            # print(f"{state}, '{char}'")

            if self.transition_table.is_final(state):
                break

            char = self._get_next_char()

        # print(char, self.buffer_position["start"], self.buffer_position["end"])
        if char == None:
            # EOF

            if self.buffer_position["start"] == self.buffer_position["end"]:
                return None
            else:
                # Process the last token
                state = self.transition_table.move(state, "EOF")

        # print(f"self.buffer_position['start']: '{self.buffer_position['start']}'")
        # print(f"self.buffer_position['end']: '{self.buffer_position['end']}'")
        # print(f"self._current_buffer: '{self._current_buffer}'")
        # print(f"self._next_buffer: '{self._next_buffer}'")

        token = self.transition_table.execute_actions(state, self, char == None)
        self._restore_buffer_positioning()

        return token
        
    def _get_next_char(self):
        position_to_read = self.buffer_position.get("end")
        char = None

        # print(self._next_buffer)
        # print(position_to_read)
        if (len(self._current_buffer) < BUFFER_SIZE or (self._next_buffer != None and len(self._next_buffer) < BUFFER_SIZE)) and position_to_read >= (len(self._current_buffer) + len(self._next_buffer) if self._next_buffer != None else len(self._current_buffer)):
            # EOF
            return None 

        if position_to_read >= BUFFER_SIZE:
            position_to_read -= BUFFER_SIZE
            
            if self._next_buffer == None:
                self._next_buffer = self._file.read(BUFFER_SIZE)
            
                if len(self._next_buffer) == 0:
                    # EOF
                    return None

            char = self._next_buffer[position_to_read]
        else:
            char = self._current_buffer[position_to_read]

        if char == "\n":
            self._file_position["line"] += 1
        else:
            self._file_position["column"] += 1

        self.buffer_position["end"] += 1

        return char
    
    def handle_lookahead(self, positions):
        self.buffer_position["end"] -= positions
        # TODO: Reposicionar self.file_position para infomar posição certa nas mensagens de erro
        
    def _restore_buffer_positioning(self):
        if self._next_buffer != None:
            self._current_buffer = self._next_buffer
            self._next_buffer = None

            new_initial_position = self.buffer_position["end"] - BUFFER_SIZE
            new_initial_position = 0 if new_initial_position < 0 else new_initial_position
        else:
            new_initial_position = self.buffer_position["end"]
        
        self.buffer_position["start"] = new_initial_position
        self.buffer_position["end"] = new_initial_position
    
    def get_position(self):
        return self._file_position

    def stop(self):
        self.file.close()