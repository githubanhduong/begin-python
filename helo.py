# Python program for left array rotation

array = [1, 2, 3, 4, 5]
shift = 2

for i in range(0, shift):
    tem = array[0]

    for j in range(0, len(array) - 1):
        array[j] = array[j + 1]
    array[len(array) - 1] = tem

for i in range(0, len(array)):
    print(array[i])
