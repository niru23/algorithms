#!/usr/bin/python

'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.

logic sort the array. Use a dictionary to get pair sums
Then use a nested for-loop to search, num[i] is the min number in quadruplet and num[j] is the second min number. The time complexity of checking whether d has the key target - num[i] - num[j] is O(1). If this key exists, add one quadruplet to the result. Use set() to remove duplicates in res, otherwise for input [-3,-2,-1,0,0,1,2,3], 0 there will be two [-3, 0, 1, 2] and two [-2, -1, 0, 3].
'''
