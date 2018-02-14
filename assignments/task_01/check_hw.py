import task_01
import unittest

class CheckHW(unittest.TestCase):


    def testNumber(self):
        """number should equal 7"""
        self.assertEqual(task_01.number, 7)

    def testOneToTen(self):
        """my_list should equal [1, 2, 3, ... 10]"""
        self.assertEqual(task_01.my_list, list(range(1, 11)))

    def testSlice(self):
        """easy_as should equal [1, 2, 3]"""
        self.assertEqual(task_01.easy_as, [1, 2, 3])

    def testReverse(self):
        """testReverse(string) should return string in reverse"""
        self.assertEqual(task_01.reverse('hello world'), 'dlrow olleh')
        self.assertEqual(task_01.reverse('racecar'), 'racecar')

    def testIsPalindrome(self):
        """testIsPalindrome(string) should return True if string reads the same both forwards and backwards"""
        self.assertEqual(task_01.is_palindrome('racecar'), True)
        self.assertEqual(task_01.is_palindrome('minivan'), False)

if __name__ == '__main__':
    unittest.main()

