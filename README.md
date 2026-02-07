# Chat with PDF

Chat with your PDF documents: ask questions and get answers based only on the document content. The app loads a PDF, chunks it, embeds with OpenAI, stores it in a vector database (Chroma), and answers your questions using retrieved context.

## Prerequisites

- **Python 3.10+**
- **OpenAI API key**

## Setup

1. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key**  
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your-openai-api-key-here
   ```

## Running the app

1. Put your PDF in the project folder (or update `file_path` in `chat_pdf.py`).
2. Run:
   ```bash
   python chat_pdf.py
   ```
3. On first run the app loads the PDF, splits it into chunks, embeds them, and stores the index in `./chroma_db`.
4. Ask questions in the terminal; answers are based only on the PDF. Type `exit` to quit.

## Project structure

```
├── chat_pdf.py       # Main app: load PDF → chunk → embed → Chroma → Q&A
├── chroma_db/        # Vector store (created on first run)
├── requirements.txt
├── .env              # Your OPENAI_API_KEY (create this, not committed)
└── README.md
```

## Notes

- The index is saved in `chroma_db/`; later runs reuse it if you don’t change the PDF path.
- To use a different PDF, edit `file_path` in `chat_pdf.py`.
