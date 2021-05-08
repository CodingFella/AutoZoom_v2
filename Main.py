import time
import webbrowser
import pyautogui
from pywinauto import Desktop


def get_participants():
    windows = Desktop(backend="uia").windows()
    temp = ""
    for w in windows:
        if "Participants (" in w.window_text():
            for char in w.window_text():
                if char.isnumeric():
                    temp += char
            return temp
    return -1


def leave():
    pyautogui.hotkey('alt', 'q')
    time.sleep(0.5)
    pyautogui.click(963, 517)


num_lines = sum(1 for line in open('schedule.txt')) - 1

name = [None] * num_lines
day = [None] * num_lines
join_time = [None] * num_lines
link = [None] * num_lines

file = open("schedule.txt", "r")
file.readline()

for x in range(num_lines):
    my_list = file.readline().split()
    name[x] = my_list[0]
    day[x] = my_list[1]
    join_time[x] = my_list[2]
    link[x] = my_list[3]

file.close()

for index, x in enumerate(name):
    print("Loaded: " + str(name[index]) + " " + str(day[index]) + " " + str(join_time[index]) + " " + str(link[index]))

while True:
    curr_day = time.strftime("%a")
    curr_time = time.strftime("%H:%M:%S")
    for index, times in enumerate(join_time):
        if times == curr_time and curr_day == day[index]:
            webbrowser.open(str(link[index]))
            print("Joining " + str(name[index]) + ". Current time: " + str(curr_time))
            time.sleep(1)
    if 15 > int(get_participants()) > 0:
        leave()
    time.sleep(1)
