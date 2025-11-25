"""
Speech-to-Text module using speech_recognition.
"""
import speech_recognition as sr


class SpeechRecognitionModule:
    """Handles speech-to-text conversion."""
    
    def __init__(self):
        """Initialize the speech recognizer."""
        self.recognizer = sr.Recognizer()
        try:
            self.microphone = sr.Microphone()
        except Exception as e:
            print(f"Warning: Microphone not available: {e}")
            self.microphone = None
    
    def listen(self, timeout=10, phrase_time_limit=5):
        """
        Listen for speech from microphone.
        
        Args:
            timeout (int): Timeout for listening in seconds
            phrase_time_limit (int): Time limit for the phrase in seconds
            
        Returns:
            str: Recognized text or None if not recognized
        """
        try:
            if not self.microphone:
                print("Microphone not available")
                return None
            
            with self.microphone as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            
            # Recognize speech using Google Speech Recognition
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        
        except sr.UnknownValueValue:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Error with speech recognition service: {e}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def listen_from_file(self, filepath):
        """
        Recognize speech from an audio file.
        
        Args:
            filepath (str): Path to audio file
            
        Returns:
            str: Recognized text or None if not recognized
        """
        try:
            with sr.AudioFile(filepath) as source:
                audio = self.recognizer.record(source)
            
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Error with speech recognition service: {e}")
            return None
