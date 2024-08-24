import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Get list of available voices
voices = engine.getProperty('voices')

# Print available voices
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")

# Choose the desired voice ID (replace 'VoiceID' with the desired ID)
desired_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'

# Set the voice
engine.setProperty('voice', desired_voice_id)

# Test the voice by speaking some text
engine.say("Hello, I am using an external custom female voice.")
engine.runAndWait()
