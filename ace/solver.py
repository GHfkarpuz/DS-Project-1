"""Solver-class and solver function"""

from typing import Iterable

class Solver:
    def __init__(self, data=None):
        self.data = data

    def solve(self) -> float:
        """
        still TODO.
        """
        if self.data is None:
            return 0.0
        # Beispiel: Summe
        return sum(self.data)
