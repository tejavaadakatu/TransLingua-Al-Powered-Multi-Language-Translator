import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Free Translator", page_icon="🌐")
st.title("🌐 Free Language Translator")
st.write("Translate text between multiple languages (No API key required).")

def translate_text(text, source_language, target_language):
    try:
        translated = GoogleTranslator(
            source=source_language,
            target=target_language
        ).translate(text)
        return translated
    except Exception as e:
        return f"Error: {str(e)}"

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-CN"
}

text = st.text_area("✍️ Enter text to translate")

source_language = st.selectbox("Select source language", list(languages.keys()))
target_language = st.selectbox("Select target language", list(languages.keys()))

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter text.")
    else:
        with st.spinner("Translating..."):
            result = translate_text(
                text,
                languages[source_language],
                languages[target_language]
            )
        st.success(result)
