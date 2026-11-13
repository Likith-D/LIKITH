import unittest

def add(a , b) :
  return a + b
  
def subtract (a,b):
  return a-b

def multiply(a, b):
  return a * b
  
class TestCalculator(unittest.TestCase):

def test_add(self):
  self.assertEqual(subtract(20,10),10)

def test_multiply(self):
  self.assertEqual(multiply(6,4),24)
  
