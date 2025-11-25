"""
Text-to-Speech module using pyttsx3.
"""
import pyttsx3
import threading
import time


class TextToSpeech:
    """Handles text-to-speech conversion."""
    
    def __init__(self):
        """Initialize the text-to-speech engine."""
        self.voice_index = 0
        self.rate = 150
        self.volume = 0.9
        self.available_voices = []
        self._get_available_voices()
    
    def _get_available_voices(self):
        """Get list of available voices."""
        try:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            self.available_voices = []
            for i, voice in enumerate(voices):
                self.available_voices.append({
                    'id': voice.id,
                    'name': voice.name,
                    'index': i
                })
            engine.stop()
            del engine
            print(f"Available voices: {[v['name'] for v in self.available_voices]}")
        except Exception as e:
            print(f"Error getting voices: {e}")
    
    def speak(self, text):
        """
        Convert text to speech and play it.
        
        Args:
            text (str): Text to convert to speech
        """
        if not text or not text.strip():
            return
        
        try:
            # Create a fresh engine for each speech
            engine = pyttsx3.init()
            engine.setProperty('rate', self.rate)
            engine.setProperty('volume', self.volume)
            
            # Set the voice
            if self.available_voices and self.voice_index < len(self.available_voices):
                try:
                    voice_id = self.available_voices[self.voice_index]['id']
                    engine.setProperty('voice', voice_id)
                except Exception as e:
                    print(f"Error setting voice: {e}")
            
            print(f"Speaking with voice index {self.voice_index}...", flush=True)
            engine.say(text)
            engine.runAndWait()
            
            # Ensure engine is stopped
            engine.stop()
            
            # Small delay to ensure audio finishes
            time.sleep(0.5)
            
            # Clean up
            del engine
            print(f"✓ Speech completed", flush=True)
            
        except Exception as e:
            print(f"❌ Error in text-to-speech: {e}", flush=True)
    
    def set_rate(self, rate):
        """
        Set speech rate.
        
        Args:
            rate (int): Speech rate (50-300, default 150)
        """
        try:
            self.rate = max(50, min(300, rate))
            print(f"Rate set to: {self.rate}", flush=True)
        except Exception as e:
            print(f"Error setting rate: {e}")
    
    def set_volume(self, volume):
        """
        Set speech volume.
        
        Args:
            volume (float): Volume level (0-1)
        """
        try:
            self.volume = max(0, min(1, float(volume)))
            print(f"Volume set to: {self.volume}", flush=True)
        except Exception as e:
            print(f"Error setting volume: {e}")
    
    def set_voice(self, voice_index=0):
        """
        Set the voice for speech.
        
        Args:
            voice_index (int): Voice index from available voices
        """
        try:
            if 0 <= voice_index < len(self.available_voices):
                self.voice_index = voice_index
                print(f"Voice set to: {self.available_voices[voice_index]['name']}", flush=True)
        except Exception as e:
            print(f"Error setting voice: {e}")
    
    def get_available_voices(self):
        """
        Get list of available voices.
        
        Returns:
            list: List of available voice dictionaries
        """
        return self.available_voices

    
    def set_rate(self, rate):
        """
        Set speech rate.
        
        Args:
            rate (int): Speech rate (50-300, default 150)
        """
        try:
            self.rate = max(50, min(300, rate))
        except Exception as e:
            print(f"Error setting rate: {e}")
    
    def set_volume(self, volume):
        """
        Set speech volume.
        
        Args:
            volume (float): Volume level (0-1)
        """
        try:
            self.volume = max(0, min(1, float(volume)))
        except Exception as e:
            print(f"Error setting volume: {e}")
    
    def set_voice(self, voice_index=0):
        """
        Set the voice for speech.
        
        Args:
            voice_index (int): Voice index from available voices
        """
        try:
            if 0 <= voice_index < len(self.available_voices):
                self.voice_index = voice_index
                print(f"Voice set to: {self.available_voices[voice_index]['name']}")
        except Exception as e:
            print(f"Error setting voice: {e}")
    
    def get_available_voices(self):
        """
        Get list of available voices.
        
        Returns:
            list: List of available voice dictionaries
        """
        return self.available_voices
