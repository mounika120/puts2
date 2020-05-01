import main
import unittest

class CalculatorTesting(unittest.TestCase):

    def DivisionInteger(self):
        num1=  self.app.get('/div?A=10&B=3')
        self.assertEqual(b'3.3 \n', arg1.data)
        self.assertNotEqual(b'7 \n',arg1.data)
    def DivisionFloat(self):
        num2=  self.app.get('/div?A=5.9&B=2.3')
        self.assertEqual(b'2.56 \n', arg2.data)
        self.assertNotEqual(b'6 \n',arg2.data)
    def DivisionFraction(self):
        num3=  self.app.get('/div?A=1/4&B=8/3')
        self.assertEqual(b'0.093 \n', arg3.data)
        self.assertNotEqual(b'1 \n',arg3.data)
    def DivisionNegative(self):
        num4=  self.app.get('/div?A=8&B=-2')
        self.assertEqual(b'-4 \n', arg4.data)
        self.assertNotEqual(b'4 \n',arg4.data)
		
    
         
         
if __name__ == '__main__':
    unittest.main()