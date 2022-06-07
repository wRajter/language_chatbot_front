import streamlit as st
from streamlit_chat import message as st_message
from language_chatbot_front.openai_translation_api import bot_translation
import re
import requests

#url = "https://chatbot-ni4mcaftla-ew.a.run.app/reply"

st.set_page_config(page_title="Multilingual Chatbot", page_icon=":computer:", layout="wide")

#dropdown to select language and reload the page
#pass that into generate answer
#add some text explaining consistency problems
#make the output larger


if "history" not in st.session_state:
    st.session_state.history = []

with st.container():
    st.title("Hi, I am your multilingual chatbot :wave:")
    st.subheader("I am here to help you learn a language of your choice :speech_balloon:")
    st.write("---")

st.subheader(":warning: If you want to change the language please reload the page :warning:")

lang_choice = st.selectbox("What language would you like to choose?", options=['No specific language', 'English', 'German', 'Spanish', 'French', 'Italian', 'Dutch', 'Polish', 'Portuguese', 'Slovak'])


st.write("---")

eng_trans = st.checkbox("Would you like an optional English translation?")


def generate_answer(url = "https://chatbot2-ni4mcaftla-ew.a.run.app/reply"):

    key_pairs = {'No specific language': 'no lang', 'English': 'en', 'German' : 'de', 'Spanish' : 'es', 'French' : 'fr', 'Italian' : 'it', 'Dutch' : 'nl', 'Polish' : 'pl', 'Portuguese' : 'pt', 'Slovak' : 'sk',
             'Hungarian' : 'hu'}
    #lang_choice = st.selectbox("What language would you like to choose?", options=['No specific language', 'English', 'German', 'Spanish', 'French', 'Italian', 'Dutch', 'Polish', 'Portuguese', 'Slovak'])
    #lang_choice = st.text_input("Choose a language")
    lang_select = key_pairs[lang_choice]

    user_message = st.session_state.input_text

    # bot translation
    if user_message.lower().startswith('translate'):
        # extracting language that we want to translate to
        pattern_language = '(.*)into\s([A-Za-z]*)'
        language_ = re.search(pattern_language, user_message).group(2)
        # extracting text for the translation
        pattern_text = "(T|t)ranslate\s(.*?)\sinto(.*)"
        text_ = re.search(pattern_text, user_message).group(2)
        # calling openai api through the bot_translation function
        output = bot_translation(text_, language_)

        session_num = len(st.session_state.history)
        st.session_state.history.append({"message": user_message, "is_user": True, 'key': f'u_{session_num}'})
        st.session_state.history.append({"message": output, "is_user": False, 'key': f'b_{session_num}'})

    elif eng_trans == True:
        if lang_select != "en":
            eng_response = requests.get(url, {"text": user_message, "user_language": "en"})
            eng_answer = eng_response.json()
            eng_response = "(" + eng_answer['response'] + ")"

            params = {'text': user_message, "user_language": lang_select}

            response = requests.get(url, params=params)
            answer = response.json()

            output = f'''
            {answer['response']}
            {eng_response}
            '''

            session_num = len(st.session_state.history)
            st.session_state.history.append({"message": user_message, "is_user": True, 'key': f'u_{session_num}'})
            st.session_state.history.append({"message": output, "is_user": False, 'key': f'b_{session_num}'})

        else:
            params = {'text': user_message, "user_language": lang_select}

            response = requests.get(url, params=params)
            answer = response.json()


            response = requests.get(url, params=params)
            answer = response.json()

            session_num = len(st.session_state.history)
            st.session_state.history.append({"message": user_message, "is_user": True, 'key': f'u_{session_num}'})
            st.session_state.history.append({"message": answer['response'], "is_user": False, 'key': f'b_{session_num}'})

    else:
        params = {'text': user_message, "user_language": lang_select}

        response = requests.get(url, params=params)
        answer = response.json()


        response = requests.get(url, params=params)
        answer = response.json()

        session_num = len(st.session_state.history)
        st.session_state.history.append({"message": user_message, "is_user": True, 'key': f'u_{session_num}'})
        st.session_state.history.append({"message": answer['response'], "is_user": False, 'key': f'b_{session_num}'})

st.text_input("Talk to the bot", key="input_text", on_change=generate_answer)

for chat in reversed(st.session_state.history):
    st_message(**chat)
