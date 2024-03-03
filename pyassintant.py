import speech_recognition as sr
import time
import threading
import tkinter as tk
import pywhatkit
import pygame
import playsound    
import subprocess
import os
import requests
import json                                                                                                                                                                                                                                  
import os
import threading
import vlc
from pytube import YouTube
from ytmusicapi import YTMusic

#PPPPPPPPPPPPPPPPP  YYYYYYY       YYYYYYY                    AAA              IIIIIIIIII                         AAA                                              iiii                          tttt                                                      tttt          
#P::::::::::::::::P Y:::::Y       Y:::::Y                   A:::A             I::::::::I                        A:::A                                            i::::i                      ttt:::t                                                   ttt:::t          
#P::::::PPPPPP:::::PY:::::Y       Y:::::Y                  A:::::A            I::::::::I                       A:::::A                                            iiii                       t:::::t                                                   t:::::t          
#PP:::::P     P:::::Y::::::Y     Y::::::Y                 A:::::::A           II::::::II                      A:::::::A                                                                      t:::::t                                                   t:::::t          
  #P::::P     P:::::YYY:::::Y   Y:::::YYY                A:::::::::A            I::::I                       A:::::::::A            ssssssssss      ssssssssss  iiiiiii    ssssssssss  ttttttt:::::ttttttt       eeeeeeeeeeee   nnnn  nnnnnnnn   ttttttt:::::ttttttt    
  #P::::P     P:::::P  Y:::::Y Y:::::Y                  A:::::A:::::A           I::::I                      A:::::A:::::A         ss::::::::::s   ss::::::::::s i:::::i  ss::::::::::s t:::::::::::::::::t     ee::::::::::::ee n:::nn::::::::nn t:::::::::::::::::t    
  #P::::PPPPPP:::::P    Y:::::Y:::::Y                  A:::::A A:::::A          I::::I                     A:::::A A:::::A      ss:::::::::::::sss:::::::::::::s i::::iss:::::::::::::st:::::::::::::::::t    e::::::eeeee:::::en::::::::::::::nnt:::::::::::::::::t    
  #P:::::::::::::PP      Y:::::::::Y                  A:::::A   A:::::A         I::::I                    A:::::A   A:::::A     s::::::ssss:::::s::::::ssss:::::si::::is::::::ssss:::::tttttt:::::::tttttt   e::::::e     e:::::nn:::::::::::::::tttttt:::::::tttttt    
  #P::::PPPPPPPPP         Y:::::::Y                  A:::::A     A:::::A        I::::I                   A:::::A     A:::::A     s:::::s  ssssss s:::::s  ssssss i::::i s:::::s  ssssss      t:::::t         e:::::::eeeee::::::e n:::::nnnn:::::n     t:::::t          
  #P::::P                  Y:::::Y                  A:::::AAAAAAAAA:::::A       I::::I                  A:::::AAAAAAAAA:::::A      s::::::s        s::::::s      i::::i   s::::::s           t:::::t         e:::::::::::::::::e  n::::n    n::::n     t:::::t          
  #P::::P                  Y:::::Y                 A:::::::::::::::::::::A      I::::I                 A:::::::::::::::::::::A        s::::::s        s::::::s   i::::i      s::::::s        t:::::t         e::::::eeeeeeeeeee   n::::n    n::::n     t:::::t          
  #P::::P                  Y:::::Y                A:::::AAAAAAAAAAAAA:::::A     I::::I                A:::::AAAAAAAAAAAAA:::::A ssssss   s:::::sssssss   s:::::s i::::issssss   s:::::s      t:::::t    ttttte:::::::e            n::::n    n::::n     t:::::t    tttttt
#PP::::::PP                Y:::::Y               A:::::A             A:::::A  II::::::II             A:::::A             A:::::As:::::ssss::::::s:::::ssss::::::i::::::s:::::ssss::::::s     t::::::tttt:::::e::::::::e           n::::n    n::::n     t::::::tttt:::::t
#P::::::::P             YYYY:::::YYYY           A:::::A               A:::::A I::::::::I            A:::::A               A:::::s::::::::::::::ss::::::::::::::si::::::s::::::::::::::s      tt::::::::::::::te::::::::eeeeeeee   n::::n    n::::n     tt::::::::::::::t
#P::::::::P             Y:::::::::::Y          A:::::A                 A:::::AI::::::::I           A:::::A                 A:::::s:::::::::::ss  s:::::::::::ss i::::::is:::::::::::ss         tt:::::::::::tt ee:::::::::::::e   n::::n    n::::n       tt:::::::::::tt
#PPPPPPPPPP             YYYYYYYYYYYYY         AAAAAAA                   AAAAAAIIIIIIIIII          AAAAAAA                   AAAAAAsssssssssss     sssssssssss   iiiiiiii sssssssssss             ttttttttttt     eeeeeeeeeeeeee   nnnnnn    nnnnnn         ttttttttttt  
                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                 
                                                                                                                                                                                                            
# ----- Needed Settings ------
# Your Free Api Key from https://api.chatanywhere.org/v1/oauth/free/github/render
OPENAI_API_KEY = "<Type Your Api Key Here>"
#-----------------------------

# ----- Optimal Settings ------
# The Name the Voice Assitant react
speakname = "Alexa"
# The Language the audio to text listen to
language = "de-DE"
# The sentence when the Assistant dot understand you
error = "Entschuldigung, ich habe das nicht verstanden"
# The sentence when the Assistant you ask to speak
speak = "Sprechen Sie jetzt"
# The sentence when the Assistant you say you that your Speaking is over
over = "Vielen Dank, das Gespräch ist beendet"
# The sentence when the Assistant has no internet connection
no_internet = "Entschulding ich habe keine Internetverbindung"
# The sentence when TTS Fails
error2 = "Das Ausprechen der Antwort ist fehlgeschlagen"
#------------------------------
r = sr.Recognizer()


class MusicPlayer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.player = None
        self.playing = False
        self.paused = False
        self.audio_file = None

    def run(self):
        while True:
            if self.player:
                pass  # Add any additional functionality needed during playback
            if self.player and not self.player.is_playing() and self.playing:
                self.playing = False
                self.paused = False
                self.audio_file = None
                print("Playback finished.")
                break

    def search_video(self, query):
        ytmusic = YTMusic()
        search_results = ytmusic.search(query, filter='videos', limit=1)
        if search_results:
            video_url = "https://music.youtube.com/watch?v=" + search_results[0]['videoId']
            return video_url
        else:
            print("No videos found for the given query.")
            return None

    def download_audio(self, video_url):
        try:
            yt = YouTube(video_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            out_file = audio_stream.download()
            base, _ = os.path.splitext(out_file)
            self.audio_file = base + '.mp3'
            os.rename(out_file, self.audio_file)
            print(yt.title + " has been successfully downloaded as an MP3 file.")
        except Exception as e:
            print("An error occurred:", e)

    def play(self):
        if self.audio_file:
            self.player = vlc.MediaPlayer(self.audio_file)
            self.player.play()
            self.playing = True
            self.paused = False

    def pause(self):
        if self.player and not self.paused:
            self.player.pause()
            self.paused = True

    def resume(self):
        if self.player and self.paused:
            self.player.play()
            self.paused = False

    def stop(self):
        if self.player:
            self.player.stop()
            self.playing = False
            self.paused = False

    def play_song(self, query):
        video_url = self.search_video(query)
        if video_url:
            self.download_audio(video_url)
            self.play()


player = MusicPlayer()

def get_chat_completion(text):
    url = 'https://api.chatanywhere.com.cn/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}'
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': text}],
        'temperature': 1.0
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        if 'choices' in result and len(result['choices']) > 0:
            return result.get('choices', [])[0].get('message', {}).get('content', None)

        else:
            print("No choices found in the response.")
            return None
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Example usage

def download_audio(text):
    # Destination file path to save the MP3
    destination_path = "output.wav"

    # Send a GET request to the URL and save the content to a file
    response = requests.get('http://localhost:5002/api/tts?text=' + text)
    if response.status_code == 200:
        try:
            with open(destination_path, "wb") as f:
                f.write(response.content)
            print("MP3 file downloaded successfully.")
            return destination_path
        except PermissionError:
            print("Permission denied: Unable to download audio")
            return None
    else:
        print("Failed to download MP3 file. Status code:", response.status_code)
        response = requests.get('http://localhost:5002/api/tts?text=' + error2)
        if response.status_code == 200:
            try:
                with open(destination_path, "wb") as f:
                    f.write(response.content)
                print("MP3 file downloaded successfully.")
                return destination_path
            except PermissionError:
                print("Permission denied: Unable to download audio")
                return None

# Function to play the audio file
def play_audio(audio_file):
    if os.path.exists(audio_file):
        # You can use any audio player here. Example using playsound:
        # subprocess.run(['playsound', audio_file])

        # If you want to use pygame:pi
        import pygame
        pygame.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print(f"File {audio_file} not found")
def process_speech():
    global is_listening
    while True:
        with sr.Microphone() as source:
            print(speak)
            is_listening = True
            canvas.itemconfig(circle, fill="green")
            root.update()
            audio_text = r.listen(source)
            print(over)
            is_listening = False
            canvas.itemconfig(circle, fill="yellow")
            root.update()
        try:
            recognized_text = r.recognize_google(audio_text, language=language)
        # Process the recognized text further if needed
            if speakname in recognized_text:
                print("Text: " + recognized_text)
                recognized_text = recognized_text.replace(speakname, "")
        
                if "Spiele" in recognized_text:
                    song = recognized_text.replace("spiele", "")
                    player.stop()
                    player.play_song(song)
                elif "Pause" in recognized_text:
                    player.pause()
                elif "Weiter" in recognized_text:
                    player.resume()

                else:
                    response = get_chat_completion(recognized_text + "auf deutsch")
                    print(response)
                    audio_file = download_audio(response)
                    play_audio(audio_file)
        except sr.UnknownValueError:
            audio_file = download_audio(error)
            play_audio(audio_file)
        except sr.RequestError as e:
            audio_file = download_audio(no_internet)
            play_audio(audio_file)
    


root = tk.Tk()
root.title("Voice Assistant")
root.geometry("200x200")

# Create canvas for drawing circles
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Draw red circle (initial state)
circle = canvas.create_oval(50, 50, 150, 150, fill="yellow")

# Create global variable to track whether assistant is listening
is_listening = False

# Start speech processing thread
speech_thread = threading.Thread(target=process_speech)
speech_thread.start()
player_thread = player.start()

# Run the GUI main loop
root.mainloop()
