############################################################## First version of Code ##################################
# import streamlit as st
# import requests
# import base64
# from PIL import Image
# from dotenv import load_dotenv
# import io
# load_dotenv()
# import os
# import json
# from groq import Groq
# import base64

# groq_api_key = os.environ.get("GROQ_API_KEY")
# GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Groq's Llama API endpoint

# # Custom background and styling
# st.markdown(
#     """
#     <style>

#         .stApp {
#             background-image: url('https://tklhbdklspihuwzuaxrb.supabase.co/storage/v1/object/public/Test_data//blur_valley.png');
#             background-size: cover;
#             background-position: center;
#             color: black;
#               }


#         /* Center header */
#         .title {
#             text-align: center;
#             font-size: 3rem;
#             font-weight: bold;
#             text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
#         }
        
#         /* Style upload box */
#         .stFileUploader {
#             background: rgba(255, 255, 255, 0.2);
#             border-radius: 10px;
#             padding: 10px;
#         }

#         /* Button styling */
#         .stButton button {
#             background-color: #B4DCE3;
#             color: black;
#             border-radius: 10px;
#             border: 2px solid ##ABCFED;
#             font-size: 16px;
#             padding: 10px;
#             transition: 0.3s;
#         }
        
#         .stButton button:hover {
#             background-color: #B4DCE3;
#             transform: scale(1.05);
#             border: 2px solid #ABCFED;
#             color: black;
#         }

#     </style>
#     """,
#     unsafe_allow_html=True,
# )



# def cap_gen(image_path, num_captions, tone, creativity, caption_length, language):

#     # Function to encode the image
#     def encode_image(image_path):
#         with open(image_path, "rb") as image_file:
#             return base64.b64encode(image_file.read()).decode('utf-8')



#     prompt =  f"""Generate {num_captions} Instagram captions for this image in {language} language.
#                                     The tone should be {tone}. 
#                                     The creativity level should be {creativity}.
#                                     Each of the generated captions should have a length of {caption_length} words.
#                                     Make sure that you also provide the relevant and trending hastags followed by each caption.
#                                     Generate the captions only in JSON format and stick to the format defined below:
                                    
#                                     "Caption 1" -  
#                                         "text": "some text",
#                                         "hashtag": "#few-hastags"


#                                     "Caption 2" -  
#                                         "text": "another text",
#                                         "hashtag": "#another-hastags"

#                                     """

#     # Getting the base64 string
#     base64_image = encode_image(image_path)

#     client = Groq()

#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": prompt},
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{base64_image}",
#                         },
#                     },
#                 ],
#             }
#         ],
#         #model="llama-3.2-90b-vision-preview",
#         model = "meta-llama/llama-4-scout-17b-16e-instruct",
#         response_format={"type": "json_object"},
#         stop=None,
#         top_p=1,
#         temperature=0.8,
#         max_completion_tokens=1000,
#         seed=42,
#         n = 1
#     )

#     response = chat_completion.choices[0].message.content
#     return response


# def caption_box(caption, hashtags):
#     box_html = f"""
#     <div style="
#         border: 2px solid #E0B586;
#         border-radius: 10px;
#         padding: 15px;
#         margin: 10px 0;
#         background-color: #B4DCE3;
#         box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
#     ">
#         <p style="font-size: 16px; color: #1A414B; font-family: Arial, sans-serif;">
#             {caption}
#         </p>
#         <p style="color: #1A414B; font-weight: bold;">
#             {hashtags}
#         </p>
#     </div>
#     """
#     st.markdown(box_html, unsafe_allow_html=True)



# def main():
#     #st.title("Instagram Caption Generator (Groq Llama)")
#     st.title(" 🖼️➡️📝 Picture Perfect Captions!")

#     uploaded_file = st.file_uploader("Upload an image (Max 4 MB allowed)", type=["jpg", "jpeg", "png", "jfif","heic"])

#     if uploaded_file is not None:
#         temp_path = os.path.join("/tmp", uploaded_file.name)
#         with open(temp_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         img = Image.open(temp_path)
#         st.image(img, caption=f"Image uploaded: {uploaded_file.name}", use_container_width= True)
#         uploaded_file.seek(0, os.SEEK_END)
#         file_size_kb = uploaded_file.tell() / 1024
#         st.write(f"File size: {file_size_kb:.2f} KB")
#         uploaded_file.seek(0) 


#         num_captions = st.slider("Number of Captions", 1, 5, 1)
#         tone = st.selectbox("Tone", ["Casual", "Professional", "Funny", "Inspirational", "Sarcastic", "Romantic", "Nostalgic", "Calmness", "Exciting", "Happiness", "Poetic"])
#         creativity = st.selectbox("Creativity", ["Low", "Medium", "High"])
#         caption_length = st.selectbox("Caption Length (words)", ["20 - 80","80 - 140", "140 - 200", "200 - 250"])
#         language = st.selectbox("Language", ["English", "Spanish", "French", "German", "Italian", "Hindi"])

#         # if st.button("Generate Captions"):
#         #     captions = cap_gen(temp_path, num_captions, tone, creativity, caption_length, language)
#         #     intm_resp = json.loads(captions)
#         #     for k,v in intm_resp.items():
#         #         st.write(f"{k.strip()} - ")
#         #         for k1, v1 in v.items():
#         #             st.write(f"{v1.strip()}")

#         if st.button("Generate Captions 🎲"):
#             captions = cap_gen(temp_path, num_captions, tone, creativity, caption_length, language)
#             intm_resp = json.loads(captions)
#             st.subheader("✨ Suggested Captions")
#             count = 1
#             for k,v in intm_resp.items():
#     #print(k,v)
#                 caption = f"Caption {count}: \n{v['text']}"
#                 hastag = v['hashtag']
                
#                 #st.write(f"Caption: {caption}")
#                 #st.write(f"Hashtag: {hastag}")
#                 caption_box(caption, hastag)
#                 st.write("\n")
#                 count += 1


                
                
#             # st.write(f"\n{len(captions)}\n")

#             # st.write(captions)

#             # st.subheader("Generated Captions:")
#             # for i, caption in enumerate(captions):
#             #     st.write(f"**Caption {i + 1}:** {caption}")

# if __name__ == "__main__":
#     main()

#################################################### Second version of code ##########################################################

import streamlit as st
import base64
from PIL import Image
import io
from dotenv import load_dotenv
import os
import json
from groq import Groq
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import warnings
from PIL import Image, ExifTags
warnings.filterwarnings("ignore")
load_dotenv()

# st.cache_data.clear()
# st.cache_resource.clear()

client = Groq()
groq_api_key = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Groq's Llama API endpoint


def correct_orientation(image):
    try:
        # Extract EXIF data
        exif = image._getexif()
        if exif:
            for tag, value in exif.items():
                tag_name = ExifTags.TAGS.get(tag, tag)
                if tag_name == "Orientation":
                    if value == 3:
                        image = image.rotate(180, expand=True)  # Upside-down
                    elif value == 6:
                        image = image.rotate(270, expand=True)  # Rotated right
                    elif value == 8:
                        image = image.rotate(90, expand=True)  # Rotated left
        return image
    except Exception as e:
        st.warning("Could not process EXIF data. Uploading as is.")
        return image



st.set_page_config(page_title="SnapScribe", page_icon="📸", layout="wide")

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'


######################################## Function to generate captions from images ##########################################################
def show_home():

    # st.markdown(
    # """
    # <style>

    #     .stApp {
    #         background-image: url('https://wallpapers.com/images/hd/pastel-cute-background-qe3eh8zpms97062y.jpg');
    #         background-size: cover;
    #         background-position: center;
    #         color: black;
    #           }


    #     /* Center header */
    #     .title {
    #         text-align: center;
    #         font-size: 3rem;
    #         font-weight: bold;
    #         text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    #     }
        
    #     /* Style upload box */
    #     .stFileUploader {
    #         background: rgba(255, 255, 255, 0.2);
    #         border-radius: 10px;
    #         padding: 10px;
    #         font-size: 14px;
    #     }

    #     /* Button styling */
    #     .stButton button {
    #         background-color: #B4DCE3;
    #         color: black;
    #         border-radius: 10px;
    #         border: 2px solid ##ABCFED;
    #         font-size: 16px;
    #         padding: 10px;
    #         transition: 0.3s;
    #     }
        
    #     .stButton button:hover {
    #         background-color: #B4DCE3;
    #         transform: scale(1.05);
    #         border: 2px solid #ABCFED;
    #         color: black;
    #     }


    # </style>
    # """,
    # unsafe_allow_html=True,
    #     )



    st.markdown(
        """
        <style>


            /* Import Google Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Pacifico&display=swap');





            /* Background image for the main app */
            .stApp {
                background-image: url('https://wallpapers.com/images/hd/pastel-cute-background-qe3eh8zpms97062y.jpg');
                background-size: cover;
                background-position: center;
                color: black;
            }

            /* Sidebar styling */
            section[data-testid="stSidebar"] {
                /* background: linear-gradient(135deg, #ff9a9e, #fad0c4); Soft pink gradient */
                background-image: url('https://i.pinimg.com/474x/e4/7c/05/e47c05b471bd734250a23f7b186ada9a.jpg');
                border-radius: 10px;
                padding: 10px;
                /* box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);  Subtle shadow */
            }

            section[data-testid="stSidebar"] * {
                /* font-family: 'Montserrat', sans-serif !important; */
                font-family: 'Montserrat', cursive !important;
                font-size: 20px;
                color: #333333 !important; /* Dark grey text */
            }

            div[role="radiogroup"] label {
            margin-bottom: 20px !important; /* Adjust spacing */
                }

                
            @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-10px); }
            100% { opacity: 1; transform: translateY(0); }
            }

            h1 {
            animation: fadeIn 1.5s ease-in-out;
            text-align: left-top;
            font-size: 42px;
            color: #FF5733;
            font-family: 'Montserrat', sans-serif !important;
            text-shadow: 3px 3px 5px rgba(0,0,0,0.3);
            }




            /* Center header */
            .title {
                text-align: center;
                font-size: 3rem;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }

            /* Style upload box */
            div[data-testid="stFileUploader"] {
                background: rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                border: 2px dashed #ccc;
                text-align: left top;
            }



            /* Button styling */
            .stButton button {
                background-color: #B1D8B7; /* Light Pink */
                color: black;
                border-radius: 10px;
                border: 2px solid #ECF87F;
                font-size: 16px;
                padding: 10px;
                transition: 0.3s;
            }
            
            /* Button hover effect */
            .stButton button:hover {
                background-color: #778A35; /* Darker Pink */
                transform: scale(1.05);
                border: 2px solid #ABCFED;
                color: white;
            }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar Content
    # with st.sidebar:
    #     st.header("🌸 Styled Sidebar")
    #     st.write("This sidebar has a gradient background and smooth styling!")
    #     st.button("Click Me")




    st.title("SnapScribe 📸✍️🔠")
    st.write("**Picture Perfect Captions!**")

    def cap_gen(image_path, num_captions, tone, creativity, caption_length, language, add_keywords):

        #Setting the temperature based on the creativity level
        if creativity == "High":
            vision_temp = 0.8
        if creativity == "Medium":
            vision_temp = 0.7
        if creativity == "Low":
            vision_temp = 0.6


        #Setting the number of tokens based on the caption length
        if caption_length == "10 - 20":
            vision_token = 300
        if caption_length == "20 - 80":
            vision_token = 700
        if caption_length == "80 - 140":
            vision_token = 1000
        if caption_length == "140 - 200":
            vision_token = 1200

        
        # Function to encode the image
        def encode_image(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
            

        def process_keywords(add_keywords):
            keywords = add_keywords.split(",")
            all__words = ", ".join([keyword.strip() for keyword in keywords])
            return all__words
        
        all_words = process_keywords(add_keywords)

        prompt =  f"""Generate {num_captions} instagram post captions for this image in {language} language.
                                        The tone should be {tone}. 
                                        The creativity level should be {creativity}.
                                        Each of the generated captions should have a length of {caption_length} words.
                                        Please use atleast one of words from the following keywords, or their synonyms, or any other form of these words: {all_words}, while generating captions. If the keyword list is empty, generate captions without any keyword restrictions. 
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
            #model="llama-3.2-90b-vision-preview",
            model = "meta-llama/llama-4-scout-17b-16e-instruct",
            response_format={"type": "json_object"},
            stop=None,
            top_p=1,
            temperature=vision_temp,
            max_completion_tokens=vision_token,
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

    uploaded_file = st.file_uploader("Upload an image (Max 4 MB allowed)", type=["jpg", "jpeg", "png", "jfif","heic"])

    if uploaded_file is not None:
        try:
            temp_path = os.path.join("/tmp", uploaded_file.name)
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            img = Image.open(temp_path)
            img = correct_orientation(img)
            st.image(img, caption=f"Image uploaded: {uploaded_file.name}", use_container_width= True)
            uploaded_file.seek(0, os.SEEK_END)
            file_size_kb = uploaded_file.tell() / 1024
            st.write(f"File size: {file_size_kb:.2f} KB")
            uploaded_file.seek(0) 


            num_captions = st.slider("Number of Captions", 1, 5, 1)
            tone = st.selectbox("Tone", ["Casual", "Funny", "Inspirational", "Sarcastic", "Romantic", "Nostalgic", "Calm", "Exciting", "Happy", "Poetic"])
            creativity = st.selectbox("Creativity", ["Low", "Medium", "High"])
            caption_length = st.selectbox("Caption Length (words)", ["10 - 20","20 - 80","80 - 140", "140 - 200"])
            language = st.selectbox("Language", ["English", "Spanish", "French", "German", "Italian"])
            add_kw = st.text_area(label="Enter keywords for caption generation (optional).", height=68, placeholder="e.g., sunset, beach, ocean, couple")


            if st.button("Generate Captions 🎲"):
                captions = cap_gen(temp_path, num_captions, tone, creativity, caption_length, language, add_kw)
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

        except Exception as e:
            st.error(f"Error generating caption: {e}")





############################################# Function to show word generator section ###################################################


def show_wordgen():

    st.markdown(
        """
        <style>


            /* Import Google Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Pacifico&display=swap');


            div[role="radiogroup"] label span {
            color: red !important;  /* Change text color */
            }


            div[role="radiogroup"] div[role="radio"]::before {
            background-color: red !important;  /* Change dot color */
            }


            /* Background image for the main app */
            .stApp {
                background-image: url('https://wallpapers.com/images/hd/pastel-cute-background-qe3eh8zpms97062y.jpg');
                background-size: cover;
                background-position: center;
                color: black;
            }

            /* Sidebar styling */
            section[data-testid="stSidebar"] {
                /* background: linear-gradient(135deg, #ff9a9e, #fad0c4); Soft pink gradient */
                background-image: url('https://i.pinimg.com/474x/e4/7c/05/e47c05b471bd734250a23f7b186ada9a.jpg');
                border-radius: 10px;
                padding: 10px;
                /* box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);  Subtle shadow */
            }

            section[data-testid="stSidebar"] * {
                /* font-family: 'Montserrat', sans-serif !important; */
                font-family: 'Montserrat', cursive !important;
                font-size: 20px;
                color: #333333 !important; /* Dark grey text */
            }

            div[role="radiogroup"] label {
            margin-bottom: 20px !important; /* Adjust spacing */
                }

                
            @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-10px); }
            100% { opacity: 1; transform: translateY(0); }
            }

            h1 {
            animation: fadeIn 1.5s ease-in-out;
            text-align: left-top;
            font-size: 42px;
            color: #FF5733;
            font-family: 'Montserrat', sans-serif !important;
            text-shadow: 3px 3px 5px rgba(0,0,0,0.3);
            }




            /* Center header */
            .title {
                text-align: center;
                font-size: 3rem;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }

            /* Style upload box */
            div[data-testid="stFileUploader"] {
                background: rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                border: 2px dashed #ccc;
                text-align: left top;
            }



            /* Button styling */
            .stButton button {
                background-color: #B1D8B7; /* Light Pink */
                color: black;
                border-radius: 10px;
                border: 2px solid #ECF87F;
                font-size: 16px;
                padding: 10px;
                transition: 0.3s;
            }
            
            /* Button hover effect */
            .stButton button:hover {
                background-color: #778A35; /* Darker Pink */
                transform: scale(1.05);
                border: 2px solid #ABCFED;
                color: white;
            }

        </style>
        """,
        unsafe_allow_html=True,
    )   





    # st.title("Captionary")
    # st.write(" 🖼️➡️📝 Picture Perfect Captions!")

    st.title("VibeText 📜✨")
    st.write("_Bring your words to life by transforming them into captivating captions.._")


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


    def cap_gen_text(keywords, num_captions, tone, creativity, caption_length, language):

    #Setting the temperature based on the creativity level
        if creativity == "High":
            temp = 0.8
        if creativity == "Medium":
            temp = 0.7
        if creativity == "Low":
            temp = 0.6


            #Setting the number of tokens based on the caption length
        if caption_length == "10 - 20":
            token_len = 300
        if caption_length == "20 - 80":
            token_len = 700
        if caption_length == "80 - 140":
            token_len = 1000
        if caption_length == "140 - 200":
            token_len = 1200


        caption_prompt = PromptTemplate(
            input_variables=["num_captions", "language", "tone", "creativity", "caption_length", "keywords"],
            template=(
                """Generate {num_captions} Instagram post captions in {language} language.
                The tone should be {tone}.
                The creativity level should be {creativity}.
                Each of the generated captions should have a length of {caption_length} words.
                You need to use at least one of the following keywords, or their synonyms, or any other form of these words: {keywords}, while generating captions.
                If the keyword list is empty, generate captions without any keyword restrictions.
                Make sure that you also provide the relevant and trending hashtags followed by each caption.
                Do not generate anything else apart from captions in JSON format.
                Generate the captions only in JSON format and stick to the format defined below:
                
                {{
                    "Caption 1": {{
                        "text": "some text",
                        "hashtag": "#few-hashtags"
                    }},
                    "Caption 2": {{
                        "text": "another text",
                        "hashtag": "#another-hashtags"
                    }}
                }}
                """
            ),
        )

        # Create LLM Chain

        llm_text = ChatGroq(model="llama-3.1-8b-instant", temperature=temp, max_tokens=token_len, timeout=None, max_retries=3)

        caption_chain = LLMChain(llm=llm_text, prompt=caption_prompt)

        response = caption_chain.run({
            "keywords": keywords if keywords else "",
            "num_captions": num_captions,
            "language": language,
            "tone": tone,
            "creativity": creativity,
            "caption_length": caption_length
        })

        return response



    keywords = st.text_area("Enter your keywords/phrases:", height=100)
    num_captions = st.slider("Number of Captions", 1, 5, 1)
    tone = st.selectbox("Tone", ["Casual", "Funny", "Inspirational", "Sarcastic", "Romantic", "Nostalgic", "Calm", "Exciting", "Happy", "Poetic"])
    creativity = st.selectbox("Creativity", ["Low", "Medium", "High"])
    caption_length = st.selectbox("Caption Length (words)", ["10 - 20","20 - 80","80 - 140", "140 - 200"])
    language = st.selectbox("Language", ["English", "Spanish", "French", "German", "Italian"])

    if st.button("🎲 Generate Captions"):
        if not keywords.strip():  # Check if input is empty or just spaces
            st.warning("⚠️ Please enter at least one keyword or phrase for generating captions.")
        else:
            with st.spinner("Generating captions... 🚀"):
                text_captions = cap_gen_text(keywords, num_captions, tone, creativity, caption_length, language)
                intm_text_resp = json.loads(text_captions)
                st.subheader("✨ Suggested Captions")
                count = 1
                for k,v in intm_text_resp.items():
                    caption = f"Caption {count}: \n{v['text']}"
                    hastag = v['hashtag']
                    caption_box(caption, hastag)
                    st.write("\n")
                    count += 1




    # if st.button("Generate Caption"):
    #     if user_words:
    #         try:
    #             prompt = f"Generate a caption using these keywords/phrases: {user_words}"
    #             # --- LLAMA Text Generation ---
    #             output = llm_text(prompt, max_tokens=150) # Example inference
    #             caption = output["choices"][0]["text"].strip()
    #             st.write("Generated Caption:", caption)
    #         except Exception as e:
    #             st.error(f"Error generating caption: {e}")
    #     else:
    #         st.warning("Please enter some keywords/phrases.")

# def show_contact():
#     st.title("Contact Page")
#     st.write("Contact us here!")
    # ... contact page content ...

# ... (rest of the navigation code remains the same)

# page = st.sidebar.selectbox("Choose a page", ["SnapScribe - Generate captions by pictures", "Vibetext - Generate captions using words", "Contact"])

# if page == "SnapScribe - Generate captions by pictures":
#     show_home(client)
# elif page == "Vibetext - Generate captions using words":
#     show_wordgen()
# elif page == "Contact":
#     show_contact()


pages = {
    1: "SnapScribe - Generate captions by pictures",
    2: "Vibetext - Generate captions using words"
    # 3: "Contact"
}

#page_options = [page for page in pages.values()]

# Use selectbox with dictionary values
#selected_key = st.sidebar.selectbox("Choose a page", options=list(pages.keys()), format_func=lambda x: pages[x])

# selected_key = st.sidebar.selectbox("Choose a page", page_options)

selected_key = st.sidebar.radio("Go to -", options=list(pages.keys()), format_func=lambda x: pages[x])

# Match selected key instead of long strings
if selected_key == 1:
    show_home()
elif selected_key == 2:
    show_wordgen()
# elif selected_key == 3:
#     show_contact()





























































































































































































































































































































































































