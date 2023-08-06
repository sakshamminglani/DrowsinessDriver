import streamlit as st
import subprocess

def main():
    st.title("Drowsiness Detector with Streamlit")

    if st.button("Start Drowsiness Detector"):
        # Run the drowsiness_detector.py script as a separate process
        subprocess.run(["python", "detect_drowsiness.py"])

if __name__ == "__main__":
    main()