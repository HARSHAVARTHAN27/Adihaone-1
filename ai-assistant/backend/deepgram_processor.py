"""
Deepgram-based NLP processor for AI Personal Assistant.
Uses Deepgram API for speech recognition and text processing.
"""
import os
import requests
from typing import Dict, Any

class DeepgramProcessor:
    """Handles NLP and speech processing using Deepgram API."""
    
    def __init__(self, api_key: str = None):
        """
        Initialize Deepgram processor.
        
        Args:
            api_key (str): Deepgram API key
        """
        self.api_key = api_key or os.getenv('DEEPGRAM_API_KEY', '')
        
        if not self.api_key:
            raise ValueError("DEEPGRAM_API_KEY not provided. Please set it in environment variables.")
        
        self.headers = {
            "Authorization": f"Token {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # Deepgram API endpoints
        self.tts_url = "https://api.deepgram.com/v1/speak"
        self.stt_url = "https://api.deepgram.com/v1/listen"
    
    def text_to_speech(self, text: str, voice: str = "aura-asteria-en") -> Dict[str, Any]:
        """
        Convert text to speech using Deepgram.
        
        Args:
            text (str): Text to convert
            voice (str): Voice model to use
            
        Returns:
            Dict with audio URL or error
        """
        try:
            params = {
                "model": voice,
                "encoding": "linear16"
            }
            
            response = requests.post(
                self.tts_url,
                headers=self.headers,
                json={"text": text},
                params=params,
                timeout=30
            )
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'audio': response.content,  # Raw audio bytes
                    'error': False
                }
            else:
                return {
                    'success': False,
                    'error': True,
                    'message': f'TTS Error: {response.status_code}'
                }
        except Exception as e:
            return {
                'success': False,
                'error': True,
                'message': f'Deepgram TTS Error: {str(e)}'
            }
    
    def speech_to_text(self, audio_file_path: str) -> Dict[str, Any]:
        """
        Convert speech to text using Deepgram.
        
        Args:
            audio_file_path (str): Path to audio file
            
        Returns:
            Dict with transcribed text
        """
        try:
            with open(audio_file_path, 'rb') as f:
                audio_data = f.read()
            
            headers = self.headers.copy()
            headers["Content-Type"] = "audio/wav"  # Adjust based on audio format
            
            params = {
                "model": "nova-2",
                "language": "en"
            }
            
            response = requests.post(
                self.stt_url,
                headers=headers,
                data=audio_data,
                params=params,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                transcript = data.get('results', {}).get('channels', [{}])[0].get('alternatives', [{}])[0].get('transcript', '')
                return {
                    'success': True,
                    'transcript': transcript,
                    'error': False
                }
            else:
                return {
                    'success': False,
                    'error': True,
                    'message': f'STT Error: {response.status_code}'
                }
        except Exception as e:
            return {
                'success': False,
                'error': True,
                'message': f'Deepgram STT Error: {str(e)}'
            }
    
    def get_available_voices(self) -> list:
        """Get list of available Deepgram voices."""
        return [
            "aura-asteria-en",      # Female voice
            "aura-luna-en",         # Female voice  
            "aura-stella-en",       # Female voice
            "aura-athena-en",       # Female voice
            "aura-hera-en",         # Female voice
            "aura-orion-en",        # Male voice
            "aura-arcas-en",        # Male voice
            "aura-perseus-en",      # Male voice
            "aura-angus-en"         # Male voice
        ]
