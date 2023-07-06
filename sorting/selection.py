def selection(data):
    array = data
    for i in range(len(array)):
        start_step = i
        step_min = i
        for j in range(step_min + 1, len(array)):
            if array[step_min] > array[j]:
                step_min = j
        temp = array[step_min]
        array[step_min] = array[start_step]
        array[start_step] = temp

    return array


data = [20, 12, 10, 12, 2]
print(selection(data))
