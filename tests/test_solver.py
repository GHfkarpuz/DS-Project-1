import pytest
from ace.solver import Solver

def test_solver_sum():
    s = Solver([1, 2, 3])
    assert s.solve() == 6

def test_solver_empty():
    s = Solver()
    assert s.solve() == 0.0
    