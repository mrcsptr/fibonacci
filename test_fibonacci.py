# coding: utf-8

import unittest
from fibonacci import *


class MyFirstTests(unittest.TestCase):

	def testFibo1(self):
		self.assertEqual(fibo(5), 5)

	def testMed(self):
		self.assertEqual(fibo(6), 8)







