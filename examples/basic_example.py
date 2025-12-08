from ace.solver import Solver

def run_example():
    s = Solver([1, 2, 3])
    print("Result:", s.solve())

if __name__ == "__main__":
    run_example()
