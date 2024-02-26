import os
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]

hf_token = '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'
# Uncomment the below line if you have locally downloaded Llama-2-7b-chat-hf LLM model.
#summerizer_model_id = os.path.join(ROOT, "Llama-2-7b-chat-hf")

# Comment this line if you have uncommented line 12 and using local Llama-2-7b-chat-hf LLM model.
# Downloads model from web and stores it in your local system cache.

summerizer_model_id = "meta-llama/Llama-2-7b-chat-hf"

store_dir_path = os.path.join(ROOT, "chroma_db" )
TEXT_SPLITTER_CHUNK = 1000
TEXT_CHUNK_OVERLAP = 50
prompt_template = ''' You are a chatbot which provides detailed answers with explanation to the user's question. Give a lengthy answer.

    Context:
    {context}

    Question:
    {question}

    Answer:
    ''' 


prompt_template_without_rag = ''' You are a chatbot which provides detailed answers with explanation to the user's question.  

    Question:
    {question}

    Answer:
    ''' 
