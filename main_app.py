import  streamlit as st 
import numpy as np 
import pandas as pd 
import requests
import openai

from streamlit_chat import message
from streamlit_lottie import st_lottie

openai.api_key = st.secrets["password"]

# Page config
st.set_page_config(page_title = "TextoVator", page_icon = ":kiss:", layout= "wide")
lotte_file = 'https://assets9.lottiefiles.com/packages/lf20_26KVdO.json'

def load_lottee(lotte_file):
    url = requests.get(lotte_file)
    if url.status_code !=200:
        return None
    return url.json()

def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text

animation = load_lottee(lotte_file = lotte_file)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=.6, # this is the degree of randomness of the model's output
    )
    # print('response we got from the apis is ',response)
    # print('***********************************************************')
    return response.choices[0].message["content"]


# HEADER section

with st.container():
    left,right = st.columns(2)

    with left:
        st.subheader('Textovator') 
        st.title('Textovator')
        st.write('Provide the below inputs - ')
    
    with right:
        st_lottie(animation_data=animation,height=300,key='coding')

## Body 

with st.container():
    st.write('---')

    left,center,right = st.columns((1,2,2))

    with left:
        n_beds = st.text_input('Number of Bedrooms: ')
        n_baths = st.text_input('Number of BathRooms: ')
        n_beds = st.text_input('Number of Beds: ')
        n_city = st.text_input('Nearest major City: ')

    with center: 
        st.write('Please select the following options: ')
        woods = st.checkbox('In Woods')
        sea = st.checkbox('Close To Woods')
        mount = st.checkbox('Close to Mountains')
        sea_fac = st.checkbox('Sea Facing')
        ac = st.checkbox('A/C')
        heat = st.checkbox('Heating')
        bathtub = st.checkbox('Bathtub')
        pat =  st.checkbox('Patio/Balcony')
        pets = st.checkbox('Pets Allowed')

    with right:
        st.write("##")
        pool =  st.checkbox('Pool')
        concierge = st.checkbox('Concierge Service')
        kids = st.checkbox('Kids Amenities')
        clean = st.checkbox('Professinal Cleaning')
        wifi = st.checkbox('High Speed Wifi')
        kitchen = st.checkbox('Kitchen Essentials')
        prem = st.checkbox('Premium Linens and Towels')
        tv = st.checkbox('Television')

    
    st.button('Submit')
    if st.button:
        prop_description = "In Woods, Number of bedrooms=3, Number of bathrooms=2, NUmber of beds=6, Close to Sea, Close to Mountains, \
        Nearest major city =Miami, Sea Facing, Air Conditioning, Heating, Bathtub,Patio/Balcony, Pets allowed, Building elevator,\
        Free parking, Concierge Services,Waterfront, pool, In Person Checkin, Kids Amenities, 24/7 Support, Professional Cleaning, \
        Pre and post stay, High-Speed WiFi, Kitchen Essentials, Cookware, Utensils, Microwave, Starter Kit of Bathroom Amenities, \
        Soap, Shampoo, Hair Dryer, Premium Linens and Towels, Television"

        prompt = f"""
        You are an Assistant for text generation designed to help get \
        the text generated with given properties attributes delimited by ```.

        Instructions: 
        - Make the tone as Persuasive 
        - If the city details are present in the text, share some fun acitivities around that area \
        or a fun fact about the city in the property description.
        - Show the output JSON
            - Property Description = Generate a detailed 600 words property description that highlights its unique features and appeals to \
              potential renters.
            - Headline = Generate a SEO and eye catching headline. 
        - If you're unsure of an answer, you can say "I don't know" or "I'm not sure". 

        - properties attributes: ```{prop_description}```
        """        

        st.write(get_completion(prompt))
    
    clear_button = st.button("Clear All", key="clear")    
    if clear_button:
        st.experimental_rerun()

with st.container():
    st.write('---')
    col1, col2, col3 = st.columns(3)

    with col1:
        clear_button = st.sidebar.button("Clear All", key="clear")    
        if clear_button:
            st.experimental_rerun()

    with col3:
        check = st.button('Help')

        if check:
            if 'generated' not in st.session_state:
                st.session_state['generated'] = []
            if 'past' not in st.session_state:
                st.session_state['past'] = []
            if 'messages' not in st.session_state:
                st.session_state['messages'] = [
                    {"role": "system", "content": "You are a helpful assistant."} ]
            
            with st.form(key='my_form', clear_on_submit=True):
                user_input = st.text_area("You:", key='input', height=100)
                submit_button = st.form_submit_button(label='Send')





