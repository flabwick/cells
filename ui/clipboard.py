import sys
import subprocess

def copy(text):
    plat = sys.platform
    try:
        if plat == "win32":
            p = subprocess.Popen(['clip'], stdin=subprocess.PIPE)
            p.communicate(text.encode('utf-8'))
        elif plat == "darwin":
            p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            p.communicate(text.encode('utf-8'))
        else:
            p = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
            p.communicate(text.encode('utf-8'))
    except Exception:
        print("\n--- Copied Text ---\n")
        print(text)
        print("\n-------------------\n")
