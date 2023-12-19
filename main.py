import pyautogui as pa
import datetime as dt
import threading

def inputChecker():
    # Create a thread to run the main loop
    thread = threading.Thread(target=mouseMover)
    thread.start()

    # Wait for enter key to be pressed
    input()

    # Set the flag to stop the main loop
    global running
    running = False

    # Wait for the main loop to finish
    thread.join()
    print("\033[Fkeep_awake stopped.")

def mouseMover():
    startMoveTime = dt.datetime.now()
    endMoveTime = startMoveTime + dt.timedelta(minutes=4, seconds=30)
    # endMoveTime = startMoveTime + dt.timedelta(seconds=1)
    global running
    running = True
    sign = -1
    while running:
        secondsDifference = round((dt.datetime.now() - endMoveTime).total_seconds())
        if secondsDifference == 0:
            pa.moveRel(0, sign * 1)
            sign = sign * -1
            startMoveTime = endMoveTime
            endMoveTime = startMoveTime + dt.timedelta(minutes=4, seconds=30)
            # endMoveTime = startMoveTime + dt.timedelta(seconds=1)
            roundedTime = startMoveTime.replace(microsecond=0)
            print(f'Mouse moved at {roundedTime}.')

if __name__ == '__main__':
    print('keep_awake has started.')
    print('Press enter to stop')
    inputChecker()
