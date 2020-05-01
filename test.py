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