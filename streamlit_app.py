import streamlit as st
from pytube import YouTube
from utilities import get_yt, transcribe_yt

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
	st.markdown('an example  of Sunny Leone  Stand Up Comedy speech')
	st.code('https://youtu.be/k7HFMq7jKLc?si=Gix5Iq6ejKkyhRcU')
