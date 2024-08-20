# uncomment if you have copied the git repo instead of installing the package and copying the file
#import sys; import os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import PySoundSphere

player = PySoundSphere.AudioPlayer("sounddevice")
player.volume = 0.025
state = None

while True:
    print("1) Play song")
    print("2) Pause song")
    print("3) Stop song")
    print("4) Set volume")
    print("5) Set position")
    print("6) Exit")

    try:
        choice = int(input(":"))
    except ValueError:
        print("Invalid input")
        continue

    if choice == 1:
        if state == "Paused":
            player.play()
            state = "Paused"
        elif state == "Playing":
            print("Already playing")
        else:
            print("Enter path to song")
            path = input(":")
            player.load(path)
            player.play()
            state = "Playing"
    elif choice == 2:
        player.pause()
        state = "Paused"
    elif choice == 3:
        player.stop()
        state = None
    elif choice == 4:
        print("Enter volume")
        try:
            vol = float(input(":"))
        except ValueError:
            print("Invalid input")
            continue
        player.volume = vol
    elif choice == 5:
        print("Enter position (in seconds)")
        try:
            pos = int(input(":"))
        except ValueError:
            print("Invalid input")
            continue
        player.position = pos
    elif choice == 6:
        break
