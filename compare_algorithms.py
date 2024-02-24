import timeit
import random
import matplotlib.pyplot as plt
from merge_sort import merge_sort
from insertion_sort import insertion_sort

def tim_sort(arr):
    arr.sort()

def generate_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time(sort_function, data):
    return timeit.timeit(lambda: sort_function(data.copy()), number=10)

def print_results(results):
    print(f"\n{'':<18} | {'10':^15} | {'100':^15} | {'1000':^15} | {'5000':^15} | {'10000':^15}")
    print(f"{'-'*104}")
    for sort_type, sort_times in results.items():
        print("{:<18} | {:^15.6f} | {:^15.6f} | {:^15.6f} | {:^15.6f} | {:^15.6f}".format(sort_type, *sort_times))
    print('\n')

def plot_graph(results, sizes):
    for sort_type, sort_times in results.items():
        plt.plot(sizes, sort_times, label=sort_type)

    plt.xlabel('Розмір вхідного масиву')
    plt.ylabel('Час виконнання (сек)')
    plt.title('Порівняння ефективності алгоритмів сортування\nза часом виконання\n')
    plt.legend()
    plt.show()

def compare_algorithms():
    sizes = [10, 100, 1000, 5000, 10000]

    merge_times = []
    insertion_times = []
    tim_times = []

    for size in sizes:
        data = generate_data(size)

        merge_time = measure_time(merge_sort, data)
        insertion_time = measure_time(insertion_sort, data)
        tim_time = measure_time(tim_sort, data)

        merge_times.append(merge_time)
        insertion_times.append(insertion_time)
        tim_times.append(tim_time)

    results = {
        "Merge Sort": merge_times,
        "Insertion Sort": insertion_times, 
        "Timsort": tim_times
    }

    print_results(results)
    plot_graph(results, sizes)

if __name__ == "__main__":
    compare_algorithms()
