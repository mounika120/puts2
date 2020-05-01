import main
import unittest

class CalculatorTesting(unittest.TestCase):

    def MultiplicationInteger(self):
        num1=  self.app.get('/mul?A=8&B=8')
        self.assertEqual(b'64 \n', arg1.data)
        self.assertNotEqual(b'8 \n',arg1.data)
    def MultiplicationFloat(self):
        num2 =  self.app.get('/mul?A=3.8&B=6.2')
        self.assertEqual(b'23.56 \n', arg2.data)
        self.assertNotEqual(b'22 \n',arg2.data)
    def MulFraction(self):
        num3 =  self.app.get('/mul?A=1/4&B=8/3')
        self.assertEqual(b'0.66 \n', arg3.data)
        self.assertNotEqual(b'0.87 \n',arg3.data)
    def MultiplicationNegative(self):
        num4=  self.app.get('/mul?A=7&B=-7')
        self.assertEqual(b'-49 \n', arg4.data)
        self.assertNotEqual(b'10.000 \n',arg4.data)
		
    
         
         
if __name__ == '__main__':
    unittest.main()