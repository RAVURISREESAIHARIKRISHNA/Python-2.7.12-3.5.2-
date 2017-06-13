import pyautogui,sys,time
print("CTRL + C to Stop...\nTHis Program Initializes in 5sec..")
time.sleep(5)
while True:
    try:
        print(pyautogui.position())
    except KeyboardInterrupt:
        sys.exit(0)
