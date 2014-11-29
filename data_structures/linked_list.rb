#!/usr/bin/ruby
# Simple singly linked list, 0-indexed
# Making it as ruby array-like as possible

class SinglyLinkedList
  attr_accessor :head

  def initialize
    self.head = Node.new(nil)
  end

  # Iterates over all the elements in the list and can perform any operation on each node
  # Returns last node
  def iterate
    i, prev, current = 0, nil, head
    while(!current.next.nil?) do
      yield(i, prev, current) if block_given? # yield is about 2x faster than block.call
      prev, current = current, current.next
      i += 1
    end
    current || prev
  end

  # Returns string representation of values, assuming value has to_s method on it
  def to_s
    vals = ''
    iterate do |i, prev, current|
      vals += ', ' unless prev.nil?
      vals += Pretty.pp(current.value)
    end
    "[#{vals}]"
  end

  # Get the current length of the list. O(n)
  def length
    # Remember, iterate stops calling on the block at the last node with a value
    return 0 if head.next.nil?
    iterate do |i, p, c|
      return i + 1 if c.next.next.nil?
    end
  end

  # Retreive last node
  def tail
    iterate
  end

  # Returns value at given index
  def at(index)
    iterate do |i, prev, current|
      return current.value if i == index
    end
    nil
  end

  # Returns index of given value (-1 if not contained)
  def index(value)
    iterate do |i, prev, current|
      return i if current.value == value
    end
    -1
  end
  
  # Append an element to the tail of the list, and returns representation of list. O(n)
  def push(value)
    t = tail
    t.value = value
    t.next = Node.new
    to_s
  end

  # Deletes value from list. If in list, return true, otherwise false
  def delete(value)
    val = nil
    iterate do |i, prev, current|
      if current.value == value
        if prev.nil? # we are at head
          val = head.value
          self.head = current.next
          return '[' + Pretty.pp(val) + ']'
        else
          val = current.value
          # Assume GC will take care of orphaned node
          prev.next = current.next
          return '[' + Pretty.pp(val) + ']'
        end
      end
    end
    nil
  end

  # Removes last element, nil if none
  def pop
    iterate do |i, prev, current|
      if current.next.value.nil?
        prev.next = Node.new
        return '[' + Pretty.pp(current.value) + ']'
      end
    end
    nil
  end

  # Removes first element, nil if none
  def shift
    val = head.value
    return nil if val.nil?
    self.head = head.next
    '[' + Pretty.pp(val) + ']'
  end
end

class Node
  attr_accessor :value, :next

  def initialize(value = nil)
    self.value, self.next = value, nil
  end
end

class Pretty
  # Pretty print a value
  def self.pp(val)
    if val.is_a?(Integer)
      val.to_s
    else
      '"' + val.to_s + '"'
    end
  end
end


# Initialize List
sll = SinglyLinkedList.new
puts "Initialize list"
puts "Length: #{sll.length}"
puts "Add 1..10"
1.upto(10).each{|i| sll.push(i) }
puts "List looks like: #{sll.to_s}"
puts "Head value: #{sll.head.value}"
puts "Tail value should be empty: #{sll.tail.value.nil?}"
len = sll.length
puts "Length: #{len}"
midpoint = (len / 2).floor
puts "Value at midpoint of #{midpoint}: #{sll.at(midpoint - 1)}"
puts "Index of 2: #{sll.index(2)}"
puts "Index of 99 (should not exist): #{sll.index(99)}"
puts "Add bananas: #{sll.push('bananas')}"
puts "Length should be 11: #{sll.length}"
puts "Remove 3: #{sll.delete(3)}"
puts "Length should be 10: #{sll.length}"
puts "Remove 99 - should be nil, not in list: #{sll.delete(99).nil?}"
puts "Bananas should still be at the end: #{sll.at(sll.length - 2)}"
puts "Pop bananas: #{sll.pop}"
puts "Last value is now: #{sll.at(sll.length - 2)}"
puts "Head element is: #{sll.head.value}"
puts "Shift should remove head element: #{sll.shift}"
puts "Head element is now: #{sll.head.value}"
