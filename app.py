# importing all libraries
import streamlit as st 
import google.generativeai as genai 
from youtube_transcript_api import YouTubeTranscriptApi

# generate your API Key and add here to configure
gemini_api_key = ''
genai.configure(api_key= gemini_api_key)


# to get the transcript
def fetch_transcript_details(youtube_video_url):
    try :
        # get video id
        video_id = youtube_video_url.split('=')[1][:11]
        # get transcript
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        # transcript is a list so join all the elements of the list
        transcript = ''
        for i in transcript_text:
            transcript += ' ' + i['text']

        return transcript

    except:
        return 0
        
# generate summary using 'Gemini-Pro' Model
def generate_gemini_content(transcript, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt + transcript)

    return response.text


# creating a prompt to get most relevent outputs
prompt = '''
You are a Youtube video summarizer, taking the transcript text and summarizing the entire video and providing the important summary in approximately 250 words also give some necessary formula if mentioned in transcript. 

Please provide summary of Transcript given here: 

'''

# title to our app
st.title('Youtube Transcript to Detailed Notes Converter')
# get youtube video link as input
youtube_link = st.text_input('Enter YouTube video link : ')

# get the image of video corrosponding to given link
if youtube_link:
    video_id = youtube_link.split('=')[1][:11]
    st.image(f'http://img.youtube.com/vi/{video_id}/0.jpg', use_column_width=True)

# creating a button to generate output on clicking
if st.button('Get  Summary'):
    transcript = fetch_transcript_details(youtube_link)

    if transcript == 0:
        st.write('No Transcript Available')

    if transcript:
        summary = generate_gemini_content(transcript, prompt)
        st.write(summary)

# creating a button to clear output on clicking
if st.button('Clear Summary'):
    summary = ' '




