from ctypes.wintypes import HDC
from pynput.mouse import Button, Controller
import time
import random
from AppKit import NSWorkspace
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()

from screen_capture import ScreenPixel

# spheres = ""

# promptList = []

# index = 0

# for i in spheres.split("\n"):
#     if len(i) > 2:
#         promptList.append(i)

prompts = ["<|endoftext|> --stylize 625 --chaos 100", "<|endoftext|> --chaos 100", "<|endoftext|> --stylize 1250 --chaos 100 --testp", "<|endoftext|> --stylize 1250 --chaos 100 --testp", "<|endoftext|> --stylize 625 --chaos 100 --hd", "<|endoftext|> --stylize 625 --chaos 100 --q 0.25"]

sp = ScreenPixel()

def check_queue():
    sp.capture()
    result = sp.pixel(424, 682)
    
    print(result)
    if result == (228, 195, 122, 255):
        return "yellow"
    elif result == (223, 49, 33, 255):
        return "red"
    elif result == (234, 51, 35, 255):
        return "red"
    elif result == (240, 205, 128, 255):
        return "yellow"
    else:
        return "white"

def write_next_prompt():
    wait_for_discord()
    prompt = prompts[random.randint(0,5)]
    # global index
    # if index > len(promptList) -1:
    #     print("Done")
    #     exit()

    mouse.position = (561.0625, 797.4492187)
    mouse.click(Button.left, 1)
    time.sleep(0.2)
    keyboard.type("/imagine")
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.type(prompt)
    # index += 1
    time.sleep(0.5)
    keyboard.press(Key.enter)
    time.sleep(30)

def wait_for_discord():
    if NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'] != "Discord":
        print("Waiting for discord...")
        while NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'] != "Discord":
            time.sleep(5)

def save_index():
    print()
    # global index
    # file = open("index.txt", "w")
    # file.write(str(index))
    # file.close()

def read_index():
    print()
    # global index
    # file = open("index.txt", "r")
    # index = int(file.read())
    # file.close()

#main loop
# read_index()
while True:
    wait_for_discord()
    queue = check_queue()
    #print(queue)
    if queue == "red":
        # index -= 1
        # save_index()
        print(f"Retrying in 1 minutes: " + promptList[index])
        time.sleep(60)
    elif queue == "yellow":
        print("Retrying in 2 seconds: " + promptList[index])
        time.sleep(2)
    # print(index)
    # save_index()
    # print("Left: " + str(len(promptList) - index))
    # print("Next: " + promptList[index])
    write_next_prompt()
    