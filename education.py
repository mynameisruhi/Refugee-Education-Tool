# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 14:14:35 2025

@author: rahul
"""
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your variables
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

language = input("What language do you speak? ")

def translateToEnglish(text):
    translated = model.generate_content(f"Translate the following text from {language} to English: {text}. ONLY RETURN THE TRANSLATION.");
    return translated.text

def translateToLanguage(text):
    translated = model.generate_content(f"Translate the following text from English to {language}: {text}. ONLY RETURN THE TRANSLATION.");
    return translated.text

subject = "What do you want to learn? For example, type angles in geometry, how to expand an algebraic equation, kinematics in physics, the Cold War, or any other topic."
subject = translateToLanguage(subject)

subjectText = input(subject)
subjectText = translateToEnglish(subjectText)

lesson = model.generate_content(f"Teach the following subject: {subjectText}.")
lesson = translateToLanguage(lesson.text)

print(lesson)

def extraHelp():
    concerns = input(translateToLanguage("Press the letter q on your keyboard if you have additional questions. Otherwise, press the letter t to proceed to a 10 question test"))
    return concerns

concerns = extraHelp()
while(concerns=="q"):
    question = input(translateToLanguage("What question do you have?"))
    question = translateToEnglish(question)
    answer = model.generate_content(f"Answer the following question: {question}")
    print(translateToLanguage(answer.text))
    concerns = extraHelp()
    
test = model.generate_content(f"Create a 10 question test over the following topic: {subjectText}. Provide the answer key at the end as well.")
print(translateToLanguage(test.text))
