#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  if len(s)>=3:
    if s[-3] == "i" and s[-2] == "n" and s[-1] == "g":
      s = s + "ly"
    else:
      s = s + "ing"
  else:
    pass
  return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  new_string = ""
  found_not = False
  found_bad = False
  for x in range(len(s)):
    if s[x] == "n" and s[x+1] == "o" and s[x+2] == "t":
      n_index = x
      found_not = True
      break
  for y in range(len(s)):
    if s[y] == "b" and s[y+1] == "a" and s[y+2] == "d":
      b_index = y
      found_bad = True
  if found_not == True and found_bad == True and n_index<b_index:
    for a in range(0, n_index):
      new_string = new_string + s[a]
    new_string = new_string + "good"
    for b in range(b_index+3, len(s)):
      new_string = new_string + s[b]
    return new_string
  else:
    return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  front = ""
  back = ""
  if len(a)//2 == 0:
    for x in range(len(a)/2):
      front = front + a[x]
    for y in range(len(a)/2, len(a)):
      back = back + a[y]
  elif len(a)//2 != 0:
    halfaroundup = int((len(a)/2)+.5)
    for x in range(halfaroundup):
      front = front + a[x]
    for y in range(halfaroundup, len(a)):
      back = back + a[y]
      
  if len(b)//2 == 0:
    for z in range(0, len(b)/2):
      front = front + b[z]
    for n in range(len(b)/2, len(b)):
      back = back + b[n]
  elif len(b)//2 != 0:
    halfbroundup = int((len(b)/2)+.5)
    for z in range(halfbroundup):
      front = front + b[z]
    for n in range(halfbroundup, len(b)):
      back = back + b[n]
  return front + back


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
