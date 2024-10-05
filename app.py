import streamlit as st
from PIL import Image
import easyocr
import cv2
import numpy as np
import re
import logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@st.cache_resource
def load_reader(languages):
    try:
        reader = easyocr.Reader(languages, gpu=False)
        logging.info(f'EasyOCR Reader initialized with languages: {languages}')
        return reader
    except Exception as e:
        logging.error(f'Error initializing EasyOCR Reader: {e}')
        st.error(f"Error initializing OCR engine: {e}")
        return None

def highlight_keywords(text, keywords):
    if not keywords:
        return text
    escaped_keywords = [re.escape(kw.strip()) for kw in keywords if kw.strip()]
    if not escaped_keywords:
        return text
    pattern = re.compile(r'(' + '|'.join(escaped_keywords) + r')', re.IGNORECASE)
    highlighted_text = pattern.sub(r'**\1**', text)
    return highlighted_text

st.set_page_config(
    page_title="📸 Multilingual OCR Application",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("📸 Multilingual Image to Text OCR Application")
st.write("""
    Upload an image containing English, Hindi, or both languages to extract the text.
    Choose the language(s) you want to extract.
""")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption='📷 Uploaded Image.', use_column_width=True)
        st.write("✅ Image successfully uploaded and displayed.")
        logging.info('Image uploaded and displayed.')

        st.sidebar.header("🗣️ OCR Language Selection")
        languages = {
            'English': 'en',
            'Hindi': 'hi',
            'English + Hindi': 'en+hi'
        }
        selected_language = st.sidebar.selectbox("Choose OCR Language", list(languages.keys()))
        lang_code = languages[selected_language]
        logging.info(f'OCR Languages selected: {selected_language} ({lang_code})')

        with st.spinner('🔍 Initializing OCR engine...'):
            reader = load_reader(lang_code.split('+'))
            if reader is None:
                st.error("Failed to initialize OCR engine. Please check the logs for more details.")
                st.stop()
            st.success('✅ OCR engine initialized.')

        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        logging.info('Converted PIL Image to OpenCV format.')

        image_gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
        st.image(image_gray, caption='Grayscale Image.', use_column_width=True)
        st.write("✅ Converted to Grayscale.")
        logging.info('Converted image to grayscale.')

        with st.spinner('🔍 Extracting text...'):
            results = reader.readtext(image_gray, detail=1, paragraph=False)
            st.success('✅ OCR extraction complete.')
            logging.info(f'OCR extraction complete with {len(results)} results.')

        extracted_text = ""
        confidences = []

        for idx, element in enumerate(results):
            if len(element) == 3:
                bbox, text, confidence = element
                extracted_text += text + " "
                confidences.append(confidence)
                logging.info(f'Text {idx + 1}: {text} | Confidence: {confidence:.2f}%')
            else:
                st.warning(f"⚠️ Unexpected OCR result format at index {idx}: {element}")
                logging.warning(f"Unexpected OCR result format at index {idx}: {element}")

        st.text_area("📝 Extracted Text", extracted_text.strip(), height=300)

        st.header("🔍 Search Keywords")
        keywords_input = st.text_input("Enter keyword(s) to search (separated by commas):")
        if keywords_input:
            keywords = [kw.strip() for kw in keywords_input.split(",") if kw.strip()]
            if keywords:
                highlighted_text = highlight_keywords(extracted_text, keywords)
                st.markdown("**🔍 Search Results:**")
                st.markdown(highlighted_text)
            else:
                st.write("⚠️ Please enter valid keyword(s).")

        if confidences:
            average_conf = sum(confidences) / len(confidences)
            st.write(f"**🔍 Average OCR Confidence:** {average_conf:.2f}%")
            st.progress(average_conf / 100)
            logging.info(f'Average OCR Confidence: {average_conf:.2f}%')
        else:
            st.write("**🔍 OCR Confidence:** Not Available")
            logging.info('No valid confidence scores available.')

        if extracted_text.strip():
            st.download_button(
                label="📥 Download Text",
                data=extracted_text.strip(),
                file_name='extracted_text.txt',
                mime='text/plain',
            )
            logging.info('Download button enabled for extracted text.')

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
        logging.error(f"An error occurred: {e}")
else:
    st.write("📂 Please upload an image file to get started.")
    logging.info('No image uploaded.')
