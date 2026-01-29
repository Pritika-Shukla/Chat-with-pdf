## chat with pdf  (RAG)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
file_path="./Pritika-Shukla .pdf"
loader = PyPDFLoader(file_path)

document=loader.load()
document[0]

text_splitter=CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0
    )
texts = text_splitter.split_documents(document)

embeddings=OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("✅ Stored chunks:", vectorstore._collection.count())

query = "What is Pritika's current comapny name?"
docs = vectorstore.similarity_search(query, k=3)

print("\n--- TOP MATCH ---\n")
print(docs[0].page_content)
print("\nMetadata:", docs[0].metadata)
