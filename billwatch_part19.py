# === Stage 19: Add undo support for the last simple mutation ===
# Project: BillWatch
class UndoStack:
    def __init__(self):
        self._history = []
        self._cursor = -1

    def push(self, state):
        self._history.append(state)
        self._cursor = len(self._history)

    def undo(self):
        if self._cursor > 0:
            self._cursor -= 1
            return self._history[self._cursor]
        return None

    def can_undo(self):
        return self._cursor > 0
