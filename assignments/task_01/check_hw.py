import task_01
import unittest

class CheckHW(unittest.TestCase):


    def testNumber(self):
        self.assertEqual(task_01.number, 7)

    def testOneToTen(self):
        self.assertEqual(task_01.my_list, list(range(1, 11)))

    def testSlice(self):
        self.assertEqual(task_01.easy_as, [1, 2, 3])

    def testReverse(self):
        self.assertEqual(task_01.reverse('hello world'), 'dlrow olleh')
        self.assertEqual(task_01.reverse('racecar'), 'racecar')

    def testIsPalindrome(self):
        self.assertEqual(task_01.is_palindrome('racecar'), True)
        self.assertEqual(task_01.is_palindrome('minivan'), False)

if __name__ == '__main__':
    unittest.main()

