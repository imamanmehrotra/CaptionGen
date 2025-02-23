import streamlit as st
import requests
import base64
from PIL import Image
from dotenv import load_dotenv
import io
load_dotenv()
import os
import json
from groq import Groq
import base64

groq_api_key = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Groq's Llama API endpoint

# Custom background and styling
st.markdown(
    """
    <style>

        .stApp {
            background-image: url('https://tklhbdklspihuwzuaxrb.supabase.co/storage/v1/object/public/Test_data//blur_valley.png');
            background-size: cover;
            background-position: center;
            color: black;
              }


        /* Center header */
        .title {
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        /* Style upload box */
        .stFileUploader {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 10px;
        }

        /* Button styling */
        .stButton button {
            background-color: #B4DCE3;
            color: black;
            border-radius: 10px;
            border: 2px solid ##ABCFED;
            font-size: 16px;
            padding: 10px;
            transition: 0.3s;
        }
        
        .stButton button:hover {
            background-color: #B4DCE3;
            transform: scale(1.05);
            border: 2px solid #ABCFED;
            color: black;
        }

    </style>
    """,
    unsafe_allow_html=True,
)



def cap_gen(image_path, num_captions, tone, creativity, caption_length, language):

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')



    prompt =  f"""Generate {num_captions} Instagram captions for this image in {language} language.
                                    The tone should be {tone}. 
                                    The creativity level should be {creativity}.
                                    Each of the generated captions should have a length of {caption_length} words.
                                    Make sure that you also provide the relevant and trending hastags followed by each caption.
                                    Generate the captions only in JSON format and stick to the format defined below:
                                    
                                    "Caption 1" -  
                                        "text": "some text",
                                        "hashtag": "#few-hastags"


                                    "Caption 2" -  
                                        "text": "another text",
                                        "hashtag": "#another-hastags"

                                    """

    # Getting the base64 string
    base64_image = encode_image(image_path)

    client = Groq()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model="llama-3.2-90b-vision-preview",
        response_format={"type": "json_object"},
        stop=None,
        top_p=1,
        temperature=0.8,
        max_completion_tokens=1000,
        seed=42,
        n = 1
    )

    response = chat_completion.choices[0].message.content
    return response


def caption_box(caption, hashtags):
    box_html = f"""
    <div style="
        border: 2px solid #E0B586;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        background-color: #B4DCE3;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    ">
        <p style="font-size: 16px; color: #1A414B; font-family: Arial, sans-serif;">
            {caption}
        </p>
        <p style="color: #1A414B; font-weight: bold;">
            {hashtags}
        </p>
    </div>
    """
    st.markdown(box_html, unsafe_allow_html=True)



def main():
    #st.title("Instagram Caption Generator (Groq Llama)")
    st.title(" 🖼️➡️📝 Picture Perfect Captions!")

    uploaded_file = st.file_uploader("Upload an image (Max 4 MB allowed)", type=["jpg", "jpeg", "png", "jfif","heic"])

    if uploaded_file is not None:
        temp_path = os.path.join("/tmp", uploaded_file.name)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        img = Image.open(temp_path)
        st.image(img, caption=f"Image uploaded: {uploaded_file.name}", use_container_width= True)
        uploaded_file.seek(0, os.SEEK_END)
        file_size_kb = uploaded_file.tell() / 1024
        st.write(f"File size: {file_size_kb:.2f} KB")
        uploaded_file.seek(0) 


        num_captions = st.slider("Number of Captions", 1, 5, 1)
        tone = st.selectbox("Tone", ["Casual", "Professional", "Funny", "Inspirational", "Sarcastic", "Romantic", "Nostalgic", "Calmness", "Exciting", "Happiness", "Poetic"])
        creativity = st.selectbox("Creativity", ["Low", "Medium", "High"])
        caption_length = st.selectbox("Caption Length (words)", ["20 - 80","80 - 140", "140 - 200", "200 - 250"])
        language = st.selectbox("Language", ["English", "Spanish", "French", "German", "Italian", "Hindi"])

        # if st.button("Generate Captions"):
        #     captions = cap_gen(temp_path, num_captions, tone, creativity, caption_length, language)
        #     intm_resp = json.loads(captions)
        #     for k,v in intm_resp.items():
        #         st.write(f"{k.strip()} - ")
        #         for k1, v1 in v.items():
        #             st.write(f"{v1.strip()}")

        if st.button("Generate Captions 🎲"):
            captions = cap_gen(temp_path, num_captions, tone, creativity, caption_length, language)
            intm_resp = json.loads(captions)
            st.subheader("✨ Suggested Captions")
            count = 1
            for k,v in intm_resp.items():
    #print(k,v)
                caption = f"Caption {count}: \n{v['text']}"
                hastag = v['hashtag']
                
                #st.write(f"Caption: {caption}")
                #st.write(f"Hashtag: {hastag}")
                caption_box(caption, hastag)
                st.write("\n")
                count += 1


                
                
            # st.write(f"\n{len(captions)}\n")

            # st.write(captions)

            # st.subheader("Generated Captions:")
            # for i, caption in enumerate(captions):
            #     st.write(f"**Caption {i + 1}:** {caption}")

if __name__ == "__main__":
    main()