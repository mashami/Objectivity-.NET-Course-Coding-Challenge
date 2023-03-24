# Question

# Create a function that takes two arrays (original array, updated array)
# as input and return two arrays of modifications (new elements, removed elements). 


def modificationsForArray(originalArray, updatedArray):
    
    original = set(originalArray)
    updated = set(updatedArray)

    newElements = list(updated - original)
    removedElements = list(original - updated)

    return newElements, removedElements

originalArray = [55, 24, 45, 11, 43,]
updatedArray = [43, 34, 55, 23, 1]

newElements, removedElements = modificationsForArray(originalArray, updatedArray)

print("New elements in an Array:", newElements)  
print("Removed elements in an Array:", removedElements)  