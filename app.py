import streamlit as st
import argostranslate.translate

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages easily.")

languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

text = st.text_area(
    "Enter the text you want to translate:",
    placeholder="Type your text here..."
)

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "Target Language",
        list(languages.keys())
    )

if st.button("Translate", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text to translate.")

    elif source_language == target_language:
        st.warning("Please choose two different languages.")

    else:
        try:
            installed_languages = (
                argostranslate.translate.get_installed_languages()
            )

            source_code = languages[source_language]
            target_code = languages[target_language]

            source = next(
                lang for lang in installed_languages
                if lang.code == source_code
            )

            target = next(
                lang for lang in installed_languages
                if lang.code == target_code
            )

            translation = source.get_translation(target)

            with st.spinner("Translating..."):
                translated_text = translation.translate(text)

            st.subheader("Translation Result")
            st.success(translated_text)

        except Exception as error:
            st.error("Translation failed.")
            st.caption(f"Technical details: {error}")