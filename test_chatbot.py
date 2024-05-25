"""
Test suite for the ChatBot class.

This test suite covers the following scenarios:
- Greeting the user
- Saying goodbye to the user
- Handling unknown user input
- Making an API call and returning the response
- Handling empty user input

Each test case checks that the ChatBot.get_response() method returns the expected response for the given user input.
"""
import unittest
from unittest.mock import patch, Mock
from chatbot import ChatBot

class TestChatBot(unittest.TestCase):

    def setUp(self):
        self.chatbot = ChatBot()

    def test_get_response_greet(self):
        user_input = "hello"
        expected_response = "Hello! How can I assist you today?"
        response = self.chatbot.get_response(user_input)
        self.assertEqual(response, expected_response)

    def test_get_response_goodbye(self):
        user_input = "goodbye"
        expected_response = "Goodbye! Have a great day."
        response = self.chatbot.get_response(user_input)
        self.assertEqual(response, expected_response)

    def test_get_response_unknown(self):
        user_input = "something unknown"
        expected_response = "I'm sorry, I didn't understand that. Could you please rephrase your request?"
        response = self.chatbot.get_response(user_input)
        self.assertEqual(response, expected_response)

    @patch('chatbot.ChatBot.call_api')
    def test_get_response_api_call(self, mock_call_api):
        mock_call_api.return_value = "API response"
        user_input = "what is the weather today?"
        expected_response = "API response"
        response = self.chatbot.get_response(user_input)
        self.assertEqual(response, expected_response)
        mock_call_api.assert_called_once()

    def test_get_response_empty_input(self):
        user_input = ""
        expected_response = "I'm sorry, I didn't receive any input. Please try again."
        response = self.chatbot.get_response(user_input)
        self.assertEqual(response, expected_response)
