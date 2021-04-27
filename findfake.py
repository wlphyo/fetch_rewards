import unittest
# given a scale and 9 gold bar and exact looks
# bars = number of bars needed to weigh to find the fake.
# start = starting gold to measure
# end = ending gold to measure
def findFake(bars, start, end):
    if (end - start) == 0:
        return start + 1
    odd_bar = -1 
    # if bars is odd numbers, there are 9 gold bars to weigh.
    # keep track of one of the gold bar
    if ((end - start) % 2 != 0):
        odd_bar = end
        end = end - 1
    # find mid point to divide and conqueror
    mid = ((end - start + 1) // 2) + start
    sum_left = 0
    sum_right = 0
    # add the left plate
    for left in range(start, mid):
        sum_left += bars[left]
    # add the right plate
    for right in range(mid , end):
        sum_right += bars[right]
    # scale
    # if scale weigh the same, the odd_bar is fake
    # other wise check left pile or right pile
    if sum_left == sum_right:
        return odd_bar
    if sum_left < sum_right:
        return findFake(bars, start, mid)
    if sum_left > sum_right:
        return findFake(bars, mid , end)

# There are only 9 bars. 
# Tests created for each individual bars
class fakeTest(unittest.TestCase):
    def test_one(self):
        bars_one = [1,2,2,2,2,2,2,2,2] # answer = 1
        self.assertEqual(1, findFake(bars_one, 0, 9))
    def test_two(self):
        bars_one = [2,1,2,2,2,2,2,2,2] # answer = 2
        self.assertEqual(2, findFake(bars_one, 0, 9))
    def test_three(self):
        bars_one = [2,2,1,2,2,2,2,2,2] # answer = 3
        self.assertEqual(3, findFake(bars_one, 0, 9))
    def test_four(self):
        bars_one = [2,2,2,1,2,2,2,2,2] # answer = 4
        self.assertEqual(4, findFake(bars_one, 0, 9))
    def test_five(self):
        bars_one = [2,2,2,2,1,2,2,2,2] # answer = 5
        self.assertEqual(5, findFake(bars_one, 0, 9))
    def test_six(self):
        bars_one = [2,2,2,2,2,1,2,2,2] # answer = 6
        self.assertEqual(6, findFake(bars_one, 0, 9))
    def test_seven(self):
        bars_one = [2,2,2,2,2,2,1,2,2] # answer = 7
        self.assertEqual(7, findFake(bars_one, 0, 9))
    def test_eight(self):
        bars_one = [2,2,2,2,2,2,2,1,2] # answer = 8
        self.assertEqual(8, findFake(bars_one, 0, 9))
    def test_nine(self):
        bars_one = [2,2,2,2,2,2,2,2,1] # answer = 9
        self.assertEqual(9, findFake(bars_one, 0, 9))

if __name__ == '__main__':
    unittest.main()

