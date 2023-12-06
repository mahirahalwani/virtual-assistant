import sys
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize the recognizer
r = sr.Recognizer()


class SpeakToMe:
    def __init__(self) -> None:
        self.voice_id = 'com.apple.speech.synthesis.voice.ava.premium'
        self.driver_name = 'nsss'
        self.speech_lang = 'en_US'

    @staticmethod
    def SpeakText(my_command: str = None, driver_name: str = 'nsss',
                  voice_id: str = 'com.apple.speech.synthesis.voice.ava.premium'):
        try:
            # Initialize the engine
            if my_command is None:
                return
            engine = pyttsx3.init(driverName=driver_name)
            engine.setProperty('voice', voice_id)
            engine.say(my_command)
            engine.runAndWait()
        except Exception as e:
            print(e)

    def listen_to_me(self):

        text = "Good day sir, let me initialize!"
        self.SpeakText(text, voice_id=self.voice_id,
                       driver_name=self.driver_name)

        # Loop infinitely for user to
        # speak
        while(True):
            try:

                # use the microphone as source for input.
                with sr.Microphone() as source:
                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level
                    r.adjust_for_ambient_noise(source, duration=0.2)

                    # listens for the user's input
                    audio = r.listen(source)

                    # Using google to recognize audio
                    my_text = r.recognize_google(
                        audio, language=self.speech_lang)
                    my_text = my_text.lower()

                    self.yes_minion(my_command=my_text)

                    my_text = ""

            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except sr.UnknownValueError as e:
                pass
            except Exception as e:
                print(f"Error: ' {e} ' occured!")

    def yes_minion(self, my_command: str = None):
        if my_command is None:
            return

        system_call = ['hello', 'hallo']
        if my_command in system_call:
            name = "Hello, Sir. My name is Abu."
            self.SpeakText(name, voice_id=self.voice_id, driver_name=self.driver_name)
            return

        tellday = ['what day is today']
        if my_command in tellday:
            # This function is for telling the
            # day of the week
            day = datetime.datetime.today().weekday() + 1
     
            #this line tells us about the number 
            # that will help us in telling the day
            Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                self.SpeakText("The day is " + day_of_the_week)
            return  

        telltime = ['what time is it']
        if my_command in telltime:
            # This method will give the time
            time = str(datetime.datetime.now())
     
            # the time will be displayed like 
            # this "2020-06-05 17:50:14.582630"
            #nd then after slicing we can get time
            print(time)
            hour = time[11:13]
            min = time[14:16]
            self.SpeakText("The time is" + hour + "Hours and" + min + "Minutes")
            return

        thanks = ['thank you']
        if my_command in thanks:
            self.SpeakText("You're welcome, sir")
            return       

        shutdown = ['shut down', 'shutdown', 'shutting down']
        if my_command in shutdown:
            talk = "Shutting down, bye bye"
            self.SpeakText(talk, voice_id=self.voice_id, driver_name=self.driver_name)
            sys.exit()

        sorry = "Sorry sir, I do not understand you. Could you say it again?"
        self.SpeakText(sorry, voice_id=self.voice_id, driver_name=self.driver_name)


if __name__ == "__main__":
    #call the class 
    stm = SpeakToMe()

    # start python to listnen to you!
    stm.listen_to_me()
