
import logging
#logging.basicConfig(filename='sample.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero not possible")
    else:
        return x / y

num1 = 10
num2 = 5
add_result = add(num1, num2)
logger.info('{} + {} = {}'.format(num1, num2, add_result))

sub_result = sub(num1, num2)
logger.info('{} - {} = {}'.format(num1, num2, sub_result))

mul_result = multiply(num1, num2)
logger.info('{} * {} = {}'.format(num1, num2, mul_result))

div_result = division(num1, num2)
logger.info('{} / {} = {}'.format(num1, num2, div_result))
