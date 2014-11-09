#!/usr/bin/env python3
import bmiCalculator
import unittest

class BMICalculatorTest(unittest.TestCase):
    
    known_values = (("1.8m", "65.6kg", 20.20))
    
    def setUp(self):
        return
    
    def test_calculate_bmi(self):
        for height, weight, actual_bmi in self.known_values:
            bmi = bmiCalculator.calculate_bmi(height, weight)
            self.assertAlmostEqual(bmi, actual_bmi)
        
        
        
if __name__ == '__main__':
    unittest.main()
        

        
        
        
