import os
import sys

PATH = r'C:\Users\1\Desktop\Питон\pygame\Party_with_Patty'

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(PATH, relative)
