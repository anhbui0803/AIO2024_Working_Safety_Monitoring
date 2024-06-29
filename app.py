import streamlit as st
from detection import detection
from config.model_config import DetectorConfig


@st.cache_data(max_entries=1000)
def process_detection(image_path):
    result_img = detection(
        image_path,
        weight_path=DetectorConfig().weight_path
    )

    return result_img


def main():
    st.set_page_config(layout="wide")
    st.title("Helmet Safety Detection with :blue[YOLOv10] :rocket:")

    uploaded_img = st.file_uploader(
        "**Input your image**", type=["jpg", "jpeg", "png"])
    example_button = st.button("Run example")

    if example_button:
        result_img = process_detection(".\\static\\example_img.jpg")
    elif uploaded_img:
        result_img = process_detection(uploaded_img)
    else:
        result_img = None

    if result_img is not None:
        st.markdown("**Detection result**")
        st.image(result_img)


if __name__ == '__main__':
    main()
