from timing_sort import run_sorting_algorithm
from random import randint

list_length = 1_000

number_list = [7, 89, 17, 23, 9, 56, 34, 8, 72, 45, 67, 12, 90, 3, 6, 27, 48, 59, 81, 10]

def main():
    # list = [randint(0, list_length) for i in range(list_length)]
    # print(len(list))
    # list = number_list.copy()
    run_sorting_algorithm("sorted", number_list)

if __name__ == "__main__":
    main()
