# Created by Isabella Lemus
# CSV Combiner project for PMG Programming Challenge
# 10/20/2022
#
# This is a class created to test the lemus_CSV.py program.
# This class should test the methods and variables in the CSVCombiner class and return correct.
#
# Currently this testing class does not run due to issues with reading command line arguments.

from lemus_CSV import CSVCombiner
import unittest

class TestCSV(unittest.TestCase):

    def testStoreArgs(self):
       pass

    def testHeader(self):
        c = CSVCombiner()
        c.constructCSV
        self.assertEqual(c.header, ["email_hash","category","filename"], "Header incorrect")

    def testContents(self):
        c = CSVCombiner()
        # Need to enter a CSV file through arguments
        self.assertEqual(c.contents, ["emailhash123","shoes","file.py"], "Contents incorrect")

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

