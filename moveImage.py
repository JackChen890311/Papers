import os

currFiles = os.listdir('./')
targetDir = 'imgs/'

for file in currFiles:
    if file.endswith('.png'):
        os.rename(file, targetDir+file)
        print(file, 'moved to', targetDir+file)