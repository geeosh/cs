#!/usr/bin/python
# Binary Search class that allows for O(log n) discovery of an item in a sorted array

class BinarySearch:

  def __init__(self, items):
    self.items = items

  # Find item amongst array of items
  # Returns index of item, or -1 if not found

  def search(self, item, low = None, high = None):
    # Initialize low and high with 0 and item array count index
    if(low == None):
      low = 0
    if(high == None):
      high = len(self.items) - 1

    # Key not found
    print "Low %d High %d" % (low,high)
    
    if(low > high):
      return -1

    middle = (low + high) / 2

    # Found item!
    if(self.items[middle] == item):
      return middle

    # If item is less than middle of array, search lower half
    if(self.items[middle] > item):
      return self.search(item, low, middle - 1)

    # Otherwise search upper half
    else:
      return self.search(item, middle + 1, high)


print "Initialize BinarySearch with sorted array"
sorted_array = [1,3,7,18,34,45,89,233,344,2342,34940,222222]
bs = BinarySearch(sorted_array)

print "Searching for 45"
print "Index: " + str(bs.search(45))

print "Searching for 222222"
print "Index: " + str(bs.search(222222))

print "Searching for 1"
print "Index: " + str(bs.search(1))

print "Searching for (non-existent) 98"
print "Index: " + str(bs.search(98))

print "Searching for (non-existent) 'abc'"
print "Index: " + str(bs.search('abc'))

