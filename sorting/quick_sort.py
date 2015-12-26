#!/usr/bin/python
# Merge Sort class that allows for O(n log n) sorting of items, using a divide-and-conquer strategy
# There is some memory overhead as it uses two buffers to store items when they are merged

from collections import deque

class QuickSort:

  def __init__(self, items):
    self.items = items

  def sort(self, low = None, high = None):
    if(low == None):
      low = 0
    if (high == None):
      high = len(self.items) - 1

    if(high - low > 0):
      pivot = self.partition(low, high)
      self.sort(low, pivot - 1)
      self.sort(pivot + 1, high)

  def partition(self, low, high):
    pivot = high
    first_high = low

    for i in range(low, high):
      if(self.items[i] < self.items[pivot]):
        # Swap items
        self.items[i], self.items[first_high] = self.items[first_high], self.items[i]
        first_high += 1

    self.items[pivot], self.items[first_high] = self.items[first_high], self.items[pivot]

    return first_high

import random

print "Initialize QuickSort with array"

items = [3, 45, 89, 1, 7, 34940, 222222, 18, 2342, 344, 34, 233]

# Shuffle items randomly
random.shuffle(items)

print "Unsorted items: " + ", ".join(str(i) for i in items)

ms = QuickSort(items)
ms.sort()

print "Sorted items: " + ", ".join(str(i) for i in ms.items)
