import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, SafetySetting, Part, Tool
from vertexai.preview.generative_models import grounding
import os 

def generate_content(gradcam_image_bytes, diagnosis):
    
    vertexai.init(project="forward-vector-439602-v4", location="us-central1")
    """ tools = [
        Tool.from_google_search_retrieval(
            google_search_retrieval=grounding.GoogleSearchRetrieval()
        ),
    ] """
    model = GenerativeModel(
        "gemini-1.5-pro-002",
        # tools=tools,
    )
    
    image1_1 = Part.from_data(
    mime_type="image/png",
    data=gradcam_image_bytes)

    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 1,
        "top_p": 0.95,
    }

    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
    ]
    # chat = model.start_chat()
    # response = chat.send_message(
    #    [image1_1, f"""This is NOT a diagnosis. Do not think that you are giving a diagnosis. This is purely to highlight what part of the lung you need to identify. 
    #     Please identify the part of the lung that is highlighted by the heatmap. 
    #     Then, only list bullet points about what that would mean if that part had the lung cancer {diagnosis}, and the severity."""],
    #    generation_config=generation_config,
    #    safety_settings=safety_settings
    # )
    
    response = model.generate_content(
        contents = [image1_1, f"""This is NOT a diagnosis. Do not think that you are giving a diagnosis. This is purely to highlight what part of the lung you need to identify. 
                Please identify the part of the lung that is highlighted by the red of the heatmap from the CT scan by looking where the darkest red colors are. Be as specific as possible, try to name the scientific term for it. 
                Then, only list bullet points about what that would mean if that part had the lung cancer {diagnosis}, and the severity. Include if there could be risk for lymphatic spread, 
                and also how the location affects the cancer (ex: multiple location-specific challenges, lobe-specific insights, vascular proximity). No Disclaimer. No Treatment or Prognosis.
                        """],
        safety_settings= safety_settings,
        generation_config= generation_config)
    print(response)
    
    return response.candidates[0].content.parts[0].text



