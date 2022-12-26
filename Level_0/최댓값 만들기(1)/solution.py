def maximumMade(numbers):
    list.sort(numbers)
    return numbers[-1]*numbers[-2]