import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Background Remover", layout="centered")
st.title("🖼️ Background Remover App")
st.write("Upload an image, and this app will remove the background.")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Original Image", use_container_width=True) 
    if st.button("Remove Background"):
        with st.spinner("Removing background..."):
            result = remove(input_image)
            st.image(result, caption="Image without Background", use_container_width=True)  
            buffered = io.BytesIO()
            result.save(buffered, format="PNG")
            byte_im = buffered.getvalue()
            st.download_button(
                label="📥 Download PNG",
                data=byte_im,
                file_name="no_background.png",
                mime="image/png"
            )
