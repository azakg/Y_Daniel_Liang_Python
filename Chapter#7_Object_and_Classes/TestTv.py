from TV import TV

def main():
    tv = TV()
    tv.turnOn()
    tv.setChannel(20)
    tv.setVolume(3)


    tv2 = TV()
    tv2.turnOn()
    tv2.setChannel(10)
    tv2.setVolume(5)

    print(f"The tv channel is {tv.getChannel()}")
    print(f"The tv2 channel is {tv2.getChannel()}")

main()