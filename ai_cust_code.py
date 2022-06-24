import speech_recognition  as sr
import os
# import transformers
from pydub import AudioSegment
from pydub.silence import split_on_silence
from gtts import gTTS
import os
import time

from transformers import pipeline
import playsound
import pickle
import random,string
r = sr.Recognizer()

with open(r"sentiment-analysis.pickle", "rb") as input_file:
    model=pickle.load(input_file)


def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=500,
                              # adjust this per requirement
                              silence_thresh=sound.dBFS - 14,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=500,
                              )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text


def return_text(filename):
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        whole_text = r.recognize_google(audio_data)
        return whole_text


def speak(text, name):
    tts = gTTS(text=text, lang='en')
    filename = name + '.mp3'
    tts.save(filename)
    playsound.playsound(filename, True)


def get_audio(said, dur):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=dur)
    try:
        said = r.recognize_google(audio)
        print(said)
    except Exception as e:
        print("Can't Hear From User" + str(e))
    return said


def final_outcome(filename):
    text = return_text(filename)
    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    speak(text, name)

    print('AI Speak Recording Done, Kindly Wait for User Outcome, before moving to next.')

    said = ""
    for i in range(1):
        said += get_audio(said, 3)
        if (len(said) > 1):
            print('I recieved input from user')
            break
        else:
            pass
    return model(said)[0]['label']




























































