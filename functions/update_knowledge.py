from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os


load_dotenv()

def update_knowledge(file):
    try:
        # extract the knowledge from pdf file
        knowledge_text = ""
        reader = PdfReader(file)
        for page in reader.pages:
            knowledge_text += page.extract_text()

        # check the knowledge has been extracted
        print(knowledge_text)


        # split the knowledge into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len
        )

        # create the documents from knowledge chunk
        docs = text_splitter.create_documents([knowledge_text])
        print(len(docs))

        # load embedding model
        embedding_model = OpenAIEmbeddings(
            model=os.getenv("OPENAI_EMBEDDING_MODEL"),
            api_key=os.getenv("OPENAI_API_KEY")
        )

        # initialize pinecone api key
        os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")

        # create pinecone vector store to store the knowledge
        db = PineconeVectorStore.from_documents(
            documents = docs,
            embedding = embedding_model,
            index_name = os.getenv("PINECONE_INDEX_NAME")
        )
        print("Knowledge updated!")
        return db
    

    except Exception as e:
        print("error: ", str(e))



