from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import config
from pathlib import Path
import os

# Define the path of the current file and its root directory
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]


if __name__ == "__main__":

    # Initialize a RecursiveCharacterTextSplitter object with specified parameters in config.py
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.TEXT_SPLITTER_CHUNK,
        chunk_overlap=config.TEXT_CHUNK_OVERLAP,
        length_function=len,
    )

    # Define the path or web link to the PDF document
    web_link = os.path.join(ROOT, "ConceptsofBiology-WEB.pdf" )
    # Initialize a PyPDFLoader object with the PDF document path or link
    loader = PyPDFLoader(web_link)
    # Load and split the PDF document into pages using the specified text splitter
    pages = loader.load_and_split(text_splitter=text_splitter)
    # print(type(pages))

    # Initialize a HuggingFaceInstructEmbeddings object
    hf_embedding = HuggingFaceInstructEmbeddings()

    # Inform about the start of the process.
    print('starting creating persistant vector store')
    # Create a Chroma vector store from the loaded document pages using Hugging Face intruct embeddings model.
    db = Chroma.from_documents(pages, hf_embedding,  persist_directory="./chroma_db")
    # Persist the created vector store.
    db.persist()

    # Inform about the completion of the process.
    print("Done")
