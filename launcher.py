import pyautogui as pag
import os, sys, cv2, time


# Increase this number if the LINE extension takes longer than one second to load
extension_load_time = 1

'''
Depending on your browser and the scale setting for your
operating system, the LINE icon may appear differently,
so take a screenshot of the icon as it appears in your
browser, crop it, and save it to this directory with the
name "line_icon.png"
'''

script_dir = os.path.dirname(os.path.realpath(__file__))

img_path = os.path.join(script_dir, "line_icon.png")

'''
Replace os.popen with a function that opens your Chromium
browser of choice on your favorite prefered OS.
'''

# Launch Brave browser on Ubuntu linux
os.popen("/usr/bin/brave-browser-stable %U")

icon_pos = None
start_time = time.time()

while (time.time() - start_time) < 3:
    try:
        print("Attempting to locate LINE icon...")
        icon_pos = pag.locateCenterOnScreen(img_path, confidence=0.9)
        if icon_pos:
            break

    except:
        time.sleep(.5)


if icon_pos:
    pag.moveTo(icon_pos)

    pag.click()

    time.sleep(extension_load_time)

    #focus selection on the Password input field by pressing tab key twice
    pag.press(["\t", "\t"])

else:
    print("Was unable to detect the LINE icon on screen.")
