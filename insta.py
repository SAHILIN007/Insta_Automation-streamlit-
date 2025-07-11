import streamlit as st
from instagrapi import Client
import os

st.set_page_config(page_title="📸 Instagram Post Uploader")

st.title("📸 Post on Instagram via Streamlit")

username = st.text_input("Instagram Username")
password = st.text_input("Instagram Password", type="password")
caption = st.text_area("Post Caption")
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if st.button("Post to Instagram"):
    if not username or not password or not uploaded_file:
        st.warning("Please fill in all fields.")
    else:
        with st.spinner("Logging in and posting..."):
            try:
                # Save uploaded file temporarily
                temp_image_path = os.path.join("temp.jpg")
                with open(temp_image_path, "wb") as f:
                    f.write(uploaded_file.read())

                cl = Client()
                cl.login(username, password)
                cl.photo_upload(temp_image_path, caption)

                os.remove(temp_image_path)
                st.success("✅ Post uploaded successfully!")
            except Exception as e:
                st.error(f"❌ Failed: {e}")
