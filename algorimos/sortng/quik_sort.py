

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

quick_sort(array, 0, len(array) - 1)
print(array)

def partition(array, start, end, compare_func):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and compare_func(array[high], pivot):
            high = high - 1

        while low <= high and not compare_func(array[low], pivot):
            low = low + 1

        if low <= high:
            array[low], arrayb[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end, compare_func):
    if start >= end:
        return

    p = partition(array, start, end, compare_func)
    quick_sort(array, start, p-1, compare_func)
    quick_sort(array, p+1, end, compare_func)

class personas:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return self.name

p1 = personas("rube", 40)
p2 = personas("barbara", 37)
p3 = personas("carelin", 0)
p4 = personas("Abrahan", 19)

array = [p1,p2,p3,p4]

quick_sort(array, 0, len(array) - 1, lambda x, y: x.age < y.age)
for person in array:
    print(person)






