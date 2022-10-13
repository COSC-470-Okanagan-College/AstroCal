import AstroCal.view.console_output as console_output
import sys


def run_TUI():
    # Runs Console
    console_output.main_menu()

def run_GUI():
    # Runs UI
    import AstroCal.view.Calendar_ui as calendar
    import AstroCal.view.home as home
    calendar.CalendarApp().run()






if __name__ == "__main__":
    # Check for minimum version of Python (3.8)
    MIN_PYTHON = (3, 8)
    if sys.version_info < MIN_PYTHON:
        sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)
    run_TUI()
