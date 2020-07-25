def sum_array(array):
    if len(array) == 1:
        return(array[0])
    else:
        return(array[0]+sum_array(array[1:]))

def max_element(array):
    if len(array) == 1:
        return(array[0])
    if len(array) == 2:
        return(max(array[0],array[1]))
    else:
        return(max(array[-1],max_element(array[:-1])))

def min_element(array):
    if len(array) == 1:
        return(array[0])
    if len(array) == 2:
        return(min(array[0],array[1]))
    else:
        return(min(array[-1],max_element(array[:-1])))

def count_element(num,array):
    count = 0
    if len(array) == 1:
        if num == array[0]:
            return(1)
    else:
        if num == array[-1]:
            count += 1
        count += count_element(num,array[:-1])
    return(count)

