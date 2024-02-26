from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import config

if __name__ == "__main__":

    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=config.TEXT_SPLITTER_CHUNK,
        chunk_overlap=config.TEXT_CHUNK_OVERLAP,
        length_function=len,
    )

    web_link = "/home/usingh4/Desktop/llm_2/ConceptsofBiology-WEB.pdf"
    loader = PyPDFLoader(web_link)
    pages = loader.load_and_split(text_splitter=text_splitter)
    print(pages[2000])



    



    # hf_embedding = HuggingFaceInstructEmbeddings()

    # print('starting creating persistant vector store')
    # db = Chroma.from_documents(pages, hf_embedding,  persist_directory="./chroma_db")
    # db.persist()


    # print("Done")
