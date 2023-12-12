
def resolveDirectionalIndex(array, origin, x, y):
    lineLength = array.find('\n') + 1
    newIndex = origin
    
    newIndex += x
    newIndex += lineLength * y
    
    if newIndex > len(array) or newIndex < 0 or  array[newIndex] == '\n':
        return -1
        
    return newIndex
