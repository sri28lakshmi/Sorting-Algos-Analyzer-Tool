from SortingAlgos import quicksort, mergesort, bubblesort, selectionsort, insertionsort
import time
from random import randint

def create_random_list(size, max_val):
    rand_list = [randint(1, max_val) for i in range(size)]
    return rand_list

def analyze_func(func_name, arr):
    start_time = time.time()
    func_name(arr)
    end_time = time.time()
    seconds = end_time - start_time
    print(f"{func_name.__name__.capitalize()}\t->Elapsed time: {seconds:.5f}")

def main():
    print("~WELCOME TO RUNTIME ANALYZER TOOL~")
    print("PRESS 1: START\nPRESS 2: EXIT")
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        size = int(input("What size list do you want to create? "))
        max_val = int(input("What is the max value of the list? "))
        run_no = int(input("How many time do you want to run?"))
        for num in range(run_no):
            print(f"Run {num + 1}")
            l = create_random_list(size, max_val)
            analyze_func(bubblesort, l.copy())
            analyze_func(mergesort, l)
            analyze_func(quicksort, l)
            analyze_func(sorted, l)
            print("-" * 40)
    elif choice == 2:
        exit()
    else:


main()


