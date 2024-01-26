import os
import tempfile
import requests
# from dotenv import load_dotenv
from PIL import Image
import streamlit as st
import imghdr
import cv2
from io import BytesIO
from huggingface_hub import from_pretrained_keras
import numpy as np
import tensorflow as tf
from keras import backend as K
import pickle
import matplotlib 

loaded_model = pickle.load(open('trained_model.sav','rb'))




st.set_page_config(page_title="Final Project",layout="wide")

st.image('logo.gif',width=200,)
st.title("Tribhuwan University")
st.subheader("Purwanchal Campus,Dharan")


st.write("---")



    # Add a new sidebar option for model selection
model_choice = st.sidebar.radio(
"Select a model:",
        (
            "AI Generated Video Detector",
            # "Real vs AI Generated Image Detection -
            "AI Generated Image Detection",
            "About Us",
            "Contact-Us"
        ),
    )


if model_choice == "AI Generated Video Detector":
       
       
        st.title("Real vs AI Generated Video Detection")
        st.write("This is a demo of a real vs AI generated video detection app ")
        st.write("Upload an video to see if it's a real human  or an AI generated image.")
        st.write("")

        uploaded_file = st.file_uploader("Choose a video ...", type=["mp4", "webM"])
                    


# Update the elif clause for Real vs AI Generated Image Detection
elif model_choice.startswith("AI Generated Image Detection"):
            
           
        

        def get_prediction(inputImage):

            print("Processing image ", inputImage.name)
    
            img = cv2.imread(inputImage.name)
   
            resize = tf.image.resize(img, ([32, 32]))
            print("Resized image size: ", resize.shape)
    
            y_pred = loaded_model.predict(np.expand_dims(resize/255, 0))
            if y_pred > 0.001: 
                return 'Predicted class: REAL'
            else:
                return 'Predicted class: AI'
    
        def main():
            st.title("Real vs AI Generated Image Detection")
            st.write("This is a demo of a real vs AI generated image detection app ")
            st.write("Upload an image to see if it's a real human  or an AI generated image.")
            st.write("")
    
    
            img = st.file_uploader("Choose an image...", type=["png", "jpg", "*"])
            if img is None:
                print("Can not load image. Error")
                return
        
            diagnosis = ''

            if st.button('Check'):
                diagnosis = get_prediction(img)

            st.success(diagnosis)
    
        if __name__ == '__main__':
            main()
       


                
elif model_choice.startswith("Contact-Us"):   

    st.header(":mailbox: Get In Touch With our team!")


    contact_form = """
    <form action="https://formsubmit.co/sulavnepal10@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")

            
elif model_choice.startswith("About Us"):   

    left_column, right_column = st.columns(2)
    with right_column:
        st.header("SULAB NEPAL")
        st.header("PUR076BEI042")
       
    with left_column:
       st.image('sulab.jpg',width=500)

    st.write("---")

    left_column, right_column = st.columns(2)
    with right_column:
        st.header("SHISHIR PARAJULI")
        st.header("PUR076BEI035")
        
    with left_column:
       st.image('sisir.jpg',width=500)

    st.write("---")

    left_column, right_column = st.columns(2)
    with right_column:
        st.header("SAPHAL BHATTARAI")
        st.header("PUR076BEI032")
       
    with left_column:
       st.image('saphal.jpg',width=500)

    st.write("---")

    left_column, right_column = st.columns(2)
    with right_column:
        st.header("PUSHPA KAMAL DAHAL")
        st.header("PUR076BEI026")
       
    with left_column:
       st.image('pushpa.png',width=500)

  
           
              
            
           
           

          