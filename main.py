import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

from util import classify, set_background


set_background('./bgs/background.png')

# set title
st.title('Pneumonia Classification App')

# set header
st.header('Please upload a chest X-ray image or select an example from the tabs.')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

tab1, tab2, tab3 = st.tabs(["Normal", "Suspicious/Initial", "Severe"])

with tab1:
   st.header("Normal")
   st.write("[Case courtesy of Callum Smith](https://radiopaedia.org/articles/pneumonia)")
   st.image("./images/normal.jpg", width=400)

with tab2:
   st.header("Suspicious/Initial")
   st.write("[Case courtesy of Callum Smith](https://radiopaedia.org/articles/pneumonia)")
   st.image("./images/suspicious.jpg", width=400)

with tab3:
   st.header("Severe")
   st.write("[Case courtesy of Callum Smith](https://radiopaedia.org/articles/pneumonia)")
   st.image("./images/severe.jpg", width=400)

# load classifier
model = load_model('./model/pneumonia_classifier.h5')

# load class names
with open('./model/labels.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    # write classification
    st.write("## {}".format(class_name))
    st.write("### score: {}%".format(int(conf_score * 1000) / 10))