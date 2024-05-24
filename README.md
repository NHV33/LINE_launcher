### Description
This is simple Python script to automatically launch the Chrome extension for the LINE chat application using the PyAutoGUI library.
I created this because LINE does not have a desktop client for Linux, so launching LINE required having to open my browser, click on a tiny icon to launch the extension, then click over to the password input field; which was very tedious.

### Usage
You will need to have PyAutoGUI and OpenCV installed to use this script:

`pip install pyautogui`

`pip install opencv-python`

If you are using some variant of Ubuntu Linux and have the Brave browser installed, you should be able to simply download the repo and click on the icon to run the script, or run it via terminal like so:

`python3 path/to/the/file/on/your/computer/launcher.py`

If you are using a different browser than Brave, or the GUI scaling is different on your OS,
then you may have to take a new screenshot of the LINE icon as it appears on your computer
and save it to the project directory as 'line_icon.png'

In Linux Mint you can trigger the script via a hotkey as shown below:
![Screenshot from 2024-05-24 15-21-38](https://github.com/NHV33/LINE_launcher/assets/145536545/ef679ff3-a628-4f36-a998-ad4c0432cc01)
