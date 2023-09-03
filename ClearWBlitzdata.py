#deepmeanx
import os
import ctypes
import shutil

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def donefile(gamedata_path):
    print('!Attention! All user data of the game will be DELETED ON THIS SYSTEM, including replays, automatic session and graphics settings (reset to silence.)')
    print('You are sure?')
    input()
    try:
        shutil.rmtree(gamedata_path)
        print('Done. All game data has been deleted.')
        input()
    except Exception as e:
        print('An error occurred while deleting the game data:', e)

def main():
    if is_admin():
        ctypes.windll.kernel32.SetConsoleTitleW("Clear WBlitz data")
        print('This program will help to clear the data of the PC version of the game WoT Blitz or Tanks Blitz')
        print('Press any key to continue')
        input()
        gamedata_path = os.path.expanduser("~/Documents/DAVAProject")
    
        if os.path.exists(gamedata_path):
            print('Game files found')
            donefile(gamedata_path)
        else:
            print(gamedata_path)
            print('The game files are not found')
            input()
            exit()
    else:
        print("Please, run this program as administrator")
        exit()

main()
