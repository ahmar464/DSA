# ////////////////  Quick Sort ////////////////////////////
def swap(a,b,array):
    if a!=b:
        temp=array[a]
        array[a]=array[b]
        array[b]=temp


def quick_sort(elements,start,end):
    if start < end:
        pi = partition(elements,start,end)
        quick_sort(elements,start,(pi-1))
        quick_sort(elements,pi+1,end)


def partition(elements,start,end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end,elements)

    swap(pivot_index,end,elements)
    return end


# elements = [11,9,29,7,2,15,28]
elements = ["mona", "dhaval", "aamir", "tina", "chang"]
quick_sort(elements, 0, (len(elements)-1))
print(elements)