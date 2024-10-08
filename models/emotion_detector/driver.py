import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model

import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration, VideoProcessorBase, WebRtcMode, VideoTransformerBase
import av

try:
    model = load_model('models/emotion_detector/saved_models/best_model.keras')
    # st.success("Model loaded successfully.")
except Exception:
    st.error("Model not loaded properly.")

RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

#face loading - object detection
try:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml' )
    # st.success("Face cascade loaded successfully.")
except Exception:
    st.write("Error loading cascade classifiers")



emotion_dict = {0:'angry', 1 :'happy', 2: 'neutral', 3:'sad', 4: 'surprise'}
class FaceEmotion(VideoProcessorBase):
    
    def recv(frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")

        #image gray
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            image=img_gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img=img, pt1=(x, y), pt2=(
                x + w, y + h), color=(255, 0, 0), thickness=2)
            roi_gray = img_gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)


            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                prediction = model.predict(roi)[0]
                
                st.write(f"Prediction: {prediction}")

                maxindex = int(np.argmax(prediction))
                finalout = emotion_dict[maxindex]
                output = str(finalout)
            label_position = (x, y)
            cv2.putText(img, output, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

def get_prediction():

    #streamlit application
    st.subheader("Webcam Live Feed")
    
    #warning before using the app
    st.warning("⚠️ Warning: This feature uses live camera footage for face emotion detection. Make sure you are comfortable with this.")
        
    st.write("Click on start to use the webcam and detect your face emotion.")
    # Start webcam streamer
    webrtc_streamer(key="object-detection", 
                    mode=WebRtcMode.SENDRECV, 
                    rtc_configuration= RTC_CONFIGURATION, 
                    video_processor_factory=FaceEmotion, 
                    media_stream_constraints={"video": True, "audio": False},
                    async_processing=True, )

if __name__ == "__main__":
    get_prediction()


