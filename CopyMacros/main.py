from time import sleep

import keyboard as kb
import pyperclip as clip

def paste():
    global stringToType
    sleep(0.1)
    stringToType = clip.paste().replace("\r\n", "\n").replace("public:\n\t", "public:\n    ").replace("private:\n\t", "private:\n    ").replace("protected:\n\t", "protected:\n    ").replace("\t", "")
    print("Copied:", repr(stringToType))

def write():
    global stringToType
    print("Typing...")
    kb.write(stringToType, delay=0.1, restore_state_after=False)
    print("Type completed")

stringToType = ""
kb.add_hotkey("ctrl+c", paste)
kb.add_hotkey("ctrl+space", write)
kb.wait("esc")