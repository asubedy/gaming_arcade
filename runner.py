#!/usr/bin/python3
import rock_paper_scissors
import pinpong
import spaceGame

keep_playing = True
while keep_playing:
    print("\n\n-------------------------------------------------------------------GAMING ARCADE----------------------------------------------------------------------")
    print("\t\t\t\t1. Rock Paper Scisior Lizard Spock")
    print("\t\t\t\t2. Ping Pong")
    print("\t\t\t\t3. Space Invader")
    print("\t\t\t\t4. Quit the arcade")
    choice = input("Enter which game you want to play: ")
    if choice == '1':
        rock_paper_scissors.start_game()
    elif choice == '2':
        pinpong.main_game(0,0)
    elif choice == '3':
        spaceGame.start()
    else:
        keep_playing = False

