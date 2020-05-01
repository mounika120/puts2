import main
import unittest

class CalculatorTesting(unittest.TestCase):

    def SubtractionInteger(self):
        num1 =  self.app.get('/sub?A=8&B=1')
        self.assertEqual(b'7 \n', arg1.data)
        self.assertNotEqual(b'9 \n',arg1.data)
    def SubtractionFloat(self):
        num2 =  self.app.get('/sub?A=8.3&B=2.3')
        self.assertEqual(b'6 \n', arg2.data)
        self.assertNotEqual(b'5.2 \n',arg2.data)
    def SubtractionFraction(self):
        num3 =  self.app.get('/sub?A=1/2&B=1/2')
        self.assertEqual(b'0 \n', arg3.data)
        self.assertNotEqual(b'3 \n',arg3.data)
    def SubtractionNegative(self):
        num4=  self.app.get('/sub?A=8.2&B=-1.8')
        self.assertEqual(b'10 \n', arg4.data)
        self.assertNotEqual(b'8 \n',arg4.data)
		
    
         
         
if __name__ == '__main__':
    unittest.main()