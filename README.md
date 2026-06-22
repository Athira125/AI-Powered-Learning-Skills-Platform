# AI-Powered-Learning-Skills-Platform
AI-powered learning platform that converts handwritten/image notes into text using OCR, summarizes content, reads it aloud, and generates quizzes, flashcards, study tips, and keywords using Streamlit, Tesseract OCR, Ollama, and gTTS.

## Project Overview
The AI-Powered Learning Skills Platform is a Streamlit-based application designed to help students learn more effectively from image-based notes. The system allows users to upload note images, extract text using OCR, summarize the content using AI, listen to the summary, and generate study materials such as quizzes, flashcards, study tips, and keywords.

## Features
- Upload notes as image files
- Extract text from notes using Tesseract OCR
- Generate summary of notes using Ollama
- Read the generated summary aloud using gTTS
- Generate quiz questions
- Generate flashcards
- Generate study tips
- Generate important keywords / key points
- Download summary as text file
- Download quiz as text file
- Download flashcards as text file

## Technologies Used
- Python
- Streamlit
- PyTesseract
- Tesseract OCR
- Pillow
- gTTS
- Ollama

## How to Run the Project
1. Install Python and required packages.
2. Install Tesseract OCR and make sure its path is configured.
3. Install Ollama and pull the required model.
4. Open terminal in the project folder.
5. Run:
   ```bash
   python -m streamlit run app.py
