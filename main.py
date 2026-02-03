import streamlit as st
import cv2
import numpy as np
from PIL import Image
import utils
import time

# 1. Page Configuration (Must be first)
st.set_page_config(
    page_title="Fin-Vision",
    page_icon="", # here we using shortcut key ( windows + . ) to add emoji good looking ui
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for "Pro" Look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.title(" Fin-Vision: The AI Fraud Sentinel")
st.markdown("### Real-time Financial Document Forensics")
st.markdown("---")

# 4. Sidebar Control
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=100)
    st.header("Control Panel")
    mode = st.radio("Select Input Mode:", ["Upload Image", "Live Camera"])
    
    st.markdown("---")
    st.caption("System Status:  Online")
    st.caption("Version: v1.0.0 (Hackathon Build)")

# 5. Main Logic
c1, c2 = st.columns([1, 1])

img = None

with c1:
    st.subheader("1. Input Document")
    if mode == " Upload Image":
        f = st.file_uploader("Upload Check/ID", type=["jpg", "png", "jpeg"])
        if f is not None:
            img = Image.open(f)
            img = np.array(img)
    else:
        cam = st.camera_input("Capture Document")
        if cam is not None:
            img = Image.open(cam)
            img = np.array(img)
            
    if img is not None:
        st.image(img, caption="Source Image", use_container_width=True)

with c2:
    st.subheader("2. Forensic Analysis")
    
    if img is not None:
        # Simulate Scanning Effect
        with st.spinner('Running AI Diagnostics...'):
            time.sleep(1.5)  # Just for "cool factor"
            
        blur_score = utils.check_blur(img)
        edge_score = utils.check_tampering(img)
        status = utils.get_status(blur_score, edge_score)
        
        # Display Metrics in a Grid
        m1, m2 = st.columns(2)
        m1.metric("Blur Score", int(blur_score), delta_color="inverse")
        m2.metric("Edge Density", int(edge_score))
        
        st.markdown("---")
        
        # Final Verdict Display
        if "Authentic" in status:
            st.success(f" VERDICT: {status}")
            st.balloons()
        else:
            st.error(f" VERDICT: {status}")
            st.caption("Reason: Document lacks necessary security fibers or texture.")
            
    else:

        st.info("Waiting for input...")

