import math

# Search each number until we find our target.
def linearSearch(target, collection):
    for i in collection:
        print(f"linear: {i}")
        # When our current number is our target we're done!
        if i is target:
            return True
    # If ever we don't find the target, it's not in this collection!
    return False

def BinSearch(target, collection):
    midIndex = math.floor(len(collection) /2)
    midPoint = collection[midIndex]
    print(f"Binary: {midPoint}")
    # Check if the mid point of our collection is the target.
    if midPoint is target:
        return True
    # Check if we've run out of numbers to check.
    if len(collection) <= 1:
        return False
    
    # When the target is lower than our mid point...
    if midPoint > target:
        # Half the collection from 0 -> our midpoint and repeat the search.
        return BinSearch(target, collection[0:midIndex])
    # Otherwise half the collection from our midpoint -> the length of the collection and repeat the search.
    return BinSearch(target, collection[midIndex:len(collection)])

def __main__():
    print(linearSearch(7, range(1, 11)))
    print(BinSearch(7, range(1, 11)))

if __name__ == "__main__":
    __main__()
