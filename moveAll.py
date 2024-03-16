import os

currFiles = os.listdir('./')
targetDirImg = 'Images/'
targetDirPaper = 'Papers/'
dontMove = ['README.md', 'Thoughts.md']

for file in currFiles:
    if file.endswith('.png'):
        os.rename(file, targetDirImg+file)
        print(file, 'moved to', targetDirImg+file)
    elif file.endswith('.md') and not file.startswith('Dashboard') and file not in dontMove:
        os.rename(file, targetDirPaper+file)
        print(file, 'moved to', targetDirPaper+file)
print('Done!')