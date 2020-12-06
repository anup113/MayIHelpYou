"""Google Cloud Text-To-Speech API sample application .
Example usage:
python quickstart.py
"""

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/aadhikari/Documents/Projects/HackDuke/credentials.json"
from google.cloud import texttospeech

# Instantiates a client

client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="Hi, You’ve reached the offices Thank you, have a great day.")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("female")
voice = texttospeech.VoiceSelectionParams(
language_code='en-US',
name='en-US-Wavenet-C',
ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
audio_encoding=texttospeech.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
# Write the response to the output file.
	out.write(response.audio_content)
	print('Audio content written to file "output.mp3"')