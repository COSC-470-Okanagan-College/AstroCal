import AstroCal.view.console_output as console_output
import AstroCal.view.Calendar_ui as calendar
import AstroCal.view.home as home
import sys


def run():
    # Runs day page UI
    # app = home
    # app.run()

    # Runs UI
    calendar.CalendarApp().run()

    # Runs Console
    # console_output.main_menu()




if __name__ == "__main__":
    # Check for minimum version of Python (3.8)
    MIN_PYTHON = (3, 8)
    if sys.version_info < MIN_PYTHON:
        sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)
    run()
