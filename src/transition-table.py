class TransitionTable:
  table = {
    "0": { "is_final": False, "movements": { "a": "2", "b": "1" } }
  }

  def move(self, state, char):
    return self.table.get(state).get("movements").get(char)
  
  def is_final(self, state):
    return self.table.get(state).get("is_final")

  def get_initial_state(self):
    return "0"