

"""
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
    
"""
# for speech-to-text
import speech_recognition as sr
# for text-to-speech
from gtts import gTTS
# for language model
import transformers
import os
import time
# for data
import os
import datetime
import numpy as np


# Building the AI
class ChatBot():
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening...")
            audio = recognizer.listen(mic)
            self.text="ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
            print("Me  --> ", self.text)
        except:
            print("Me  -->  ERROR")
    @staticmethod
    def text_to_speech(text):
        print("Fares --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        statbuf = os.stat("res.mp3")
        mbytes = statbuf.st_size / 1024
        duration = mbytes / 200
        os.system('start res.mp3')  
        time.sleep(int(50*duration))
        os.remove("res.mp3")
    def wake_up(self, text):
        return True if self.name in text.lower() else False
    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')
# Running the model
if __name__ == "__main__":
    ai = ChatBot(name="fares")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    ex=True
    while ex:
        ai.speech_to_text()
        ## wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Fares the AI, what can I do for you?"
        ## action time
        elif "time" in ai.text:
            res = ai.action_time()
        ## respond politely
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","mention not"])
        elif any(i in ai.text for i in ["how are you","good"]):
            res = np.random.choice(["I am fine ","Good!","cool!","I'm here if you need me!","mention not"])
        elif any(i in ai.text.lower() for i in ["help", "assist", "support"]):
            res = np.random.choice(["How can I help you?", "What do you need assistance with?", "I'm here to support you! What do you need?", "Let me know how I can help!"])
        elif any(i in ai.text.lower() for i in ["how are you", "how's it going", "how have you been"]):
            res = np.random.choice(["I'm just a bot, but I'm doing great! How about you?", "I'm here to help you! How are you?", "I'm functioning at full capacity! How can I assist you?"])
        elif any(i in ai.text.lower() for i in ["sorry", "apologies", "my bad", "pardon"]):
            res = np.random.choice(["No worries!", "It's okay!", "No problem!", "Don't worry about it!", "All good!"])
        elif any(i in ai.text.lower() for i in ["thank", "thanks", "thank you", "appreciate"]):
            res = np.random.choice(["You're welcome!", "Anytime!", "No problem!", "Glad to help!", "My pleasure!"])
        elif any(i in ai.text.lower() for i in ["no", "nope", "nah", "not really"]):
            res = np.random.choice(["Okay, no problem!", "Alright, let me know if you need anything else!", "Got it!", "No worries!"])
        elif any(i in ai.text.lower() for i in ["yes", "yeah", "yep", "sure", "absolutely"]):
            res = np.random.choice(["Great!", "Awesome!", "Good to hear!", "Alright!", "Excellent!"])
        elif any(i in ai.text.lower() for i in ["bye", "goodbye", "see you", "farewell"]):
            res = np.random.choice(["Goodbye!", "See you later!", "Take care!", "Farewell!", "Have a great day!"])
        elif any(i in ai.text.lower() for i in ["hi", "hello", "hey", "greetings"]):
            res = np.random.choice(["Hello!", "Hi there!", "Hey!", "Greetings!", "How can I help you today?"])
        elif any(i in ai.text.lower() for i in ["feedback", "opinion", "thoughts", "review"]):
            res = np.random.choice(["I'd love to give my feedback. What specifically are you asking about?", "Sure, I can provide my thoughts. What do you need feedback on?", "Let me know what you're looking for feedback on!", "I'd be happy to review it. What are you asking about?"])
        elif any(i in ai.text.lower() for i in ["info", "information", "details", "facts"]):
            res = np.random.choice(["What specific information are you looking for?", "I'd be happy to provide more details. What do you need to know?", "Let me get that information for you. What exactly are you interested in?", "I can help with that. What details do you need?"])
        elif any(i in ai.text.lower() for i in ["joke", "funny", "laugh", "humor", "hilarious"]):
            res = np.random.choice(["Why don't scientists trust atoms? Because they make up everything!", "Want to hear a joke about construction? I'm still working on it.", "Why did the scarecrow win an award? Because he was outstanding in his field!", "I'm always up for a good laugh!"])
        elif any(i in ai.text.lower() for i in ["recommend", "suggest", "advice", "tips"]):
            res = np.random.choice(["Sure, I'd be happy to help! What are you looking for recommendations on?", "I have some ideas! What do you need advice on?", "Let me give you some tips. What specifically are you interested in?", "I can suggest a few things. What are you thinking about?"])
        elif any(i in ai.text.lower() for i in ["weather", "rain", "sunny", "snow", "forecast"]):
            res = np.random.choice(["Weather can be quite unpredictable, right?", "Do you like this kind of weather?", "The weather is always a good topic to talk about!", "What's the weather like where you are?"])
        elif any(i in ai.text.lower() for i in ["sad", "unhappy", "depressed", "down", "upset"]):
            res = np.random.choice(["I'm sorry to hear that. Do you want to talk about it?", "I'm here for you. How can I help?", "That's tough. Is there anything I can do to assist you?", "I hope things get better for you soon."])
        elif any(i in ai.text.lower() for i in ["happy", "excited", "joyful", "elated", "thrilled"]):
            res = np.random.choice(["That's wonderful to hear!", "I'm glad you're feeling good!", "Awesome!", "That's great!", "Fantastic!"])
        elif any(i in ai.text.lower() for i in ["good job", "well done", "nice work", "impressive", "excellent"]):
            res = np.random.choice(["Thank you!", "Glad you liked it!", "I appreciate it!", "Thanks for the compliment!", "I'm happy to help!"])
        elif any(i in ai.text.lower() for i in ["okay", "got it", "understood", "alright", "cool"]):
            res = np.random.choice(["Great!", "Awesome!", "Good to know!", "Alright!", "Cool!"])
        elif any(i in ai.text.lower() for i in ["i don't understand", "confused", "clarify", "explain"]):
            res = np.random.choice(["I'm here to help! What part are you confused about?", "Can you tell me more about what you need clarification on?", "I'll do my best to explain. What exactly are you having trouble with?", "Let's figure this out together. What do you need help with?"])
        
        elif any(i in ai.text.lower() for i in ["order status", "track order", "order update"]):
            res = np.random.choice(["You can track your order using the tracking number sent to your email.", "Let me check the status of your order. Could you provide your order number?", "Your order is being processed. We will notify you once it's shipped."])

        elif any(i in ai.text.lower() for i in ["return", "refund", "exchange"]):
            res = np.random.choice(["You can initiate a return or exchange through our returns portal on the website.", "Please provide your order number and the item you wish to return or exchange.", "Our return policy allows for returns within 30 days of purchase."])

        elif any(i in ai.text.lower() for i in ["complaint", "issue", "problem", "concern"]):
           res = np.random.choice(["I'm sorry to hear that you're having an issue. Can you describe the problem in detail?", "We take complaints seriously. Please let us know what went wrong.", "Your feedback is important to us. Can you provide more details about your concern?"])

        elif any(i in ai.text.lower() for i in ["billing", "payment", "invoice", "charge"]):
           res = np.random.choice(["For billing inquiries, please provide your invoice number.", "You can view and manage your payments in the billing section of your account.", "Let me help you with your billing issue. Can you provide more details?"])

        elif any(i in ai.text.lower() for i in ["account", "login", "password", "profile"]):
           res = np.random.choice(["You can reset your password using the 'Forgot Password' link on the login page.", "To update your profile information, go to the account settings section.", "If you're having trouble logging in, please try resetting your password."])

        elif any(i in ai.text.lower() for i in ["shipping", "delivery", "shipment"]):
           res = np.random.choice(["Our standard shipping time is 5-7 business days.", "You can track your shipment with the tracking number provided in your confirmation email.", "For express delivery options, please visit our shipping information page."])

        elif any(i in ai.text.lower() for i in ["product info", "product details", "product question"]):
           res = np.random.choice(["You can find detailed product information on the product page.", "What specific details are you looking for about the product?", "Feel free to ask any questions about the product, and I'll be happy to help."])

        elif any(i in ai.text.lower() for i in ["promotion", "discount", "coupon", "offer"]):
           res = np.random.choice(["You can apply discount codes during checkout.", "Check out our latest promotions on the offers page.", "Do you have a specific promotion or coupon code you need help with?"])

        elif any(i in ai.text.lower() for i in ["contact support", "speak to a representative", "customer service number"]):
           res = np.random.choice(["You can contact our support team via the 'Contact Us' page.", "Our customer service number is available on the contact page.", "Feel free to reach out to us through our live chat for immediate assistance."])

        elif any(i in ai.text.lower() for i in ["feedback", "suggestion", "review", "rate"]):
           res = np.random.choice(["We value your feedback. Please let us know how we can improve.", "You can leave a review on the product page.", "We appreciate your suggestions. What would you like to share?"])

        elif any(i in ai.text.lower() for i in ["cancel order", "order cancellation", "cancel my order"]):
           res = np.random.choice(["You can cancel your order from your account page if it hasn't been shipped yet.", "Please provide your order number so I can assist with the cancellation.", "I'll help you cancel your order. Could you provide more details?"])

        elif any(i in ai.text.lower() for i in ["out of stock", "availability", "backorder"]):
           res = np.random.choice(["Some items may be restocked soon. Please check back later or sign up for notifications.", "Could you tell me which product you're looking for? I can check its availability.", "We can notify you when the item is back in stock. Would you like that?"])

        elif any(i in ai.text.lower() for i in ["warranty", "guarantee", "warranty claim"]):
           res = np.random.choice(["Our products come with a one-year warranty. For more details, please visit our warranty page.", "To file a warranty claim, please provide your order number and the issue.", "I'm here to help with warranty claims. Can you give me more information about the problem?"])

        elif any(i in ai.text.lower() for i in ["technical support", "tech support", "technical issue", "software issue"]):
           res = np.random.choice(["Our technical support team can assist you. Can you describe the issue?", "For technical support, please visit our support page or contact our tech team.", "I'm here to help with technical issues. What seems to be the problem?"])

        elif any(i in ai.text.lower() for i in ["installation", "setup", "how to install", "how to set up"]):
           res = np.random.choice(["You can find installation guides and setup instructions on our website.", "Let me guide you through the installation process. What product are you setting up?", "Our support page has detailed setup instructions. What specific help do you need?"])

        elif any(i in ai.text.lower() for i in ["damaged item", "defective product", "broken item"]):
           res = np.random.choice(["I'm sorry to hear that you received a damaged item. Please provide your order number and a description of the issue.", "For defective products, we offer replacements. Can you share more details about the problem?", "We apologize for the inconvenience. Could you send a picture of the damaged item and your order number?"])

        elif any(i in ai.text.lower() for i in ["gift card", "voucher", "gift certificate"]):
           res = np.random.choice(["You can purchase gift cards on our website.", "To use a gift card, enter the code during checkout.", "If you have a problem with a gift card, please provide the card number and issue."])

        elif any(i in ai.text.lower() for i in ["loyalty program", "rewards", "points", "membership"]):
           res = np.random.choice(["Join our loyalty program to earn rewards on purchases.", "You can check your rewards points in your account.", "Would you like to learn more about our membership benefits?"])

        elif any(i in ai.text.lower() for i in ["subscription", "unsubscribe", "subscribe", "newsletter"]):
           res = np.random.choice(["You can manage your subscription preferences in your account settings.", "To unsubscribe from our newsletter, click the link at the bottom of any email from us.", "Would you like to subscribe to our newsletter for the latest updates and offers?"])

        elif any(i in ai.text.lower() for i in ["store hours", "location", "address", "find us"]):
           res = np.random.choice(["Our store hours and locations can be found on our website.", "We have several locations. Which one are you looking for?", "Please visit our 'Find Us' page for store addresses and hours."])


        elif any(i in ai.text.lower() for i in ["order status", "track order", "order update"]):
            res = np.random.choice(["You can track your order using the tracking number sent to your email.", "Let me check the status of your order. Could you provide your order number?", "Your order is being processed. We will notify you once it's shipped."])

        # Return/Refund/Exchange
        elif any(i in ai.text.lower() for i in ["return", "refund", "exchange"]):
            res = np.random.choice(["You can initiate a return or exchange through our returns portal on the website.", "Please provide your order number and the item you wish to return or exchange.", "Our return policy allows for returns within 30 days of purchase."])

        # Complaint/Issue
        elif any(i in ai.text.lower() for i in ["complaint", "issue", "problem", "concern"]):
            res = np.random.choice(["I'm sorry to hear that you're having an issue. Can you describe the problem in detail?", "We take complaints seriously. Please let us know what went wrong.", "Your feedback is important to us. Can you provide more details about your concern?"])

        # Billing/Payment
        elif any(i in ai.text.lower() for i in ["billing", "payment", "invoice", "charge"]):
            res = np.random.choice(["For billing inquiries, please provide your invoice number.", "You can view and manage your payments in the billing section of your account.", "Let me help you with your billing issue. Can you provide more details?"])

        # Account/Login/Password
        elif any(i in ai.text.lower() for i in ["account", "login", "password", "profile"]):
            res = np.random.choice(["You can reset your password using the 'Forgot Password' link on the login page.", "To update your profile information, go to the account settings section.", "If you're having trouble logging in, please try resetting your password."])

        # Shipping/Delivery
        elif any(i in ai.text.lower() for i in ["shipping", "delivery", "shipment"]):
            res = np.random.choice(["Our standard shipping time is 5-7 business days.", "You can track your shipment with the tracking number provided in your confirmation email.", "For express delivery options, please visit our shipping information page."])

        # Product Info
        elif any(i in ai.text.lower() for i in ["product info", "product details", "product question"]):
            res = np.random.choice(["You can find detailed product information on the product page.", "What specific details are you looking for about the product?", "Feel free to ask any questions about the product, and I'll be happy to help."])

        # Promotion/Discount
        elif any(i in ai.text.lower() for i in ["promotion", "discount", "coupon", "offer"]):
            res = np.random.choice(["You can apply discount codes during checkout.", "Check out our latest promotions on the offers page.", "Do you have a specific promotion or coupon code you need help with?"])

        # Contact Support
        elif any(i in ai.text.lower() for i in ["contact support", "speak to a representative", "customer service number"]):
            res = np.random.choice(["You can contact our support team via the 'Contact Us' page.", "Our customer service number is available on the contact page.", "Feel free to reach out to us through our live chat for immediate assistance."])

        # Feedback
        elif any(i in ai.text.lower() for i in ["feedback", "suggestion", "review", "rate"]):
            res = np.random.choice(["We value your feedback. Please let us know how we can improve.", "You can leave a review on the product page.", "We appreciate your suggestions. What would you like to share?"])

        # Order Cancellation
        elif any(i in ai.text.lower() for i in ["cancel order", "order cancellation", "cancel my order"]):
            res = np.random.choice(["You can cancel your order from your account page if it hasn't been shipped yet.", "Please provide your order number so I can assist with the cancellation.", "I'll help you cancel your order. Could you provide more details?"])

        # Stock Availability
        elif any(i in ai.text.lower() for i in ["out of stock", "availability", "backorder"]):
            res = np.random.choice(["Some items may be restocked soon. Please check back later or sign up for notifications.", "Could you tell me which product you're looking for? I can check its availability.", "We can notify you when the item is back in stock. Would you like that?"])

        # Warranty
        elif any(i in ai.text.lower() for i in ["warranty", "guarantee", "warranty claim"]):
            res = np.random.choice(["Our products come with a one-year warranty. For more details, please visit our warranty page.", "To file a warranty claim, please provide your order number and the issue.", "I'm here to help with warranty claims. Can you give me more information about the problem?"])

        # Technical Support
        elif any(i in ai.text.lower() for i in ["technical support", "tech support", "technical issue", "software issue"]):
            res = np.random.choice(["Our technical support team can assist you. Can you describe the issue?", "For technical support, please visit our support page or contact our tech team.", "I'm here to help with technical issues. What seems to be the problem?"])

        # Installation/Setup
        elif any(i in ai.text.lower() for i in ["installation", "setup", "how to install", "how to set up"]):
            res = np.random.choice(["You can find installation guides and setup instructions on our website.", "Let me guide you through the installation process. What product are you setting up?", "Our support page has detailed setup instructions. What specific help do you need?"])

        # Damaged/Defective Item
        elif any(i in ai.text.lower() for i in ["damaged item", "defective product", "broken item"]):
            res = np.random.choice(["I'm sorry to hear that you received a damaged item. Please provide your order number and a description of the issue.", "For defective products, we offer replacements. Can you share more details about the problem?", "We apologize for the inconvenience. Could you send a picture of the damaged item and your order number?"])

        # Gift Card/Voucher
        elif any(i in ai.text.lower() for i in ["gift card", "voucher", "gift certificate"]):
            res = np.random.choice(["You can purchase gift cards on our website.", "To use a gift card, enter the code during checkout.", "If you have a problem with a gift card, please provide the card number and issue."])

        # Loyalty Program
        elif any(i in ai.text.lower() for i in ["loyalty program", "rewards", "points", "membership"]):
            res = np.random.choice(["Join our loyalty program to earn rewards on purchases.", "You can check your rewards points in your account.", "Would you like to learn more about our membership benefits?"])

        # Subscription/Newsletter
        elif any(i in ai.text.lower() for i in ["subscription", "unsubscribe", "subscribe", "newsletter"]):
            res = np.random.choice(["You can manage your subscription preferences in your account settings.", "To unsubscribe from our newsletter, click the link at the bottom of any email from us.", "Would you like to subscribe to our newsletter for the latest updates and offers?"])

        # Store Info
        elif any(i in ai.text.lower() for i in ["store hours", "location", "address", "find us"]):
            res = np.random.choice(["Our store hours and locations can be found on our website.", "We have several locations. Which one are you looking for?", "Please visit our 'Find Us' page for store addresses and hours."])

        # Service Hours
        elif any(i in ai.text.lower() for i in ["service hours", "business hours", "operating hours", "support hours"]):
            res = np.random.choice(["Our customer service hours are listed on our contact page.", "We are available to assist you during our business hours.", "Our support team is available Monday through Friday, 9 AM to 5 PM."])

        # Shipping Cost
        elif any(i in ai.text.lower() for i in ["shipping cost", "delivery fee", "shipping charges", "delivery charges"]):
            res = np.random.choice(["Shipping costs are calculated at checkout based on your location and order size.", "You can view the shipping charges in your cart before completing the purchase.", "For detailed shipping rates, please visit our shipping information page."])

        # International Shipping
        elif any(i in ai.text.lower() for i in ["international shipping", "global delivery", "overseas shipping", "worldwide shipping"]):
            res = np.random.choice(["We offer international shipping to many countries. Please check our shipping policy for details.", "International shipping rates are calculated at checkout.", "For information on international shipping, please visit our shipping information page."])

        # Bulk Orders
        elif any(i in ai.text.lower() for i in ["bulk order", "large quantity", "wholesale", "bulk purchase"]):
            res = np.random.choice(["For bulk orders, please contact our sales team.", "We offer discounts for large quantity purchases. Please reach out for more information.", "To place a bulk order, visit our wholesale section or contact customer service."])

        # Customization
        elif any(i in ai.text.lower() for i in ["customization", "personalize", "custom order", "special request"]):
            res = np.random.choice(["We offer customization options for select products. Please check the product page for details.", "For custom orders, please contact our support team with your requirements.", "We can personalize certain items. What customization are you looking for?"])

        # Payment Methods
        elif any(i in ai.text.lower() for i in ["payment methods", "accepted payments", "pay by card", "pay by paypal"]):
            res = np.random.choice(["We accept various payment methods including credit cards, PayPal, and more.", "You can view all accepted payment methods at checkout.", "For more information on payment options, please visit our payment information page."])

        # Invoice Request
        elif any(i in ai.text.lower() for i in ["invoice request", "billing statement", "request invoice", "request receipt"]):
            res = np.random.choice(["You can request an invoice through your account order history.", "Please provide your order number to receive a billing statement.", "Invoices are sent via email after purchase. Check your inbox or spam folder."])

        # Product Comparison
        elif any(i in ai.text.lower() for i in ["product comparison", "compare products", "difference between products", "product features"]):
            res = np.random.choice(["You can compare products on our website using the comparison tool.", "What specific products would you like to compare?", "Our product pages have detailed features and specifications for comparison."])

        # Size Guide
        elif any(i in ai.text.lower() for i in ["size guide", "size chart", "fit guide", "size measurement"]):
            res = np.random.choice(["You can find size guides on the product page.", "Please refer to our size chart to ensure the best fit.", "If you're unsure about the size, our fit guide can help you choose the right one."])

        # Color Options
        elif any(i in ai.text.lower() for i in ["color options", "available colors", "product colors", "color choices"]):
            res = np.random.choice(["The available colors for each product are listed on the product page.", "Which product color are you interested in?", "You can select the color option before adding the product to your cart."])

        # Material Information
        elif any(i in ai.text.lower() for i in ["material info", "product material", "what is it made of", "material details"]):
            res = np.random.choice(["Material information is provided in the product description.", "What specific material details are you looking for?", "Our product pages include information about the materials used."])

        # Environmental Impact
        elif any(i in ai.text.lower() for i in ["environmental impact", "sustainability", "eco-friendly", "green products"]):
            res = np.random.choice(["We are committed to sustainability. You can learn more about our efforts on our sustainability page.", "Many of our products are eco-friendly. Check the product details for more information.", "For questions about our environmental impact, please visit our eco-friendly initiatives page."])

        # Return Policy
        elif any(i in ai.text.lower() for i in ["return policy", "refund policy", "exchange policy", "return terms"]):
            res = np.random.choice(["Our return policy allows for returns within 30 days of purchase.", "You can find our return policy on the returns page.", "Please review our refund and exchange policy for detailed information."])

        # Privacy Policy
        elif any(i in ai.text.lower() for i in ["privacy policy", "data privacy", "information security", "personal data"]):
            res = np.random.choice(["Our privacy policy is available on our website.", "We take data privacy seriously. You can read about our practices in our privacy policy.", "For information on how we protect your personal data, please visit our privacy policy page."])

        # Terms of Service
        elif any(i in ai.text.lower() for i in ["terms of service", "user agreement", "service terms", "terms and conditions"]):
            res = np.random.choice(["Our terms of service are available on our website.", "Please review our terms and conditions for detailed information.", "You can find our user agreement on the terms of service page."])

        # Order Modifications
        elif any(i in ai.text.lower() for i in ["modify order", "change order", "update order", "edit order"]):
            res = np.random.choice(["You can modify your order if it hasn't been shipped yet. Please visit your order history.", "For changes to your order, contact customer support with your order number.", "I'm here to help with order modifications. What changes would you like to make?"])

        # Backorder Information
        elif any(i in ai.text.lower() for i in ["backorder info", "pre-order", "advance order", "future availability"]):
            res = np.random.choice(["You can place a pre-order for items that are on backorder.", "For information on advance orders, please visit our backorder page.", "We'll notify you when the item is available. Would you like to proceed with a pre-order?"])

        # Store Pickup
        elif any(i in ai.text.lower() for i in ["store pickup", "in-store pickup", "pickup order", "collect in store"]):
            res = np.random.choice(["You can choose store pickup at checkout.", "For in-store pickup, please wait for the confirmation email before coming to the store.", "Visit our store pickup page for more information."])

        # Gift Wrapping
        elif any(i in ai.text.lower() for i in ["gift wrapping", "gift wrap", "wrapping service", "wrap my order"]):
            res = np.random.choice(["We offer gift wrapping services at checkout.", "Would you like to add gift wrapping to your order?", "You can choose the gift wrap option on the product page."])

        # Product Recommendations
        elif any(i in ai.text.lower() for i in ["product recommendations", "suggest products", "what should I buy", "recommend something"]):
            res = np.random.choice(["Based on your interests, I recommend checking out our bestsellers.", "What type of product are you looking for? I can suggest some options.", "You can find personalized recommendations on your account dashboard."])

        # User Manuals
        elif any(i in ai.text.lower() for i in ["user manual", "instruction booklet", "how to use", "user guide"]):
            res = np.random.choice(["User manuals are available for download on the product page.", "Please visit our support section for user guides and instruction booklets.", "What product do you need a manual for? I can help you find it."])

        # Software Updates
        elif any(i in ai.text.lower() for i in ["software update", "firmware update", "update product", "latest version"]):
            res = np.random.choice(["You can download the latest software updates from our website.", "Check the product page for firmware update instructions.", "Would you like help updating your product software?"])

        # Troubleshooting
        elif any(i in ai.text.lower() for i in ["troubleshooting", "fix issue", "product not working", "solve problem"]):
            res = np.random.choice(["Please describe the issue you're experiencing, and I'll help you troubleshoot.", "Our support page has troubleshooting guides for common problems.", "What seems to be the problem with your product? I'll do my best to assist."])

        # Reset Instructions
        elif any(i in ai.text.lower() for i in ["reset instructions", "how to reset", "factory reset", "reset device"]):
            res = np.random.choice(["You can find reset instructions in the user manual or on our support page.", "Would you like me to guide you through the reset process?", "Please provide the product model for specific reset instructions."])

        # Track Package
        elif any(i in ai.text.lower() for i in ["track package", "where is my package", "package status", "package tracking"]):
            res = np.random.choice(["You can track your package using the tracking number provided in your confirmation email.", "Please visit the tracking page and enter your tracking number for the latest status.", "Do you have your tracking number? I can help you check the status of your package."])

        # Cancellation Policy
        elif any(i in ai.text.lower() for i in ["cancellation policy", "order cancellation terms", "cancel order rules", "cancel terms"]):
            res = np.random.choice(["Our cancellation policy is detailed on the order policy page.", "You can cancel your order within a specific time frame. Please check our cancellation terms.", "For detailed cancellation rules, please visit our policy page."])

        # Gift Card Balance
        elif any(i in ai.text.lower() for i in ["gift card balance", "check balance", "remaining balance", "card balance"]):
            res = np.random.choice(["You can check your gift card balance on our website.", "Please enter your gift card number on the balance check page.", "Do you have your gift card number? I can help you check the remaining balance."])

        # Lost Package
        elif any(i in ai.text.lower() for i in ["lost package", "missing package", "did not receive", "package not delivered"]):
            res = np.random.choice(["I'm sorry to hear your package is missing. Please provide your order number for assistance.", "If your package is lost, we will investigate and resolve the issue. Please contact support.", "You can report a missing package through our support page."])

        # Wrong Item Received
        elif any(i in ai.text.lower() for i in ["wrong item", "received incorrect item", "wrong product", "incorrect order"]):
            res = np.random.choice(["I apologize for the error. Please provide your order number and details of the incorrect item.", "We'll send you the correct item. Please contact support with your order number.", "You can initiate a return for the wrong item and we'll send the right one."])

        # Expedited Shipping
        elif any(i in ai.text.lower() for i in ["expedited shipping", "rush delivery", "fast shipping", "priority shipping"]):
           res = np.random.choice(["We offer expedited shipping options at checkout.", "For rush delivery, please select the expedited shipping option during checkout.", "Visit our shipping information page for details on priority shipping."])
 
        # Product Registration
        elif any(i in ai.text.lower() for i in ["product registration", "register product", "warranty registration", "register item"]):
            res = np.random.choice(["You can register your product on our website.", "Please visit the product registration page to complete your registration.", "What product would you like to register? I can help you with the process."])

        # Product Recall
        elif any(i in ai.text.lower() for i in ["product recall", "safety recall", "recall notice", "recalled item"]):
            res = np.random.choice(["We provide recall information on our safety page.", "If you have a recalled item, please contact support for further instructions.", "Please visit our recall notice page for more details."])

        # Product Upgrade
        elif any(i in ai.text.lower() for i in ["product upgrade", "upgrade options", "new version", "latest model"]):
            res = np.random.choice(["You can upgrade to the latest model through our upgrade program.", "Check the product page for upgrade options and details.", "Would you like to learn more about upgrading your product?"])

        # Payment Error
        elif any(i in ai.text.lower() for i in ["payment error", "transaction failed", "payment issue", "payment not processed"]):
            res = np.random.choice(["I'm sorry to hear about the payment error. Please try again or contact your bank.", "For payment issues, check your card details and try again.", "You can contact our support team for assistance with payment errors."])

        # Refund Status
        elif any(i in ai.text.lower() for i in ["refund status", "refund update", "where is my refund", "refund processing"]):
            res = np.random.choice(["You can check the status of your refund in your account order history.", "Refunds typically take 5-7 business days to process.", "For refund updates, please contact our support team with your order number."])

        # Secure Checkout
        elif any(i in ai.text.lower() for i in ["secure checkout", "payment security", "checkout safety", "safe payment"]):
            res = np.random.choice(["Our checkout process is secure and encrypted to protect your information.", "You can shop with confidence knowing our payment process is safe.", "For more information on payment security, please visit our secure checkout page."])

        # Seasonal Offers
        elif any(i in ai.text.lower() for i in ["seasonal offers", "holiday sale", "special discounts", "limited time offer"]):
            res = np.random.choice(["Check out our seasonal offers page for the latest deals.", "We have special discounts during holidays. Don't miss out!", "Would you like to know more about our limited-time offers?"])

        # Accessibility
        elif any(i in ai.text.lower() for i in ["accessibility", "accessible services", "disabled access", "access for all"]):
            res = np.random.choice(["We are committed to accessibility. You can learn more on our accessibility page.", "For accessible services, please visit our support page.", "Do you need help with accessibility options? We are here to assist."])

        # Store Policies
        elif any(i in ai.text.lower() for i in ["store policies", "shop policies", "store rules", "shop guidelines"]):
            res = np.random.choice(["You can find our store policies on the policies page.", "Please review our shop guidelines for detailed information.", "For store rules and policies, visit our policy page."])

        # Partner Inquiries
        elif any(i in ai.text.lower() for i in ["partner inquiries", "business partnership", "collaboration", "affiliate program"]):
            res = np.random.choice(["For partnership inquiries, please contact our business development team.", "We welcome collaborations. Please visit our affiliate program page for more details.", "Interested in partnering with us? Reach out through our contact page."])

        # Gift Ideas
        elif any(i in ai.text.lower() for i in ["gift ideas", "gift suggestions", "present ideas", "what to gift"]):
            res = np.random.choice(["Looking for gift ideas? Check out our gift guide page.", "We have curated gift suggestions for every occasion.", "Need help with gift ideas? I can suggest some popular options."])

        # Technical Documentation
        elif any(i in ai.text.lower() for i in ["technical documentation", "spec sheets", "tech specs", "technical details"]):
            res = np.random.choice(["You can find technical documentation on the product page.", "For spec sheets and technical details, visit our support section.", "What specific technical information are you looking for?"])

        # Lost Password
        elif any(i in ai.text.lower() for i in ["lost password", "forgot password", "reset password", "password help"]):
            res = np.random.choice(["You can reset your password using the 'Forgot Password' link on the login page.", "Please visit our password recovery page to reset your password.", "Need help with your password? I'll guide you through the reset process."])

        # Browser Compatibility
        elif any(i in ai.text.lower() for i in ["browser compatibility", "supported browsers", "website issues", "browser support"]):
            res = np.random.choice(["Our website supports most major browsers. Please update to the latest version.", "For best performance, use an updated browser.", "Having issues with the website? Try clearing your browser cache or switching browsers."])

        # Order Confirmation
        elif any(i in ai.text.lower() for i in ["order confirmation", "confirm my order", "order receipt", "order acknowledgment"]):
            res = np.random.choice(["You should receive an order confirmation email shortly after purchase.", "Please check your inbox and spam folder for the order confirmation.", "If you haven't received an order confirmation, please contact support with your order details."])
        elif any(i in ai.text for i in ["exit","close"]):
            res = np.random.choice(["Tata","Have a good day","Bye","Goodbye","Hope to meet soon","peace out!"])
            ex=False
        ## conversation
        else:   
            if ai.text=="ERROR":
                res="Sorry, come again?"
            else:
                chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
                res = str(chat)
                res = res[res.find("bot >> ")+6:].strip()
        ai.text_to_speech(res)
    print("----- Closing down Fares -----")