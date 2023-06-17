import random
import time
import matplotlib.pyplot as plt


def generate_rand_list(list, list_length=10, max_rand=100, print_values=False):
    for i in range(list_length):
        random_int = random.randint(1, max_rand)
        list.append(random_int)
        if print_values:
            print(f'Number {i}: {random_int}')
    return list


def quick_sort(list):
    if len(list) <= 1:
        return list

    pivot = list[len(list) // 2]

    left_list = []
    right_list = []
    mid_list = []

    for element in list:
        if element < pivot:
            left_list.append(element)
        elif element > pivot:
            right_list.append(element)
        else:
            mid_list.append(element)

    return quick_sort(left_list) + mid_list + quick_sort(right_list)


def bubble_sort(list):
    length = len(list)

    for i in range(length):
        swap = False

        for j in range(0, length - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swap = True

        if not swap:
            break

    return list

def selection_sort(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j] :
                list[j + 1] = list[j]
                j -= 1
        list[j + 1] = key



def generate_rand_list(list, list_length=10, max_rand=100, print_values=False):
    for i in range(list_length):
        random_int = random.randint(1, max_rand)
        list.append(random_int)
        if print_values:
            print(f'Number {i}: {random_int}')
    return list


def measure_time(string, given_list):
    start = time.time()

    if string == "quick_sort":
        quick_sort(given_list)
    elif string == "bubble_sort":
        bubble_sort(given_list)
    elif string == "selection_sort":
        selection_sort(given_list)
    elif string == "insertion_sort":
        insertion_sort(given_list)
    else:
        given_list.sort()

    end = time.time()

    total_time = end - start
    print(f"The execution time of {string} was {total_time}s")
    return total_time


def main():
    list = []
    rand_list = generate_rand_list(list, 1000, 500)

    quick_sort_time = measure_time("quick_sort", rand_list)
    bubble_sort_time = measure_time("bubble_sort", rand_list)
    selection_sort_time = measure_time("selection_sort", rand_list)
    insertion_sort_time = measure_time("insertion_sort", rand_list)
    python_sorting_time = measure_time("python_sorting", rand_list)

    algorithms = ['Quick Sort', 'Bubble Sort', 'Selection Sort', 'Insertion Sort']

    try:
        print(f"Python sorting was {quick_sort_time / python_sorting_time} times faster than {algorithms[0]}")
        print(f"Python sorting was {bubble_sort_time / python_sorting_time} times faster than {algorithms[1]}")
        print(f"Python sorting was {selection_sort_time / python_sorting_time} times faster than {algorithms[2]}")
        print(f"Python sorting was {insertion_sort_time / python_sorting_time} times faster than {algorithms[3]}")
    except ZeroDivisionError:
        print("Python sorting was significantly faster than the other sorting methods")

    times = [quick_sort_time, bubble_sort_time, selection_sort_time, insertion_sort_time]
    plt.barh(algorithms, times, color='blue')
    plt.xlabel('Time (s)')
    plt.title('Execution Time of Sorting Algorithms')
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        "End of execution"
