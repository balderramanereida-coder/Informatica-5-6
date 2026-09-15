import time
def main():


    playlist = ["Boston","Dracula","I knwew It, i Knew you","Hate that i made you love me","Risk it all"]
    playlist.append("Be By You")

    playlist.insert(0,"Bohemian Rhapsody")
    print(playlist)

    playlist.pop(4)
    print(playlist)
    print(playlist.index("Rish it all"))
    print("Number of songs in playlist:",len(playlist))
    playlist.reverse()
    print(playlist)

    #challenge
    repet = len(playlist)
    while repeat > 0:
        print(playlist)
        song = playlist[0]
        playlist.append(song)
        repeat -= 1

        time.sleep(3)






if __name__ == "__main__":
    main()
