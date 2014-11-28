#!/usr/bin/ruby
# Simple singly linked list, 0-indexed

class SinglyLinkedList
  attr_accessor :head

  def initialize
    self.head = Node.new(nil)
  end

  # Retreive last node
  def tail
    iterate
  end

  # Iterates over all the elements in the list and can perform any operation on each node
  # Returns last node with a value in it
  def iterate
    prev, at = nil, head
    while(!at.next.nil?) do
      yield prev, at if block_given? # yield is about 2x faster than block.call
      prev, at = at, at.next
    end
    at || prev
  end

   # Get the current length of the list. O(n)
  def length
    i = 0
    iterate do
      i += 1
    end
    i
  end

  def at(index)
    i = 0
    iterate do |prev, current|
      return current if i == index
      i += 1
    end
    nil
  end

  def index(value)
    i = 0
    iterate do |prev, current|
      return i if current.value == value
      i += 1
    end
    nil
  end
  
  # Append an element to the tail of the list. O(n)
  def push(value)
    tail.value = value
    tail.next = Node.new
    true
  end

  # Removes value from list. If in list, return true, otherwise false
  def pop(value)
    iterate do |prev, current|
      if current.value == value
        # Assume GC will take care of orphaned node
        prev.next = current.next
        return true
      end
    end
    false
  end
end

class Node
  attr_accessor :value, :next

  def initialize(value = nil)
    self.value, self.next = value, nil
  end
end


# Initialize List
sll = SinglyLinkedList.new
puts "Initialize list and add 1..10"

1.upto(10).each{|i| sll.push(i) }

puts "First value: #{sll.head.value}"
puts "Last value should be empty: #{sll.tail.value.nil?}"
len = sll.length
puts "Length: #{len}"
midpoint = (len / 2).floor
puts "Value at midpoint of #{midpoint}: #{sll.at(midpoint - 1).value}"
puts "Index of 2: #{sll.index(2)}"
puts "Add bananas: #{sll.push('bananas')}"
puts "Length should be 11: #{sll.length}"
puts "Remove 3: #{sll.pop(3)}"
puts "Length should be 10: #{sll.length}"
puts "Remove 99 - should be false, not in list: #{sll.pop(99)}"
puts "Bananas should still be at the end: #{sll.at(sll.length - 1).value}"
