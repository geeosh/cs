#!/usr/bin/python
# Merge Sort class that allows for O(n log n) sorting of items, using a divide-and-conquer strategy
# There is some memory overhead as it uses two buffers to store items when they are merged

from collections import deque

class MergeSort:

  def __init__(self, items):
    self.items = items

    # Buffers hold elements to merge
    # They are FIFO queues, deque is best data structure in Python for this
    self.buffer1 = deque()
    self.buffer2 = deque()

  # Sort items
  def sort(self, low = None, high = None):
    if(low == None):
      low = 0
    if(high == None):
      high = len(self.items) - 1
    
    if(low < high):
      middle = (low + high) / 2
      self.sort(low, middle)
      self.sort(middle + 1, high)
      self._merge(low, middle, high)

  # Merge together results
  def _merge(self, low, middle, high):
    # For loops with range are not inclusive of last element, so need to add 1
    for i in range(low, middle + 1):
      self.buffer1.append(self.items[i])

    for i in range(middle + 1, high + 1):
      self.buffer2.append(self.items[i])

    i = low
    while(len(self.buffer1) > 0 and len(self.buffer2) > 0):
      # Pick lowest order items off head of buffers
      if(self.buffer1[0] <= self.buffer2[0]):
        self.items[i] = self.buffer1.popleft()
      else:
        self.items[i] = self.buffer2.popleft()
      i += 1

    while(len(self.buffer1) > 0):
      self.items[i] = self.buffer1.popleft()
      i += 1

    while(len(self.buffer2) > 0):
      self.items[i] = self.buffer2.popleft()
      i += 1

import random

print "Initialize MergeSort with list"

items = [3, 45, 89, 1, 7, 34940, 222222, 18, 2342, 344, 34, 233]

# Shuffle items randomly
random.shuffle(items)

print "Unsorted items: " + ", ".join(str(i) for i in items)

ms = MergeSort(items)
ms.sort()

print "Sorted items: " + ", ".join(str(i) for i in ms.items)
