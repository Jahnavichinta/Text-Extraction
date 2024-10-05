# 📸 Multilingual OCR Streamlit Application

## 📖 Table of Contents
📸 Multilingual OCR Streamlit Application
📚 Description
✨ Features
🛠️ Technologies Used
🚀 Demo
📋 Installation
🖥️ Usage
Running the App Locally
Using the Application
🌐 Deployment
🔍 Features Overview

## Prerequisites
Clone the Repository
Set Up a Virtual Environment

# 📚 Description
The Multilingual OCR Streamlit Application is a user-friendly web application that leverages EasyOCR and Streamlit to extract text from images containing English, Hindi, or both languages. It allows users to upload an image, extract the embedded text, search for specific keywords within the extracted content, and highlights the matching sections in green for easy identification.


# ✨ Features
Image Upload: Supports JPG, JPEG, PNG, and BMP formats.
Language Selection: Choose to extract English only, Hindi only, or both languages simultaneously.
Grayscale Conversion: Automatically converts uploaded images to grayscale to enhance OCR accuracy.
Text Extraction: Extracts text from images using EasyOCR.
Keyword Search: Enter keywords to search within the extracted text.
Highlighted Results: Displays search results with matching keywords highlighted in green.
Download Option: Download the extracted text as a .txt file.
Responsive UI: Clean and intuitive interface built with Streamlit.


# 🛠️ Technologies Used
Streamlit: For building the web application interface.
EasyOCR: For Optical Character Recognition (OCR) to extract text from images.
Pillow: For image handling and processing.
OpenCV: For image preprocessing tasks like grayscale conversion.
NumPy: For numerical operations on image data.
Regular Expressions (re): For keyword search and highlighting.
Git: For version control.
GitHub: For hosting the repository and deploying the app.

# 🚀 Demo
Live Demo: Access the live application https://text-extraction-nkcwyckfbiqj3yzdxkttkj.streamlit.app/.

## 📋 Installation
Prerequisites
Python 3.7 or higher installed on your machine.
Git installed for version control. 

# 🖥️ Usage
Running the App Locally
After installing the dependencies, you can run the Streamlit app locally.
streamlit run app.py

# Using the Application
## Upload an Image:

Click on the "📂 Choose an image..." button.
Select an image file in JPG, JPEG, PNG, or BMP format containing English, Hindi, or both languages.
Select Language(s):

In the sidebar, choose whether to extract English, Hindi, or both languages.
View Extracted Text:

The uploaded image will be displayed along with its grayscale version.
Extracted text from the image will appear in the "📝 Extracted Text" section.
Search for Keywords:

Enter one or more keywords separated by commas in the "🔍 Search Keywords" input field.
Matching keywords within the extracted text will be highlighted in green in the "🔍 Search Results" section.
Download Extracted Text:

Click on the "📥 Download Text" button to download the extracted text as a .txt file.

# 🌐 Deployment
Deploying on Streamlit Community Cloud
Streamlit Community Cloud is a free platform to deploy your Streamlit apps.

Push Your Code to GitHub:
Create a requirements.txt File:

Ensure all dependencies are listed. Refer to the Installation section.
Sign in to Streamlit Community Cloud:

Visit Streamlit Community Cloud and sign in with your GitHub account.
Deploy Your App:

Click on "New app".
Select your repository (Text-Extraction) and branch (main).
Specify the main file as app.py.
Click "Deploy".
Monitor Deployment:

Streamlit will install the dependencies from requirements.txt and launch your app.
Visit the provided URL to access your live application.
