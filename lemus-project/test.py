# Created by Isabella Lemus
# CSV Combiner project for PMG Programming Challenge
# 10/20/2022
#
# This is a class created to test the lemus_CSV.py program.
# This class should test all methods in the CSVCombiner class and return correct.
#
# Currently this testing class does not run due to issues with taking command line arguments.

from lemus_CSV import CSVCombiner
import unittest

class TestCSV(unittest.TestCase):
    def testCheckOrder(self):
        right = "category"
        wrong = "notCategory"
        c = CSVCombiner()
        self.assertEqual(c.checkOrder(right), True, "Check order incorrect, type 1")
        self.assertEqual(c.checkOrder(wrong), False, "Check order incorrect, type 2")
    def testGetFileName(self):
        c = CSVCombiner()
        file = c.getFileName("./newPath/directory/file.py")
        self.assertEqual(file, "file.py", "Incorrect file name")

