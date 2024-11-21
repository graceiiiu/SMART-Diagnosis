import streamlit as st
import numpy as np
import os
import sys

st.write(f"Python version: {sys.version}")

try:
    import tensorflow as tf
    st.success(f"""
    TensorFlow successfully loaded!
    Version: {tf.__version__}
    GPU Available: {tf.test.is_built_with_cuda()}
    """)
except ImportError as e:
    st.error(f"""
    Failed to import TensorFlow. Error details:
    {str(e)}
    
    Attempting to install TensorFlow...
    """)
    
    import subprocess
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tensorflow==2.15.0"])
        import tensorflow as tf
        st.success("TensorFlow installed and imported successfully!")
    except Exception as install_error:
        st.error(f"""
        Failed to install TensorFlow. Error details:
        {str(install_error)}
        
        Please check your requirements.txt file contains:
        tensorflow==2.15.0
        numpy>=1.24.3
        protobuf>=3.20.0
        keras>=2.15.0
        h5py>=3.9.0
        """)
        st.stop()

st.title("COPD Detection System")
st.write("Upload a breathing sound recording to check for COPD indicators.")

# File uploader
audio_file = st.file_uploader("Upload Audio File", type=['wav'])

if audio_file is not None:
    st.audio(audio_file)
    
    if st.button("Analyze Audio"):
        st.info("Model loading... This might take a few minutes.")
        
        try:
            # Your model loading and prediction code here
            # For now, using placeholder prediction
            import random
            confidence = random.random() * 100
            diagnosis = "COPD" if confidence > 50 else "NOT COPD"
            
            st.subheader("Results:")
            st.write(f"Diagnosis: {diagnosis}")
            st.write(f"Confidence: {confidence:.2f}%")
            st.progress(confidence / 100)
        except Exception as e:
            st.error(f"An error occurred during analysis: {str(e)}")
