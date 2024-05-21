from Constants import *





def questions():
    print("Which shape is your favorite?")
    time.sleep(0.5)
    print("type in th' # inside th' () next to th' answer,")
    time.sleep(0.5)
    shape=input("Circle(1), Square(2), Triangle(3):")

    print("Choose your element.")
    time.sleep(0.5)
    element=input("Earth(1), Fire(2), Water(3), Air(4):")

    print("How warm do u desire th' atmosphere to be")
    time.sleep(0.5)
    temperature = input("Dawn(1), Day(2), Dusk(3), Night(4):")

    print("Are you bored or stressed, which is th' best enviornment?")
    time.sleep(0.5)
    enviornment = input("Peaceful(1), Civil(2), Mania(3):")

    print("What realm is best?")
    time.sleep(0.5)
    terrain = input("Forest(1), basin(2), archeplago(3):")
    time.sleep(0.5)

    print("U need some shelter?")
    time.sleep(0.5)
    print("choose a layout for your home?")
    time.sleep(0.5)
    base = ("Spacious(1), Tall(2), Fancy(3):")

Q = questions()