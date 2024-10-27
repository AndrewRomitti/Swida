from Bio import Entrez
from Bio.Medline import parse
import pandas as pd
from io import StringIO

def fetch_pubmed_data(email, search_term, retmax):
    Entrez.email = email
    print(search_term)
    handle = Entrez.esearch(db="pubmed", term=search_term, retmax=retmax, sort="pub_date")
    record = Entrez.read(handle)
    handle.close()

    idlist = record["IdList"]

    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
    records = handle.read()
    handle.close()

    records = parse(StringIO(records))

    columns = ["PMID", "Abstract", "Publication Date", "Article ID", "E-Publication Date", "Language", "Link"]
    df = pd.DataFrame(columns=columns)

    for record in records:
        pmid = record.get("PMID", "N/A")
        language = record.get("LA", ["N/A"])
        
        if "eng" in language:
            new_row = {
                "PMID": pmid,
                "Title": record.get("TI", "N/A"),
                "Abstract": record.get("AB", "N/A"),
                "Publication Date": record.get("DP", "N/A"),
                "Article ID": ", ".join(record.get("AID", ["N/A"])),
                "E-Publication Date": record.get("DEP", "N/A"),
                "Language": ", ".join(language),
                "Link": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" 
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    return df

import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, SafetySetting, Part, Tool
from vertexai.preview.generative_models import grounding
import os 

def generate_content(diagnosis, df):
    
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
    
    random_articles = df.sample(n=3)

    responses = []
    for ind, article in random_articles.iterrows():
        response = model.generate_content(
            contents = f"""Provide a 1 or 2 sentence key finding from the following abstract with title {article["Title"]}.
                            In one sentence after, explain how the article is useful for lung cancer patient.
                            Structure your response as:
                            
                            Title: {article["Title"]} (Bold this)
                            - Key Finding: (Enter Key Finding)
                            - Link: {article["Link"]} (Format this to link to url)
                            - Date: {article["Publication Date"]}
                            """,
            safety_settings= safety_settings,
            generation_config= generation_config)
        responses.append(response.candidates[0].content.parts[0].text)
    
    return responses

def getEducationalResources(diagnosis):
    email = "e.danielachacon@gmail.com"
    if diagnosis == "Normal":
        search_term = "Lung Cancer Screening and Prevention"
    else:
        search_term = diagnosis + " Lung Cancer"
    retmax = 50

    pubmed_data = fetch_pubmed_data(email, search_term, retmax)
    return generate_content(diagnosis, pubmed_data)