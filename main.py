# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from appium import webdriver
from os import path
APPIUM = 'http://127.0.0.1:4723/wd/hub'
CAPS = { 'platformName': 'Android',
'udid': 'K6M3051112B0021', 'automationName': 'UiAutomator2', }
driver = webdriver.Remote(APPIUM, CAPS)
driver.quit()