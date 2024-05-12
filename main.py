import streamlit as st
import math
import os

def main():
    st.markdown("""
    <style>
    body {
        background-size: cover;     
    }
    .wide-container {
        max-width: 100%;
        padding-left: 20px;
        padding-right: 20px;
        text-align: left;
        position: relative;
    }
    .wide-paragraph {
        width: 100%;
        text-align: left;
    }
    .centered-title {
        text-align: left;
        color: yellow;
    }
    .answer-button {
        background-color: green;
        color: white;
    }
    /* Vertical lines */
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
    .fx-color {
            color: yellow;
        }
    .fy-color {
            color: #e75480;
        }
    .name{
            text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    # Load image from a file path
    image_path_1 = r"C:/Users/Sucheta/OneDrive/Desktop/Mech/images/bg_img.png"  
    # Display the image
    st.image(image_path_1, width=500, use_column_width=True)
    

    # Display the Mech Calculator input fields outside the button condition
    st.markdown('<p class="fx-color"><b>Enter Σ Fx in newton(N) :</p>', unsafe_allow_html=True)
    value1 = st.number_input("", format="%f", key="fx_input", label_visibility="collapsed")
    st.markdown('<p class="fy-color"><b>Enter Σ Fy in newton(N) :</p>', unsafe_allow_html=True)
    value2 = st.number_input("", format="%f", key="fy_input", label_visibility="collapsed")
    
    if st.button("MECH CALCULATOR"):
        if value2 != 0:
        # Calculation
            result = round(math.sqrt((value1) ** 2 + (value2) ** 2), 3)
            angle_val = math.atan(value1 / value2)
            angle = round(math.degrees(angle_val), 2)
        # Displaying the result
            st.write("Resultant, R = ", result, "N")
            st.write("Angle with x-axis, θ = ", angle, "°")
    else:
        st.write("Angle with x-axis = 90°")
        st.write("Resultant currently = 0 N")

    st.write("Made by Sucheta", format="name")
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"



if __name__ == "__main__":
    main()



