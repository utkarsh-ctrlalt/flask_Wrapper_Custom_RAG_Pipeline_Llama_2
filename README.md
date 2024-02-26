# flask_Wrapper_Custom_RAG_Pipeline_Llama_2
 A Flask-based REST API serves a customized RAG pipeline powered by the Llama 2 LLM model.

# Running this service as a Docker Container
 ## docker run command - 
    sudo docker run -d --runtime=nvidia --gpus all -p 8502:8502 --name {container_name} {image_name}

 ### <b>NOTE:</b> If you have downloaded the Llama 2-7b-chat-hf locally, update the config.py file according to the comments in that script.
 