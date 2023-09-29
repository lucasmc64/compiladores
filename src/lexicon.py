BUFFER_SIZE=4096

class Lexer():
    next_buffer = None
    file_position = { "line": 1, "column": 0 }
    _buffer_position = { "start": 0, "end": 0 }
    
    def __init__(self, file_path):
        self.file = open(file_path)
        self.current_buffer = self.file.read(BUFFER_SIZE)
        
    def get_next_token(self):
        print("Next token")

    def _get_next_char(self):
        print("Next char")
    
    def get_position(self):
        print("Position")

    def stop(self):
        self.file.close()