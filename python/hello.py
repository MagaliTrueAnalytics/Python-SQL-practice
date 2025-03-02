#What is your mood today ? Depending on your feeling, 
# you'll be sayed hello by a cute turtle ... or a angry but encouraging T-REX !
import cowsay

name = input("What is your name? ")

mood = input("What is your mood today? Happy or sad? ")
emotion = mood.lower().strip()

if emotion == "happy":
    print(cowsay.turtle("Hello " + name + " you look great today!"))
elif emotion == "sad":
    print(cowsay.trex("Hello " + name + " don't worry, tomorrow will be better!"))