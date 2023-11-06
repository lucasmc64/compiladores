from lexicon import Lexer
from productions import Productions

class Syntactical:
  def __init__(self, lexer: Lexer, productions: Productions) -> None:
    self.lexer = lexer
    self.productions = productions

  def analysis(self):
    token = self.lexer.get_next_token()

    
