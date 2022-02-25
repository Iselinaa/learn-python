board = []

input_array_0 = [[1,2,3],[2,4]]
input_array_1 = [[1,2],[2,4], [[1, [4, 7, [8, 10]]], 5]]

expected_result = [1,2,4,5]


def addToListIfNotExist(array, elements):
    for i in elements:
        if (i not in array):
            array.append(i)
    return array

def flatten(array):
  results = []
  for numbers in array:
    for i in numbers:
        addToListIfNotExist(results, flatten([i]) if isinstance(i, list) else [i])
  return results

result = flatten(input_array_1)
print("result: ", result)

print(addToListIfNotExist([1,4,6], [5,8,9,4]))