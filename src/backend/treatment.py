import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, SafetySetting, Part, Tool
from vertexai.preview.generative_models import grounding
import os 

def generate_content(diagnosis):
    
    vertexai.init(project="forward-vector-439602-v4", location="us-central1")
    tools = [
        Tool.from_google_search_retrieval(
            google_search_retrieval=grounding.GoogleSearchRetrieval()
        ),
    ] 
    model = GenerativeModel(
        "gemini-1.5-flash-002",
        tools=tools,
    )

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

    if diagnosis == "Normal":
        response = model.generate_content(
            contents = f""" Provide a 1 paragraph explanation of various lung cancer and only 3 bullet points of general ways to prevent lung cancer.
                            In the paragraph explanation, always include what contributes to risk and who/what is strongly connected to lung cancer. No Disclaimer.
                            """,
            safety_settings= safety_settings,
            generation_config= generation_config)
    else:
        response = model.generate_content(
            contents = f"""Based on the diagnosis: {diagnosis}, provide only a list and explanation of only 3 different treatments. Include 
                            risks and side effects, treatment goals and expectations, potential/average duration and cost of treatment, impact on daily life. No Disclaimer.
                            """,
            safety_settings= safety_settings,
            generation_config= generation_config)
        
    return response.candidates[0].content.parts[0].text