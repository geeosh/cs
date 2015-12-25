#!/usr/bin/python
# Merge Sort class that allows for O(n log n) sorting of items, using a divide-and-conquer strategy
# There is some memory overhead as it uses two buffers to store items when they are merged

class MergeSort:

  def __init__(self, items):
    self.items = items
    self.sorted = []

  # Sort items
  def sort(self, low = None, high = None):
    if(low == None):
      low = 0
    if(high == None):
      high = len(self.items)
    
    if(low < high):
      middle = (low + high) / 2
      self.sort(low, middle)
      self.sort(middle + 1, high)
      self._merge(low, middle, high)

  # Merge together results
  def _merge(self, low, middle, high):
    # Buffers are expected to be used as FIFO queues
    buffer1 = []; buffer2 = []

    print "Low %d Middle %d High %d" % (low, middle, high)

    for i in range(low,middle):
      print i
      buffer1.append(self.items[i])

    for i in range(middle + 1, high):
      print i
      buffer2.append(self.items[i])

    while(len(buffer1) > 0 and len(buffer2) > 0):
      if(buffer1[0] <= buffer2[0]):
        self.sorted.append(buffer1.pop(0))
      else:
        self.sorted.append(buffer2.pop(0))

    while(len(buffer1) > 0):
      self.sorted.append(buffer1.pop(0))

    while(len(buffer2) > 0):
      self.sorted.append(buffer2.pop(0))


import random

print "Initialize MergeSort with array"

items = [3, 45, 89, 1, 7, 34940, 222222, 18, 2342, 344, 34, 233]

# Shuffle items randomly
random.shuffle(items)

print "Unsorted items: " + ", ".join(str(i) for i in items)

ms = MergeSort(items)
ms.sort()

print "Sorted items: " + ", ".join(str(i) for i in ms.sorted)
