import streamlit as st
from pytube import YouTube
from utilities import get_yt, transcribe_yt
from PIL import Image


st.image("https://amarnani.000webhostapp.com/wp-content/uploads/2024/01/cropped-668579e4-fb37-40bd-b367-03a829bf0193-1-scaled-1.jpg")
st.markdown('# 📝 ** Content extraction App** ')
st.markdown('-created by amaresh')
st.warning('waiting for URL input in the left sidebar.')


# Sidebar
st.sidebar.header('Input parameter')

with st.sidebar.form(key='my_form'):
	URL = st.text_input('Enter URL of YouTube video:')
	submit_button = st.form_submit_button(label='Go')

# Run custom functions if URL is entered 
if submit_button:
    get_yt(URL)
    transcribe_yt()

    with open("transcription.zip", "rb") as zip_download:
        btn = st.download_button(
            label="Download ZIP",
            data=zip_download,
            file_name="transcription.zip",
            mime="application/zip"
        )

with st.sidebar.expander('Example URL'):
	st.markdown("example of youtube video:The Brief history of ai")
	st.code('https://youtu.be/056v4OxKwlI?si=AnhcUiYMwSFd4Gbe')
