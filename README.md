# 🤖 Chatbot Lokal dengan LangChain & Ollama

Chatbot ini menggunakan **LangChain** dan **LLM lokal** (melalui [Ollama](https://ollama.com)) untuk menjawab pertanyaan berdasarkan isi dokumen lokal seperti PDF. Semua proses berjalan **sepenuhnya offline**, tanpa internet, menjaga privasi dan keamanan data.

---

## ✨ Fitur Utama

- 🔒 **Privat & Offline**: Tidak memerlukan internet atau API eksternal.
- 📄 **Analisis Dokumen Lokal**: Chatbot dapat menjawab pertanyaan berdasarkan isi PDF.
- 🧠 **Model Bahasa Lokal**: Gunakan `llama3`, `mistral`, atau model lokal lain via Ollama.
- ⚡ **Performa Tinggi**: Menggunakan vectorstore Chroma untuk pencarian cepat.
- 🔧 **Modular & Extensible**: Mudah dikembangkan menjadi web UI atau agent lanjutan.

---

## 🏗️ Teknologi yang Digunakan

- Python 3.10+
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [Chroma VectorDB](https://www.trychroma.com/)
- `PyPDFLoader` (parser PDF)
- `RecursiveCharacterTextSplitter` (split dokumen)

---

## 📁 Struktur Proyek

