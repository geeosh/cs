#!/usr/bin/python
# Merge Sort class that allows for O(n log n) sorting of items, using a divide-and-conquer strategy
# There is some memory overhead as it uses two buffers to store items when they are merged

from collections import deque

class QuickSort:

  def __init__(self, items):
    self.items = items

import random

print "Initialize QuickSort with array"

items = [3, 45, 89, 1, 7, 34940, 222222, 18, 2342, 344, 34, 233]

# Shuffle items randomly
random.shuffle(items)

print "Unsorted items: " + ", ".join(str(i) for i in items)

ms = QuickSort(items)
ms.sort()

print "Sorted items: " + ", ".join(str(i) for i in ms.items)
