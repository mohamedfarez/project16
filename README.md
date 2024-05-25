# project16
Chatbot with NLP (Speech Recognition )


by: mohamed fares
The ChatBot class is the main entry point for the AI chatbot application. It provides functionality for speech-to-text conversion, text-to-speech generation, and handling various user interactions.

The class has the following methods:

- `__init__(self, name)`: Initializes the ChatBot instance with the given name.
- `speech_to_text(self)`: Converts speech input from the microphone to text using the speech_recognition library.
- `text_to_speech(text)`: Converts the given text to speech using the gTTS library and plays the audio.
- `wake_up(self, text)`: Checks if the chatbot's name is mentioned in the given text, indicating that the user is addressing the chatbot.
- `action_time(self)`: Returns the current time in the format 'HH:MM'.

The `if __name__ == "__main__":` block sets up the ChatBot instance, initializes the language model, and enters a loop to handle user interactions.

 Handles the case where the AI's response is "ERROR". If this occurs, it sets the response to "Sorry, come again?". Otherwise, it processes the AI's text using the Transformers library, extracts the bot's response, and sends it to the text-to-speech engine.
    
