# Import all necessary libraries
import google.generativeai as genai  # Import Google's Generative AI library for text generation
from dotenv import load_dotenv  # Import dotenv to load environment variables from a .env file
import os  # Import os to interact with the operating system

# Load environment variables from .env file
load_dotenv()

# Access your API key from environment variables
api_key = os.getenv("API_KEY")

# Configure the generative AI model with the API key
genai.configure(api_key=api_key)

# Initialize the generative AI model
model = genai.GenerativeModel("gemini-1.5-flash")

# Ask the user for their preferred language
language = input("What language do you speak? ")

# Function to translate text from the user's language to English
def translateToEnglish(text):
    translated = model.generate_content(f"Translate the following text from {language} to English: {text}. ONLY RETURN THE TRANSLATION.")
    return translated.text

# Function to translate text from English to the user's language
def translateToLanguage(text):
    translated = model.generate_content(f"Translate the following text from English to {language}: {text}. ONLY RETURN THE TRANSLATION.")
    return translated.text

# Ask the user what topic they want to learn about
subject = "What do you want to learn? For example, type angles in geometry, how to expand an algebraic equation, kinematics in physics, the Cold War, or any other topic."
subject = translateToLanguage(subject)  # Translate the prompt into the user's language

# Get user input for the subject they want to learn
subjectText = input(subject)
subjectText = translateToEnglish(subjectText)  # Translate the user's response to English

# Generate a lesson on the chosen topic
lesson = model.generate_content(f"Teach the following subject: {subjectText}.")
lesson = translateToLanguage(lesson.text)  # Translate the lesson into the user's language

# Display the lesson
print(lesson)

# Function to check if the user needs additional help
def extraHelp():
    concerns = input(translateToLanguage("Press the letter q on your keyboard if you have additional questions. Otherwise, press the letter t to proceed to a 10 question test"))
    return concerns

# Ask the user if they need additional help
concerns = extraHelp()
while concerns == "q":  # If the user has more questions, continue the loop
    # Ask the user to type their question
    question = input(translateToLanguage("What question do you have?"))
    question = translateToEnglish(question)  # Translate the question to English
    
    # Generate an answer to the user's question
    answer = model.generate_content(f"Answer the following question: {question}")
    
    # Display the translated answer
    print(translateToLanguage(answer.text))
    
    # Ask again if the user has more questions
    concerns = extraHelp()

# Generate a 10-question test on the chosen topic, including an answer key
test = model.generate_content(f"Create a 10 question test over the following topic: {subjectText}. Provide the answer key at the end as well.")

# Display the translated test
print(translateToLanguage(test.text))

