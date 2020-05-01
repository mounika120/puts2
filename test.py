import main
import unittest

class CalculatorTesting(unittest.TestCase):

    def mainFunction(self):
        main.app.testing = True
        self.app = main.app.ClientCalculator()


    def AdditionInteger(self):
        num1 = self.app.get('/add?A=1&B=2')
        self.assertEqual(b'3 \n', arg1.data)
        self.assertNotEqual(b'5\n',arg1.data)
    def AdditionFloat(self):
        num2 =  self.app.get('/add?A=1.1&B=1.2')       
        self.assertEqual(b'2.3 \n', arg2.data)
        self.assertNotEqual(b'5.7 \n',arg2.data)
    def AdditionFraction(self):
        num3 =  self.app.get('/add?A=1/2&B=1/2')
        self.assertEqual(b'1 \n', arg3.data)
        self.assertNotEqual(b'8.7 \n',arg3.data)
    def AdditionNegative(self):
        num4=  self.app.get('/add?A=5&B=-1.3')
        self.assertEqual(b'3.7 \n', arg4.data)
        self.assertNotEqual(b'-2 \n',arg4.data)
		
    
         
         
if __name__ == '__main__':
    unittest.main()