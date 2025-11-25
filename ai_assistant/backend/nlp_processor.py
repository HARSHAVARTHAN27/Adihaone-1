"""
NLP module for processing user commands and intent recognition.
"""
import re
from datetime import datetime

class NLPProcessor:
    """Processes natural language input and recognizes user intents."""
    
    def __init__(self):
        """Initialize the NLP processor."""
        self.intents = {
            'time': ['what time', 'current time', 'tell me time', 'what\'s the time'],
            'date': ['what date', 'current date', 'today\'s date', 'what\'s today'],
            'reminder': ['remind me', 'set reminder', 'set a reminder', 'create reminder'],
            'search': ['search for', 'find information', 'web search', 'look up', 'google'],
            'math': ['calculate', 'solve', 'what is', 'how much', 'multiply', 'add', 'subtract', 'divide'],
            'greeting': ['hello', 'hi', 'hey', 'greetings', 'what\'s up'],
            'help': ['help', 'what can you do', 'available commands', 'capabilities'],
            'goodbye': ['goodbye', 'bye', 'exit', 'quit', 'see you']
        }
    
    def recognize_intent(self, text):
        """
        Recognize the intent of the user's input.
        
        Args:
            text (str): User input text
            
        Returns:
            dict: Contains 'intent' and 'confidence'
        """
        text_lower = text.lower().strip()
        
        # Check each intent
        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if keyword in text_lower:
                    return {
                        'intent': intent,
                        'confidence': 0.9,
                        'text': text
                    }
        
        # Default to unknown
        return {
            'intent': 'unknown',
            'confidence': 0.0,
            'text': text
        }
    
    def extract_entities(self, text):
        """
        Extract entities (numbers, dates, names) from text.
        
        Args:
            text (str): User input text
            
        Returns:
            dict: Extracted entities
        """
        entities = {
            'numbers': self._extract_numbers(text),
            'time_expressions': self._extract_time_expressions(text),
            'dates': self._extract_dates(text)
        }
        return entities
    
    def _extract_numbers(self, text):
        """Extract numeric values from text."""
        numbers = re.findall(r'\b\d+(?:\.\d+)?\b', text)
        return [float(n) if '.' in n else int(n) for n in numbers]
    
    def _extract_time_expressions(self, text):
        """Extract time-related expressions."""
        time_patterns = r'\b(\d{1,2}:\d{2}(?:am|pm)?|\b(?:morning|afternoon|evening|night)\b)'
        return re.findall(time_patterns, text, re.IGNORECASE)
    
    def _extract_dates(self, text):
        """Extract date-related expressions."""
        date_patterns = r'\b(\d{1,2}/\d{1,2}/\d{2,4}|(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)|tomorrow|today)\b'
        return re.findall(date_patterns, text, re.IGNORECASE)
    
    def parse_command(self, text):
        """
        Parse user input and extract intent with entities.
        
        Args:
            text (str): User input text
            
        Returns:
            dict: Parsed command with intent and entities
        """
        intent_result = self.recognize_intent(text)
        entities = self.extract_entities(text)
        
        return {
            'intent': intent_result['intent'],
            'confidence': intent_result['confidence'],
            'text': text,
            'entities': entities
        }
