"""
Free API-based NLP processor for AI Personal Assistant.
Uses free APIs like Hugging Face, Groq, or Together AI.
"""
import os
import requests
from typing import Dict, Any

class FreeAPIProcessor:
    """Handles NLP using free APIs."""
    
    def __init__(self, api_key: str = None, api_provider: str = "groq"):
        """
        Initialize free API processor.
        
        Args:
            api_key (str): API key for the chosen provider
            api_provider (str): API provider (groq, huggingface, together)
        """
        self.api_key = api_key or os.getenv('FREE_API_KEY', '')
        self.api_provider = api_provider or os.getenv('API_PROVIDER', 'groq')
        
        if not self.api_key:
            raise ValueError("API_KEY not provided. Please set FREE_API_KEY environment variable.")
        
        self.setup_provider()
    
    def setup_provider(self):
        """Setup the API provider."""
        if self.api_provider == "groq":
            self.api_url = "https://api.groq.com/openai/v1/chat/completions"
            self.model = "llama-3.3-70b-versatile"  # Latest available model
            self.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        elif self.api_provider == "huggingface":
            self.api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
            self.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        elif self.api_provider == "together":
            self.api_url = "https://api.together.xyz/v1/chat/completions"
            self.model = "mistralai/Mistral-7B-Instruct-v0.1"
            self.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        else:
            raise ValueError(f"Unknown API provider: {self.api_provider}")
    
    def process(self, user_input: str, system_prompt: str = None) -> Dict[str, Any]:
        """
        Process user input using free API and return response.
        
        Args:
            user_input (str): User's input text
            system_prompt (str): System prompt for context (optional)
            
        Returns:
            Dict with response, tokens, and metadata
        """
        try:
            if not system_prompt:
                system_prompt = (
                    "You are a helpful AI personal assistant. Be concise, friendly, and helpful. "
                    "Answer questions accurately and perform the requested tasks."
                )
            
            # Prepare the request based on provider
            if self.api_provider == "groq":
                response = self._call_groq(user_input, system_prompt)
            elif self.api_provider == "huggingface":
                response = self._call_huggingface(user_input, system_prompt)
            elif self.api_provider == "together":
                response = self._call_together(user_input, system_prompt)
            else:
                return {
                    'response': 'Unknown API provider',
                    'error': True,
                    'tokens': 0
                }
            
            return response
            
        except Exception as e:
            return {
                'response': f'Error: {str(e)}',
                'error': True,
                'tokens': 0
            }
    
    def _call_groq(self, user_input: str, system_prompt: str) -> Dict[str, Any]:
        """Call Groq API (free tier available)."""
        try:
            payload = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                "temperature": 0.7,
                "max_tokens": 1024
            }
            
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'response': data['choices'][0]['message']['content'],
                    'error': False,
                    'tokens': data.get('usage', {}).get('total_tokens', 0)
                }
            else:
                return {
                    'response': f'API Error: {response.status_code}',
                    'error': True,
                    'tokens': 0
                }
        except Exception as e:
            return {
                'response': f'Groq API Error: {str(e)}',
                'error': True,
                'tokens': 0
            }
    
    def _call_huggingface(self, user_input: str, system_prompt: str) -> Dict[str, Any]:
        """Call Hugging Face Inference API (free tier available)."""
        try:
            payload = {
                "inputs": f"{system_prompt}\n\nUser: {user_input}\n\nAssistant:",
                "parameters": {"max_new_tokens": 512}
            }
            
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and len(data) > 0:
                    text = data[0].get('generated_text', '')
                    return {
                        'response': text,
                        'error': False,
                        'tokens': len(text.split())
                    }
                else:
                    return {
                        'response': str(data),
                        'error': False,
                        'tokens': 0
                    }
            else:
                return {
                    'response': f'API Error: {response.status_code}',
                    'error': True,
                    'tokens': 0
                }
        except Exception as e:
            return {
                'response': f'Hugging Face API Error: {str(e)}',
                'error': True,
                'tokens': 0
            }
    
    def _call_together(self, user_input: str, system_prompt: str) -> Dict[str, Any]:
        """Call Together AI API (free tier available)."""
        try:
            payload = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                "temperature": 0.7,
                "max_tokens": 1024
            }
            
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'response': data['choices'][0]['message']['content'],
                    'error': False,
                    'tokens': data.get('usage', {}).get('total_tokens', 0)
                }
            else:
                return {
                    'response': f'API Error: {response.status_code}',
                    'error': True,
                    'tokens': 0
                }
        except Exception as e:
            return {
                'response': f'Together AI Error: {str(e)}',
                'error': True,
                'tokens': 0
            }
    
    def get_available_models(self) -> list:
        """Get list of available models for the provider."""
        if self.api_provider == "groq":
            return ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "qwen/qwen3-32b"]
        elif self.api_provider == "huggingface":
            return ["mistralai/Mistral-7B-Instruct-v0.1", "meta-llama/Llama-2-7b-chat"]
        elif self.api_provider == "together":
            return ["mistralai/Mistral-7B-Instruct-v0.1", "meta-llama/Llama-2-7b-chat-hf"]
        return []
    
    def set_model(self, model_name: str) -> bool:
        """Set the model to use."""
        available = self.get_available_models()
        if model_name in available:
            self.model = model_name
            return True
        return False
