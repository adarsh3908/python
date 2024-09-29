from gtts import gTTS
text= input("enter  your text:")
language='en'
speech=gTTS(text=text, lang=language, slow = False)
speech.save("gtts.mp3")
print("Text has been converted to speech and saved as 'gtts.mp3'")