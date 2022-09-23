import model
import control
import view


def run():
    hello()
    control.test_swe()
    print(control.getRiseSet(2022, 9, 22, 'SUN', 'RISE'))


def hello():
    print("Hello, moon!")
