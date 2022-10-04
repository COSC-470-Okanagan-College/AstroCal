import view
import sys

def run():
    hello()
    # print("Sun Rise and Set for Sept, 22")
    # print(control.getRiseSet(2022, 9, 22, 'SUN', 'RISE'))
    # print(control.getRiseSet(2022, 9, 22, 'SUN', 'SET'))

    # print("Moon Rise and Set for Sept, 22")
    # print(control.getRiseSet(2022, 9, 22, 'MOON', 'RISE'))
    # print(control.getRiseSet(2022, 9, 22, 'MOON', 'SET'))
    app = view.home
    app.run()
    #view.createMenu()
    #runs everything
    #app = view.mainApp()
    #app.mainloop()

def hello():
    print("Hello, moon!")


if __name__ == "__main__":
    # Check for minimum version of Python (3.8)
    MIN_PYTHON = (3, 8)
    if sys.version_info < MIN_PYTHON:
        sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)
    run()
