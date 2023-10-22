import streamlit as st
import numpy as np
import os
import pickle

model = pickle.load(open("model.pkl", "rb"))

def main():
    st.title("Cancer Triage")

    smokes = st.toggle("SMOKING", value=False, label_visibility="visible")
    yello_fingers = st.toggle("YELLOW_FINGERS", value=False, label_visibility="visible")
    anxiety = st.toggle("ANXIETY", value=False, label_visibility="visible")
    peer_pressure = st.toggle("PEER_PRESSURE", value=False, label_visibility="visible")
    chronic_disease = st.toggle("CHRONIC DISEASE", value=False, label_visibility="visible")
    fatigue = st.toggle("FATIGUE", value=False, label_visibility="visible")
    allergy = st.toggle("ALLERGY", value=False, label_visibility="visible")
    wheezing = st.toggle("WHEEZING", value=False, label_visibility="visible")
    alcohol = st.toggle("ALCOHOL CONSUMING", value=False, label_visibility="visible")
    coughing = st.toggle("COUGHING", value=False, label_visibility="visible")
    shortness_of_breath = st.toggle("SHORTNESS OF BREATH", value=False, label_visibility="visible")
    swallowing_difficulty = st.toggle("SWALLOWING DIFFICULTY", value=False, label_visibility="visible")
    chest_pain = st.toggle("CHEST PAIN", value=False, label_visibility="visible")
    pressed = st.button("Triage")

    if pressed:
        print("pressed")
        x = [
            2 if smokes else 1,
            2 if yello_fingers else 1,
            2 if anxiety else 1,
            2 if peer_pressure else 1,
            2 if chronic_disease else 1,
            2 if fatigue else 1,
            2 if allergy else 1,
            2 if wheezing else 1,
            2 if alcohol else 1,
            2 if coughing else 1,
            2 if shortness_of_breath else 1,
            2 if swallowing_difficulty else 1,
            2 if chest_pain else 1,
        ]
        print(x)
        y = model.predict(np.array(x).reshape(1, -1))
        st.markdown(f'<h1 style="text-align: center">{ "Imaging Needed!" if y == 1 else "No Imaging Needed."}</h1>',unsafe_allow_html=True)


if __name__ == "__main__":
    main()
