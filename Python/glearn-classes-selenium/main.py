from gLearn import getClasses
from getpass import getpass
from pprint import pprint
from operator import itemgetter

pinNumber = input("Enter PIN Number: ")
password = getpass("Enter Password: ")


classList = sorted(getClasses(pinNumber, password), key=itemgetter('date'))

pprint(classList)
