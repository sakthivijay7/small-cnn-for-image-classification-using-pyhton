from tensorflow.keras.preprocessing.image import img_to_array,load_img
from keras.models import load_model
from PIL import Image
import numpy as np
import streamlit as st

# #[theme]
# base="light"
# primaryColor="#08b906"
# secondaryBackgroundColor="#43f5d5"
# textColor="#04078e"


st.title("Image classification using CNN")
st.subheader("Ironman vs Ultron")

model_load=load_model("trained_model.h5")

image=st.file_uploader("Upload an image",type=["jpg","jpeg","png","jfif"])


# img_path=r"D:\ALL\DL\predict\imag.jfif"
if image is not None:
  
  st.image(image,caption="Uploaded Image",use_container_width=True)
  
  img=load_img(image,target_size=(224,224))
  img_array=img_to_array(img)/255.0
  img_expand=np.expand_dims(img_array,axis=0)


if st.button("Predict"):
    predict=model_load.predict(img_expand)
    if predict[0][0]>0.5:
      st.success("This is  Ultron \U0001F608")
    else:
      st.success("This is  Ironman \U0001F60E")    
 

