import speech_recognition as sr
import pyttsx3
import openai
import pywhatkit                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                 
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
# Your Open ai Api Key from https://platform.openai.com/account/api-keys
openai.api_key = "<Typ in your Open Ai Api Key>"
#-----------------------------

# ----- Optimal Settings ------
# The Name the Voice Assitant react
speakname = "Auto"
# The Language the audio to text listen to
language = "de-DE"
# The sentence when the Assistant dot understand you
error = "Entschuldigung, ich habe das nicht verstanden"
# The sentence when the Assistant you ask to speak
speak = "Sprechen Sie jetzt"
# The sentence when the Assistant you say you that your Speaking is over
over = "Vielen Dank, das Gespräch ist beendet"
#------------------------------
engine = pyttsx3.init()
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print(speak)
        audio_text = r.listen(source)
        print(over)
    recognized_text = r.recognize_google(audio_text, language=language)
    if speakname in recognized_text:
        print("Text: " + recognized_text)
        recognized_text = recognized_text.replace(speakname, "")
        
        if "play" in recognized_text:
            song = recognized_text.replace("play", "")
            pywhatkit.playonyt(song)
            
        else:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=recognized_text + "auf deutsch",
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            engine.say(response["choices"][0]["text"])
            engine.runAndWait()


    else:
        engine.say(error)
        engine.runAndWait()
        print(error)

