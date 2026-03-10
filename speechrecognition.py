import speech_recognition as sr

# Create recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak something...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("📝 You said:", text)
except sr.UnknownValueError:
    print("❌ Sorry, I could not understand the audio.")
except sr.RequestError:
    print("⚠️ Could not request results, check your internet.")
