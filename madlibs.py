import gTTS

tts = gTTS('hello')

tts.save('hello.mp3')
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")


madlibs = f"My {noun} and I went out to {verb} food yesterday at {place}, the food was {adjective} but when we got home, we found out the food was {adjective2}"
print(madlibs)
tts = gTTS(text=madlibs, lang='en')
tts.save('madlibs.mp3')
