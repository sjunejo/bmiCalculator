#!/usr/bin/env python3
import bmiCalculator
import unittest

class BMICalculatorTest(unittest.TestCase):
    
    known_bmi_values = (("1.8m", "65.6kg", 20.20),("5'9", "159lb", 23.5))
    
    known_weight_classes = ((18.4, "UNDERWEIGHT"), (30, "OBESE"))

    def test_calculate_bmi(self):
        for (height, weight, actual_bmi) in self.known_bmi_values:
            bmi = bmiCalculator.calculate_bmi(height, weight)
            self.assertAlmostEqual(bmi, actual_bmi, 1)

    def test_calculate_weight_classes(self):
        for (bmi, actual_weight_class) in self.known_weight_classes:
            weight_class = bmiCalculator.determine_weight_class(bmi)
            self.assertEqual(weight_class, actual_weight_class)
        
        
if __name__ == '__main__':
    unittest.main()
        

        
        
        
