{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'calculator' from 'calc' (d:\\Muthu\\machine learning\\unittesting\\calc.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01munittest\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mcalc\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m calculator\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mTestCalc\u001b[39;00m(unittest\u001b[38;5;241m.\u001b[39mTestCase):\n\u001b[0;32m      5\u001b[0m     \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mtest_add\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n",
      "\u001b[1;31mImportError\u001b[0m: cannot import name 'calculator' from 'calc' (d:\\Muthu\\machine learning\\unittesting\\calc.py)"
     ]
    }
   ],
   "source": [
    "import unittest\n",
    "from calc import calculator\n",
    "\n",
    "class TestCalc(unittest.TestCase):\n",
    "    def test_add(self):\n",
    "        calc = calculator()\n",
    "        result = calc.add(10, 5)\n",
    "        self.assertEqual(result, 15)\n",
    "\n",
    "    def test_sub(self):\n",
    "        calc = calculator()\n",
    "        result = calc.sub(10, 5)\n",
    "        self.assertEqual(result, 5)\n",
    "\n",
    "    def test_multiply(self):\n",
    "        calc = calculator()\n",
    "        result = calc.multiply(10, 5)\n",
    "        self.assertEqual(result, 50)\n",
    "\n",
    "    def test_division(self):\n",
    "        calc = calculator()\n",
    "        result = calc.division(10, 5)\n",
    "        self.assertEqual(result, 2)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    unittest.main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
