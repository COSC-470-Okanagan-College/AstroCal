import AstroCal.view.console_output as console_output
import sys


def run():
    # Runs UI
    #app = view.tkGUI_Launch
    # app.mainloop()

    # Runs Console
    console_output.main_menu()


if __name__ == "__main__":
    # Check for minimum version of Python (3.8)
    MIN_PYTHON = (3, 8)
    if sys.version_info < MIN_PYTHON:
        sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)
    run()
