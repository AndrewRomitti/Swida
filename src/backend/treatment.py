import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, SafetySetting, Part, Tool
from vertexai.preview.generative_models import grounding
import os 

def generate_content(diagnosis):
    
    vertexai.init(project="forward-vector-439602-v4", location="us-central1")
    """ tools = [
        Tool.from_google_search_retrieval(
            google_search_retrieval=grounding.GoogleSearchRetrieval()
        ),
    ] """
    model = GenerativeModel(
        "gemini-1.5-flash-002",
        # tools=tools,
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

    response = model.generate_content(
        contents = f"""Based on the diagnosis: {diagnosis}, provide a 1 paragraph explanation of the disease
                        a 5 bullet point list of potential causes and a list and explanation of 5 different treatments.
                        
                        Structure it like this:
                        
                        Explanation:
                        Causes:
                        Treatments:""",
        safety_settings= safety_settings,
        generation_config= generation_config)
    return response

print(generate_content("Large Cell Carcinoma"))
        
