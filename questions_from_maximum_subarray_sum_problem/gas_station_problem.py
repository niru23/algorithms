#!/usr/bin/python

import unittest
import sys
'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.


Solution
This is basically the maximum subarray sum problem. On the other hand, we can look at it from somewhat different POV. Let us find out where will we have the most deficiency in the fuel if we start the journey from the very first gas station. Since we know that reaching this point shall take the most of the fuel, we can conclude that the truck has to start at this point to minimize the negative fuell balance. Below is the solution with the driver program with O(N) time and O(1) space complexity and there is no need for any DP, since everything is done in a single pass and using only two integers to store the start point index and its value (though this is needed only for printing purposes).


check http://stackoverflow.com/questions/2286849/algorithm-for-truck-moving-around-a-circle-of-gas-stations
'''


def canCompleteCircuit( gas, cost):
    minimum_cost =sys.maxint
    minimum_position =-1
    costnow =0
    minimum_cost =sys.maxint
    minimum_position =-1
    costnow =0
    for i in range(len(gas)):
            costnow+= gas[i]-cost[i]
            if costnow <minimum_cost:
                minimum_cost =costnow
                minimum_position =i
    if costnow >=0:
           return (minimum_position+1)%len(gas)
    else:
            return -1    


class Test(unittest.TestCase):
      data =[([1,1,3,1],[2,2,1,1],2)]

      def test_canCompleteCircuit(self):
          for gas,cost,expected in self.data:
              actual =canCompleteCircuit(gas,cost)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()


