import os
import json_utils
import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx


os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"

# Change default theme or settings dynamically
st.set_page_config(
    page_title="TOPIN TAGS | PST-Tech",
    page_icon="icon.png",
    layout="wide",
)

data = None

if not data:
    data = json_utils.get_json_data()

st.markdown(
    """
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1>Find Topin Tags</h1>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,1,1])

section = col1.selectbox('Choose Section', json_utils.get_sections(data))

topic = col2.selectbox('Choose Topic', json_utils.get_topics(data, section))

sub_topic = col3.selectbox('Choose Sub-Topic', json_utils.get_sub_topics(data, section, topic))

col1.code(section)
col2.code(topic)
col3.code(sub_topic)