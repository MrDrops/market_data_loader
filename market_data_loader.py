import os
import shutil
import subprocess
import re
import win32gui
import time
import pyautogui
import winsound

"""
goal of this script is to automatically open MT5, download all market
data files for each chart and save it into my predetermined folder
by using elements learned in automate the boring stuff with python book

INSTRUCTIONS: Run script and allow for a few minutes not touching mouse or keyboard
so that pyautogui can take control of mouse and desktop until it copies all files
will sound a bell when done

modifiable variables
allPairs - can be majors, minors, the default: minors+majors
If you want any other subgroup just create the dictionary

open mt5
open each chart and select daily timeframe
save chart data in correct folder
Overwrite previous data if needed to update
return a message confirming success

requirements:
file management
mouse automation
keyboard automation
gui identification
gui automation
"""
start = time.time()

def clearFolder(desiredPath):
    """
    checks if there are older chart files in desiredPath and erases them if True
    """
    if os.listdir(desiredPath) != None:
        for fileName in os.listdir(desiredPath):
            try:
                os.remove((desiredPath + '\\' + fileName))
            except:
                continue # handles directories

sourceChartPath = r'C:\Users\Drops\Documents\Trading_Files\chart_data_files'
clearFolder(sourceChartPath)
        
#should open mt5 and have it on screen
subprocess.Popen("C:\\Program Files\\ICMarkets - MetaTrader 5\\terminal64.exe")
time.sleep(3)
os.chdir('C:\\Users\\Drops\\Documents\\Trading_Files\\code_images\\')
#timeframes = {'1h' : '1h.png', '4h' : '4h.png', '1d' : '1d.png', '1w' : '1w.png'}
timeframes = ['o', '4', 'd', 'w'] # hour, 4 hour, day, week
majors = {'eurusd': 'eurusd.png', 'usdchf': 'usdchf.png', 'gbpusd': 'gbpusd.png',
    'usdjpy': 'usdjpy.png', 'usdcad': 'usdcad.png', 'audusd': 'audusd.png'}
minors = {'audjpy': 'audjpy.png', 'eurgbp': 'eurgbp.png', 'eurnzd': 'eurnzd.png', 'gbpcad': 'gbpcad.png',
    'gbpchf': 'gbpchf.png', 'nzdjpy': 'nzdjpy.png', 'nzdusd': 'nzdusd.png', 'gbpaud': 'gbpaud.png',
    'audchf': 'audchf.png', 'audnzd': 'audnzd.png', 'audcad': 'audcad.png', 'chfjpy': 'chfjpy.png',
    'euraud': 'euraud.png', 'eurchf': 'eurchf.png', 'eurjpy': 'eurjpy.png', 'eurcad': 'eurcad.png',
    'gbpjpy': 'gbpjpy.png', 'cadchf': 'cadchf.png', 'cadjpy': 'cadjpy.png', 'gbpnzd': 'gbpnzd.png',
    'nzdcad': 'nzdcad.png', 'nzdchf': 'nzdchf.png', 'usdsgd': 'usdsgd.png'}
dicList = [majors, minors]
#majors.update(minors) #for all pairs

#WARNING: ATM save folder in MT5 must be the desired forlder, it will save in whatever folder is set to
for dic in dicList:
    print(dic)
    for picFile in dic.values():
        # Open chart
        pyautogui.hotkey('alt', 'f')
        pyautogui.press('n')
        pyautogui.press('f')
        # choose pair chart
        time.sleep(0.2)
        majOrMin = None
        if picFile in majors.values():
            majOrMin = pyautogui.locateCenterOnScreen('majorButton.png')
        else:
            majOrMin = pyautogui.locateCenterOnScreen('minorButton.png')
        pyautogui.click(majOrMin)
        time.sleep(0.5)
        clickloc = pyautogui.locateCenterOnScreen(picFile)
        time.sleep(0.5)
        if clickloc == None:
            break
        pyautogui.click(clickloc)
        time.sleep(0.5)
        # save pair chart for every timeframe (1h, 4h, day, week)
        for tf in timeframes:
            pyautogui.hotkey('alt', 'c')
            pyautogui.press('f')
            pyautogui.press(tf)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(0.5)
            pyautogui.press('\n')
            time.sleep(0.5)
        # close chart
        pyautogui.hotkey('ctrl', 'f4')
        time.sleep(0.5)

# #After downloading all files, it will move them to their respective folder
# os.chdir(r'C:\Users\Drops\Documents\Trading_Files\chart_data_files')
# sourceChartPath = r'C:\Users\Drops\Documents\Trading_Files\chart_data_files'
# oneHRe = re.compile(r'\w+H1.csv')
# fourHRe = re.compile(r'\w+H4.csv')
# dayRe = re.compile(r'\w+Daily.csv')
# weekRe = re.compile(r'\w+Weekly.csv')
# chartPath = r'C:\Users\Drops\Documents\Trading_Files\chart_data_files'
# oneHPath = r'C:\Users\Drops\Documents\Trading_Files\chart_data_files\1h_charts'
# fourHPath = r'C:\Users\Drops\Documents\Trading_Files\chart_data_files\4h_charts'
# dayPath = r'C:\Users\Drops\Documents\Trading_Files\chart_data_files\1d_charts'
# weekPath = r'C:\Users\Drops\Documents\Trading_Files\chart_data_files\1w_charts'
# allTimeFrames = [oneHRe, fourHRe, dayRe, weekRe]
# pathTfList = [oneHPath, fourHPath, dayPath, weekPath]
# #check if folders are full if true erase them
# for tfPath in pathTfList:
#      clearFolder(tfPath)
# #textList = os.listdir(chartPath)
# for chrtFile in os.listdir(chartPath):
#     for i in range(len(allTimeFrames)):
#         match = re.search(allTimeFrames[i], chrtFile)
#         if match:
#             joinPath = sourceChartPath + '\\' + chrtFile
#             if i == 0:
#                 #copy to 1 hour folder
#                 shutil.move(joinPath, oneHPath)
#                 break
#             elif i == 1:
#                 #copy to 4h folder
#                 shutil.move(joinPath, fourHPath)
#                 break
#             elif i == 2:
#                 #copy to 1d folder
#                 shutil.move(joinPath, dayPath)
#                 break
#             else:
#                 #copy to week folder
#                 shutil.move(joinPath, weekPath)
#                 break

# times the operation
end = time.time()
print(end - start)
# Alarm when process finishes
duration = 500 # milliseconds
freq = 440 # Hz
winsound.Beep(freq, duration)
winsound.Beep(freq, duration)
winsound.Beep(freq, duration)
print('end')
