# import keras_ocr
# import matplotlib.pyplot as plt
# from TTS import capture_image

# from langchain import OpenAI, LLMChain, PromptTemplate
# from langchain.memory import ConversationBufferWindowMemory

# import easyocr


# from TTS import capture_image
# from TTS import speak
# import os
# from dotenv import find_dotenv, load_dotenv

# dotenv_path= find_dotenv()
# load_dotenv(dotenv_path)
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


# template = """
# Data Obtained from OCR by Camera for Blind Individuals

# This data is obtained through optical character recognition (OCR) using a camera operated by blind individuals. Due to variations in capturing conditions and text complexities, the data may contain inconsistencies or inaccuracies. However, it holds valuable information that can be explored and understood with the help of contextual analysis and interpretation.

# OCR technology enables blind individuals to access printed materials and documents by converting them into digital text. Although the captured text may lack formatting or perfect alignment, it opens avenues for blind users to engage with textual content through alternative means.

# Interpreting the Meaning:

# 1. Contextual Analysis: To understand the data, consider the context in which it was captured. Explore the environment, potential document types, or specific scenarios that may provide insights into the captured text's purpose.

# 2. Interpretive Approach: Instead of focusing solely on literal interpretations, adopt an interpretive approach. Identify key terms, patterns, and relationships to provide explanations or alternative descriptions that uncover the intended meaning behind the captured words.

# 3. Collaborative Efforts: Engage in collaborative discussions with blind individuals or experts familiar with OCR technology. By combining their expertise and insights, a more comprehensive understanding of the captured data can be achieved.

# Please contribute your insights, interpretations, or clarifications to help unravel the meaning behind the captured text.

# Let's embark on this meaningful journey together, embracing the challenges and opportunities presented by OCR-generated data from the perspective of blind individuals!

# history: {history}
# Text: {ocr_text}

# """

# prompt = PromptTemplate(input_variables=[ "history", "ocr_text"], template=template)
# # Initialize ChatGPT
# chatgpt_chain = LLMChain(
#     llm=OpenAI(temperature=0),
#     prompt=prompt,
#     verbose=True,
#     memory=ConversationBufferWindowMemory(k=2),
# )

# path = capture_image()
# img = path

# reader = easyocr.Reader(['en'])
# result = reader.readtext(img, detail = 0, paragraph = True)

# speak("Recognized Text:" + result)
# # Print recognized text
# speak("i guess that makes some sense.lets make more meaning out of that.")
# # Send recognized text to ChatGPT for feedback
# response_text = chatgpt_chain.predict(human_input=result)
# # Print ChatGPT's feedback
# speak("here you go .Results are :  ", response_text)


# import os
# import easyocr
# import sys
# import io
# import easyocr
# import matplotlib.pyplot as plt
# from dotenv import find_dotenv, load_dotenv
# from TTS import capture_image, speak
# from langchain import OpenAI, LLMChain, PromptTemplate
# from langchain.memory import ConversationBufferWindowMemory

# dotenv_path= find_dotenv()
# load_dotenv(dotenv_path)
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# template = """
# Data Obtained from OCR by Camera for Blind Individuals

# This data is obtained through optical character recognition (OCR) using a camera operated by blind individuals. Due to variations in capturing conditions and text complexities, the data may contain inconsistencies or inaccuracies. However, it holds valuable information that can be explored and understood with the help of contextual analysis and interpretation.

# OCR technology enables blind individuals to access printed materials and documents by converting them into digital text. Although the captured text may lack formatting or perfect alignment, it opens avenues for blind users to engage with textual content through alternative means.

# Interpreting the Meaning:

# 1. Contextual Analysis: To understand the data, consider the context in which it was captured. Explore the environment, potential document types, or specific scenarios that may provide insights into the captured text's purpose.

# 2. Interpretive Approach: Instead of focusing solely on literal interpretations, adopt an interpretive approach. Identify key terms, patterns, and relationships to provide explanations or alternative descriptions that uncover the intended meaning behind the captured words.

# 3. Collaborative Efforts: Engage in collaborative discussions with blind individuals or experts familiar with OCR technology. By combining their expertise and insights, a more comprehensive understanding of the captured data can be achieved.

# Please contribute your insights, interpretations, or clarifications to help unravel the meaning behind the captured text.

# Let's embark on this meaningful journey together, embracing the challenges and opportunities presented by OCR-generated data from the perspective of blind individuals!

# history: {history}
# Text: {ocr_text}
# """
# prompt = PromptTemplate(input_variables=[ "history", "ocr_text"], template=template)

# # Initialize ChatGPT
# chatgpt_chain = LLMChain(
#     llm=OpenAI(temperature=0),
#     prompt=prompt,
#     verbose=True,
#     memory=ConversationBufferWindowMemory(k=2),
# )

# def process_image_from_url():
#     path = capture_image() # Modify capture_image function to use url
#     img = path

#     # Temporarily redirect stdout to a dummy stream during Reader initialization
#     stdout = sys.stdout
#     sys.stdout = io.StringIO()
#     reader = easyocr.Reader(['en'])
#     sys.stdout = stdout

#     result = reader.readtext(img, detail = 0, paragraph = True)
#     speak("Recognized Text: {result}")
#     speak("I guess that makes some sense. Let's make more meaning out of that.")
#     response_text = chatgpt_chain.predict(ocr_text=result)
#     speak("Here you go. Results are: ", response_text)

# process_image_from_url()


import os
import sys
import io
import easyocr
from dotenv import find_dotenv, load_dotenv
from TTS import capture_image, speak
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
import speech_recognition as sr

dotenv_path= find_dotenv()
load_dotenv(dotenv_path)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def _approve(_input: str) -> bool:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 200
        r.pause_threshold = 0.5
        msg = (
            "Do you approve of the following input? "
            "Please say 'Yes' or 'No'."
        )
        msg += "\n\n" + _input + "\n"
        speak(msg)
        try:
            audio = r.listen(source, timeout=50, phrase_time_limit=50)
            resp = r.recognize_google(audio)
            return resp.lower() in ("yes", "y")
        except Exception as e:
            speak(f"An error occurred while recognizing your response: {e}")
            return False

template = """
Data Obtained from OCR by Camera for Blind Individuals


This data is obtained through optical character recognition (OCR) using a camera operated by blind individuals. Due to variations in capturing conditions and text complexities, the data may contain inconsistencies or inaccuracies. However, it holds valuable information that can be explored and understood with the help of contextual analysis and interpretation.

OCR technology enables blind individuals to access printed materials and documents by converting them into digital text. Although the captured text may lack formatting or perfect alignment, it opens avenues for blind users to engage with textual content through alternative means.

Interpreting the Meaning:

1. Contextual Analysis: To understand the data, consider the context in which it was captured. Explore the environment, potential document types, or specific scenarios that may provide insights into the captured text's purpose.

2. Interpretive Approach: Instead of focusing solely on literal interpretations, adopt an interpretive approach. Identify key terms, patterns, and relationships to provide explanations or alternative descriptions that uncover the intended meaning behind the captured words.

3. Collaborative Efforts: Engage in collaborative discussions with blind individuals or experts familiar with OCR technology. By combining their expertise and insights, a more comprehensive understanding of the captured data can be achieved.

Please contribute your insights, interpretations, or clarifications to help unravel the meaning behind the captured text.

Let's embark on this meaningful journey together, embracing the challenges and opportunities presented by OCR-generated data from the perspective of blind individuals!


Text: {ocr_text}
"""

prompt = PromptTemplate(input_variables=["ocr_text"], template=template)
chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0),
    prompt=prompt,
    verbose=True,
    memory=ConversationBufferWindowMemory(k=2),
)

def process_image():
    while True:
        try:
            path = capture_image()
            speak("processing  captured image ")
            stdout = sys.stdout
            sys.stdout = io.StringIO()
            reader = easyocr.Reader(['en'])
            sys.stdout = stdout
            result = reader.readtext(path, detail=0, paragraph=True)
            if not result:
                speak("No text recognized, please capture the image again.")
                continue
            speak("Recognized Text")
            speak(result)

            if _approve(result):
                speak("Let's make more meaning out of that.")
                response_text = chatgpt_chain.predict(ocr_text=result)
                speak("Here you go. Results are:")
                speak(response_text)
                
                break
            else:
                speak("Let's try again.")
        except Exception as e:
            speak(f"An error occurred: {str(e)}")
            if _approve("Do you want to try again?"):
                continue
            else:
                break



