# Py AI Assistant

Py Assistant ist ein Sprachassistent, der auf Python basiert. Er nutzt die [OpenAI GPT-3 API](https://openai.com/) für die Textgenerierung und [Thortsen Voice] (https://www.thorsten-voice.de/en/motivation-vision/) für TTS 

## Features

Py Assistant kann derzeit folgende Aktionen ausführen:

- YouTube-Videos abspielen: Sie können Py Assistant auffordern, ein bestimmtes Video auf YouTube zu finden und abzuspielen, indem Sie sagen "[Speakname] play [Video-Name]".
- Fragen beantworten: Sie können Py Assistant Fragen stellen, indem Sie einfach Ihre Frage stellen.

## Verwendung

Py Assistant kann durch die Ausführung der Datei `pyassintant.py` gestartet werden. Die folgenden Schritte sind erforderlich:

1. Fügen Sie Ihre OpenAI API-Schlüssel in die Variable `api_key` in der Datei `pyassintant.py` ein.
2. Stellen Sie sicher, dass Sie die erforderlichen Python-Bibliotheken installiert haben, indem Sie das folgende Kommando ausführen: `pip install -r requirements.txt`.
3. Führen Sie das Programm aus, indem Sie die Datei `pyassintant.py` ausführen.

## Anforderungen

Py Assistant erfordert die folgenden Anforderungen:

- Python 3.6 oder höher
- Eine Internetverbindung
- Eine gültige OpenAI API-Schlüssel von https://api.chatanywhere.org/v1/oauth/free/github/render

## Credits

Py Assistant wurde von thetechnikfreak entwickelt und verwendet die folgenden Bibliotheken:

- [Chatanywhere API](https://api.chatanywhere.org/v1/oauth/free/github/render)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- [requests](https://pypi.org/project/requests/)
- [json](https://docs.python.org/3/library/json.html)
- [tkinter](https://docs.python.org/3/library/tk.html)
- [threading](https://pypi.org/project/threading)
- [request](https://pypi.org/project/request)
- [pygame](https://pypi.org/project/pygame)
- [pytube](https://pypi.org/project/pytube)
- [ytmusicapi](https://pypi.org/project/ytmusicapi)
- [vlc](https://pypi.org/project/python-vlc)

## Lizenz

Py AI Assistant ist unter der [MIT-Lizenz](https://opensource.org/licenses/MIT) lizenziert.
