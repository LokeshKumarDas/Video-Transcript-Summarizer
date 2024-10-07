import streamlit as st 
import google.generativeai as genai 
from youtube_transcript_api import YouTubeTranscriptApi

gemini_api_key = 'AIzaSyAg3rt1XLVnxXe-rL2w4BzFhlbBhMkt0-g'
genai.configure(api_key= gemini_api_key)

def fetch_transcript_details(youtube_video_url):
    try :
        video_id = youtube_video_url.split('=')[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ''
        for i in transcript_text:
            transcript += ' ' + i['text']

        return transcript

    except:
        return 0
        

def generate_gemini_content(transcript, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt + transcript)

    return response.text


prompt = '''
You are a Youtube video summarizer, taking the transcript text and summarizing the entire video and providing the important summary in approximately 250 words also give some necessary formula if mentioned in transcript. 

Please provide summary of Transcript given here: 

'''


st.title('Youtube Transcript to Detailed Notes Converter')
youtube_link = st.text_input('Enter YouTube video link : ')

if youtube_link:
    video_id = youtube_link.split('=')[1][:11]
    st.image(f'http://img.youtube.com/vi/{video_id}/0.jpg', use_column_width=True)

if st.button('Get  Summary'):
    transcript = fetch_transcript_details(youtube_link)

    if transcript == 0:
        st.write('No Transcript Available')

    if transcript:
        summary = generate_gemini_content(transcript, prompt)
        st.write(summary)

if st.button('Clear Summary'):
    summary = ' '




