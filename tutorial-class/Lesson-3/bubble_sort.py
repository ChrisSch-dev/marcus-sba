numbers = [2, 35, 50, 98, 14, 93, 33]

def swap(numbers, i, j):
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp

def bubble_sort(numbers):
    length = len(numbers)
    for i in range(length - 1):
        if numbers[i] > numbers[i + 1]:
            swap(numbers, 0, i + 1)

    if numbers[0] > numbers[1]:
        swap(numbers, 0, 1)
    if numbers[1] > numbers[2]:
        swap(numbers, 1, 2)

    if numbers[5] > numbers[6]:
        swap(numbers, 5, 6)
