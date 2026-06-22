import streamlit as st
import pytesseract
from PIL import Image
import subprocess
from gtts import gTTS

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if "ocr_text" not in st.session_state:
    st.session_state["ocr_text"] = ""
if "summary" not in st.session_state:
    st.session_state["summary"]=""
if "quiz" not in st.session_state:
    st.session_state["quiz"] = ""
if "flashcards" not in st.session_state:
    st.session_state["flashcards"] = ""
if "study_tips" not in st.session_state:
    st.session_state["study_tips"] = ""
if "keywords" not in st.session_state:
    st.session_state["keywords"] = ""

st.title("AI-Powered Learning Skills Platform")

st.header("Upload Notes")

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.success("Notes uploaded successfully!")

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Notes", use_container_width=True)

    if st.button("Extract Text"):
        extracted_text = pytesseract.image_to_string(image)
        st.session_state["ocr_text"] = extracted_text

    if st.session_state["ocr_text"] != "":
        st.subheader("OCR Result")
        st.text_area("Extracted Text", st.session_state["ocr_text"], height=250)

        if st.button("Summarize Notes"):
             prompt = f"Summarize the following study notes in simple points:\n\n{st.session_state['ocr_text']}"

             result = subprocess.run(
              ["ollama", "run", "llama3.2", prompt],
               capture_output=True,
                text=True,
                encoding="utf-8"
        )

             st.session_state["summary"] = result.stdout

if st.session_state["summary"] != "":
    st.subheader("Summary")
    st.text_area("Generated Summary", st.session_state["summary"], height=250)
    st.download_button(
        label="Download Summary",
        data=st.session_state["summary"],
        file_name="summary.txt",
        mime="text/plain"
    )

    if st.button("Read Summary Aloud"):
        tts = gTTS(st.session_state["summary"])
        tts.save("summary.mp3")

        audio_file = open("summary.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    if st.button("Generate Quiz"):
        quiz_prompt = f"Create 3 simple study questions from the following summary:\n\n{st.session_state['summary']}"

        quiz_result = subprocess.run(
            ["ollama", "run", "llama3.2", quiz_prompt],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        st.session_state["quiz"] = quiz_result.stdout

    if st.session_state["quiz"] != "":
        st.subheader("Quiz Questions")
        st.text_area("Generated Quiz", st.session_state["quiz"], height=250)
        st.download_button(
        label="Download Quiz",
        data=st.session_state["quiz"],
        file_name="quiz.txt",
        mime="text/plain"
    )
    if st.button("Generate Flashcards"):
        flashcard_prompt = f"Create 3 simple flashcards in Question-Answer format from the following summary:\n\n{st.session_state['summary']}"

        flashcard_result = subprocess.run(
            ["ollama", "run", "llama3.2", flashcard_prompt],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        st.session_state["flashcards"] = flashcard_result.stdout
    if st.session_state["flashcards"] != "":
        st.subheader("Flashcards")
        st.text_area("Generated Flashcards", st.session_state["flashcards"], height=250)
        st.download_button(
        label="Download Flashcards",
        data=st.session_state["flashcards"],
        file_name="flashcards.txt",
        mime="text/plain"
    )
    if st.button("Generate Study Tips"):
        tips_prompt = f"Give 5 simple study tips for learning the following topic:\n\n{st.session_state['summary']}"

        tips_result = subprocess.run(
            ["ollama", "run", "llama3.2", tips_prompt],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        st.session_state["study_tips"] = tips_result.stdout
    if st.session_state["study_tips"] != "":
        st.subheader("Study Tips")
        st.text_area("Generated Study Tips", st.session_state["study_tips"], height=250)
    if st.button("Generate Keywords"):
        keyword_prompt = f"Extract 8 important keywords or key points from the following study summary:\n\n{st.session_state['summary']}"

        keyword_result = subprocess.run(
            ["ollama", "run", "llama3.2", keyword_prompt],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        st.session_state["keywords"] = keyword_result.stdout
    if st.session_state["keywords"] != "":
        st.subheader("Important Keywords / Key Points")
        st.text_area("Generated Keywords", st.session_state["keywords"], height=200)