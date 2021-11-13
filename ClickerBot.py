import pyautogui
import time

def keyboard(delay):
    time.sleep(delay)
    pyautogui.press(['shift', 'shift', 'shift', 'shift', 'shift', 'shift', 'shift', 'shift', 'shift', 'shift'])

def click(delay): 
    time.sleep(delay)     
    pyautogui.click()

def main(clicks=100, delay=0.1, click_or_press='p'):

    global year_start, month_start, day_start, hour_start, minute_start, second_start, weekday_start, yearday_start, daylight_start, start

    print('')
    for i in range(3):
        print(f"Starting in {3-i}...")
        time.sleep(1)
    #time.sleep(1)
    start = time.localtime(time.time())
    year_start, month_start, day_start, hour_start, minute_start, second_start, weekday_start, yearday_start, daylight_start = start
    print("Starting at :", "%02d:%02d:%02d"%(hour_start, minute_start, second_start))
    print('')

    if click_or_press == 'c':
        for i in range(1, clicks+1):
            click(delay=delay)        
            print("press", i)
    else:
        for i in range(1, clicks+1):
            keyboard(delay=delay)        
            print("press", i*10)
       
def bot():
    print('')
    click_or_press = str(input("Do you want to auto-click or to auto-press a key ?\nType 'c' for auto-click, 'p' for auto-press:"))
    if click_or_press not in ('c', 'p'):
        print('')
        print("Invalid command, bot set to auto-press by default")
        click_or_press = 'p'
        print('')

    try:
        delay=float(input("Delay: "))
    except:
        print("Invalid number, delay is set to 0.1")
        delay=0.1

    try:
        if click_or_press == 'p':
            clicks = int(int(input("Number of press: "))/10)
        else:
            clicks = int(input("Number of clicks: "))
    except:
        print("Invalid number, click set to 100 by default")
        if click_or_press == 'p':
            clicks = int(100/10)
        else:
            clicks = 100

    main(clicks=clicks, delay=delay, click_or_press=click_or_press)

if __name__=='__main__':
    start = time.localtime(time.time())
    year_start, month_start, day_start, hour_start, minute_start, second_start, weekday_start, yearday_start, daylight_start = start

    bot()

    finished = time.localtime(time.time())
    year_finished, month_finished, day_finished, hour_finished, minute_finished, second_finished, weekday_finished, yearday_finished, daylight_finished = finished
    print("Finished at :", "%02d:%02d:%02d"%(hour_finished, minute_finished, second_finished))
    print("Duration : ", "%02d:%02d:%02d"%(abs(hour_finished - hour_start), abs(minute_finished - minute_start), abs(second_finished - second_start)))
