"""
Multi-provider LLM processor supporting multiple free APIs.
Supports: Groq, HuggingFace, Together AI, Deepgram, and more.
"""
import os
import requests
from typing import Dict, Any

class LLMProcessor:
    """Unified processor for multiple LLM providers."""
    
    def __init__(self, api_key: str = None, provider: str = "groq"):
        """
        Initialize LLM processor with support for multiple providers.
        
        Args:
            api_key (str): API key for the provider
            provider (str): Provider name (groq, huggingface, together, deepgram)
        """
        self.api_key = api_key or os.getenv('LLM_API_KEY', '')
        self.provider = provider or os.getenv('LLM_PROVIDER', 'groq')
        
        if not self.api_key:
            raise ValueError(f"API_KEY not provided for {self.provider}")
        
        self.setup_provider()
    
    def setup_provider(self):
        """Setup the selected provider configuration."""
        if self.provider == "groq":
            self.api_url = "https://api.groq.com/openai/v1/chat/completions"
            self.model = "llama-3.3-70b-versatile"
            self.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        
        elif self.provider == "deepgram":
            self.api_url = "https://api.deepgram.com/v1/models"
            self.model = "deepgram-nova-2"
            self.headers = {
                "Authorization": f"Token {self.api_key}",
                "Content-Type": "application/json"
            }
        
        elif self.provider == "huggingface":
            self.api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
            self.model = "mistralai/Mistral-7B-Instruct-v0.1"
            self.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        
        elif self.provider == "together":
            self.api_url = "https://api.together.xyz/v1/chat/completions"
            self.model = "mistralai/Mistral-7B-Instruct-v0.1"
            self.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        
        else:
            raise ValueError(f"Unknown provider: {self.provider}")
    
    def process(self, user_input: str, system_prompt: str = None) -> Dict[str, Any]:
        """
        Process user input and return LLM response.
        
        Args:
            user_input (str): User's input text
            system_prompt (str): System prompt for context
            
        Returns:
            Dict with response and metadata
        """
        try:
            if not system_prompt:
                system_prompt = (
                    "You are a helpful AI personal assistant. Be concise, friendly, and helpful. "
                    "Answer questions accurately and perform the requested tasks."
                )
            
            if self.provider in ["groq", "together"]:
                return self._call_chat_api(user_input, system_prompt)
            elif self.provider == "huggingface":
                return self._call_huggingface(user_input, system_prompt)
            elif self.provider == "deepgram":
                return self._call_deepgram(user_input, system_prompt)
            else:
                return {
                    'response': f'Provider {self.provider} not supported',
                    'error': True,
                    'tokens': 0
                }
        
        except Exception as e:
            return {
                'response': f'Error: {str(e)}',
                'error': True,
                'tokens': 0
            }
    
    def _call_chat_api(self, user_input: str, system_prompt: str) -> Dict[str, Any]:
        """Call OpenAI-compatible chat API (Groq, Together, etc)."""
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
                    'tokens': data.get('usage', {}).get('total_tokens', 0),
                    'provider': self.provider
                }
            elif response.status_code == 401:
                return {
                    'response': 'Invalid API key. Please check your credentials.',
                    'error': True,
                    'tokens': 0
                }
            else:
                return {
                    'response': f'API Error {response.status_code}: {response.text[:200]}',
                    'error': True,
                    'tokens': 0
                }
        except Exception as e:
            return {
                'response': f'{self.provider.title()} API Error: {str(e)}',
                'error': True,
                'tokens': 0
            }
    
    def _call_huggingface(self, user_input: str, system_prompt: str) -> Dict[str, Any]:
        """Call Hugging Face Inference API."""
        try:
            prompt = f"{system_prompt}\n\nUser: {user_input}\n\nAssistant:"
            payload = {
                "inputs": prompt,
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
                    # Extract only the assistant's response
                    if 'Assistant:' in text:
                        text = text.split('Assistant:')[-1].strip()
                    return {
                        'response': text,
                        'error': False,
                        'tokens': len(text.split()),
                        'provider': self.provider
                    }
                return {
                    'response': str(data),
                    'error': False,
                    'tokens': 0
                }
            elif response.status_code == 401:
                return {
                    'response': 'Invalid Hugging Face token.',
                    'error': True,
                    'tokens': 0
                }
            else:
                return {
                    'response': f'API Error {response.status_code}',
                    'error': True,
                    'tokens': 0
                }
        except Exception as e:
            return {
                'response': f'Hugging Face Error: {str(e)}',
                'error': True,
                'tokens': 0
            }
    
    def _call_deepgram(self, user_input: str, system_prompt: str) -> Dict[str, Any]:
        """Call Deepgram API (if they have LLM support)."""
        # Deepgram primarily focuses on speech, not text LLM
        # This is a placeholder for future integration
        return {
            'response': 'Deepgram LLM support coming soon. Use speech-to-text instead.',
            'error': True,
            'tokens': 0
        }
    
    def get_available_models(self) -> list:
        """Get list of available models for the provider."""
        if self.provider == "groq":
            return ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "qwen/qwen3-32b"]
        elif self.provider == "huggingface":
            return ["mistralai/Mistral-7B-Instruct-v0.1", "meta-llama/Llama-2-7b-chat"]
        elif self.provider == "together":
            return ["mistralai/Mistral-7B-Instruct-v0.1", "meta-llama/Llama-2-7b-chat-hf"]
        elif self.provider == "deepgram":
            return ["deepgram-nova-2", "deepgram-nova", "deepgram-base"]
        return []
    
    def set_model(self, model_name: str) -> bool:
        """Set the model to use."""
        available = self.get_available_models()
        if model_name in available:
            self.model = model_name
            return True
        return False
