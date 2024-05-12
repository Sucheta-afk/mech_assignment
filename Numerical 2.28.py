import streamlit as st
import os

st.markdown("""
    <style>
    .wide-container {
        max-width: 100%;
        padding-left: 20px;
        padding-right: 20px;
        text-align: left;
        position: relative;
    }
    .left-title {
        text-align: left;
        color: #D90166;
    }
    .vertical-line-yellow {
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        width: 5px;
        background-color: yellow;
    }
    .vertical-line-darkpink {
        position: absolute;
        top: 0;
        bottom: 0;
        right: 0;
        width: 5px;
        background-color: darkpink;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='wide-container'>"
    "<div class='vertical-line-yellow'></div>"
    "<h1 class='left-title'>PROBLEM 2/28</h1>"
    "<div class='vertical-line-darkpink'></div>"
    "</div>",
    unsafe_allow_html=True
)


# Display the paragraph permanently
st.markdown("<div class='wide-container'><p class='wide-paragraph'>2/28) Power is to be transferred from the pinion A to the output gear C inside a mechanical drive. Because of output motion requirements and space limitations, an idler & rear B is introduced as shown. A force analysis has determined that the total contact force between each pair of meshing teeth has a magnitude Fn = 5500 N, and these forces are shown acting on idler gear B. Determine the magnitude of the resultant R of the two contact forces acting on the idler gear. Complete both a graphical and a vector solution.</p></div>", unsafe_allow_html=True)
        
# Load image from a file path
image_path = r"C:/Users/Sucheta/OneDrive/Desktop/Mech/images/image.png"  
# Display the image
st.image(image_path, width=300, use_column_width=False)
        
st.write("Here is the answer...")
# Load image from a file path
answer_image_path = r"C:\Users\Sucheta\OneDrive\Desktop\Mech\images\answer.png"  
# Display the image
st.image(answer_image_path, width=500, use_column_width=False)

if st.button("Home Page"):
        # Define the path to the file you want to navigate to
        target_file_path = r"C:\Users\Sucheta\OneDrive\Desktop\Mech\main.py"  # Change this to the actual path of your file
        
        # Check if the target file exists
        if os.path.exists(target_file_path):
            # If the file exists, redirect the user to the target file
            os.system(f"streamlit run {target_file_path}")
        else:
            # If the file does not exist, display an error message
            st.error("The target file does not exist.")
