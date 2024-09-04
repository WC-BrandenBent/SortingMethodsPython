from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    set_up_var = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    repeat_times = repeat(setup=set_up_var, stmt=stmt, repeat=3, number=10)
        # Timing Experiment 1:
        #   Execute setup code
        #   Measure time for 10 executions of stmt
        # Timing Experiment 2:
        #   Execute setup code
        #   Measure time for 10 executions of stmt
        # Timing Experiment 3:
        #   Execute setup code
        #   Measure time for 10 executions of stmt
        # Result: [time1, time2, time3]
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(repeat_times)}")