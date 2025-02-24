from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
import os
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=200,
)

loader = Docx2txtLoader('./Information.docx')
document_list = loader.load_and_split(text_splitter=text_splitter)



# 환경변수를 불러옴
load_dotenv()

# OpenAI에서 제공하는 Embedding Model을 활용해서 `chunk`를 vector화
embedding = OpenAIEmbeddings(model='text-embedding-3-large')




index_name = 'lee-index'
pinecone_api_key = os.environ.get("PINECONE_API_KEY")
pc = Pinecone(api_key=pinecone_api_key)


database = PineconeVectorStore.from_documents(document_list, embedding, index_name=index_name)