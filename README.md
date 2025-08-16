# Swida

This was Daniel Achacon and Andrew Romitti's submission to AI ATL

## What it is
Swida is an AI tool that aims to assist doctors in the lung cancer diagnosing process and patients in being more informed about lung cancer information. The app starts with classifying a CT scan of the lungs and then uses a Data Efficient Image Transformer to classify the lung as either normal or as one of 3 types of lung cancer. Following this, the model returns a Gradient Classification Activation Map in order to visualize its output, and that heatmap is then fed into Google Gemini-1.5-pro-002 where it explains where on the lung the AI is focusing on and what that means for the patient. Next, we use Google Gemini-1.5-flash-002 with the Google grounding feature to give potential treatment plans and a list of cutting-edge research papers related to the cancer they were diagnosed with. Thus, Swida enables both patients and doctors to engage in proactive, informed discussions about health options. Ultimately, we produced a tool that enhances healthcare diagnostics through its advanced image analysis.

## How we built it
We used React, HTML, CSS, Javascript & NodeJS to build the front end, and Flask for the backend. Kaggle was used for the dataset, and we used Google Colab to train a HuggingFace DeIT on a GPU and also for training the Resnet50 that was used for the GradCAM predictions. We used the NCBI Entrez Programming Utilities (E-utilities) API to scrape research papers and their information from the PubMed Database and pandas to process and clean the information. Finally, we used the Gemini API & VertexAI to develop the LLM capabilities of our software.

Demo video: https://www.youtube.com/watch?v=AGEKlWcHaS4&t=2s
