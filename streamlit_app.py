import streamlit as st
import pandas as pd
import numpy as np
import os, urllib
import streamlit_features_test, uber_pickups

DATA_URL_ROOT	= "https://raw.githubusercontent.com/hanmbink/DataScience/main/"
FILE_NAME_INST	= "instructions.md"

def main():

    # Render the readme as markdown using st.markdown.

    readme_text = st.markdown(get_file_content_as_string(FILE_NAME_INST))

    # Add a select box for the options

    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox("Choose an app",
        ["Show instructions", "App 1", "App 2"])

    if app_mode == "Show instructions":
        st.sidebar.success('To continue select an app from drop down list')
    
    elif app_mode == "App 1":
        readme_text.empty()
        streamlit_features_test.run_it()
    
    elif app_mode == "App 2":
        readme_text.empty()
        uber_pickups.run_it()

# Download a single file and make its content available as a string.
@st.cache(show_spinner=False)
def get_file_content_as_string(path):
	url = DATA_URL_ROOT + path
	response = urllib.request.urlopen(url)
	return response.read().decode("utf-8")

if __name__ == "__main__":
    main()



