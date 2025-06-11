# Case Study – AI with Heterogeneous User Data

## 1. Strategi Penyatuan Data Pengguna

Untuk menyatukan data pengguna yang tersebar, saya akan menggunakan pendekatan **Entity Resolution**. Ini adalah proses menyatukan record yang merujuk ke entitas yang sama, meskipun datanya berbeda-beda.

Langkah-langkah:

- Normalisasi data (hapus spasi, lowercase, format tanggal)
- Gunakan **unique key combination** (misal: email + no HP + tanggal lahir)
- Terapkan **fuzzy matching** untuk nama yang mirip tapi tidak identik

## 2. Teknik untuk Menangani Data Tidak Terstruktur

Untuk data seperti chat, catatan, atau dokumen:

- Gunakan **NLP (Natural Language Processing)**
- Tools: spaCy, HuggingFace Transformers, atau Google Gemini/OpenAI API
- Teknik:
  - Named Entity Recognition (NER) untuk ambil entitas (nama, alamat, tanggal)
  - Text classification (untuk label preferensi/emosi)
  - Embedding + vector similarity (misal untuk menyamakan opini pengguna)

## 3. Menangani Nama yang Sama

Nama sama ≠ orang yang sama. Maka tidak hanya mengandalkan nama, tapi juga:

- Alamat email
- Nomor HP
- Riwayat transaksi / lokasi login
- Timestamp interaksi

Jika semuanya cocok atau mirip secara probabilistik, maka bisa diasumsikan orang yang sama. Bisa juga pakai model pembelajaran **probabilistik record linkage**.

## 4. Desain Model AI untuk Personalisasi

Model AI harus mampu memahami konteks pengguna:

- Buat **user profile vector** dari data mereka
- Gunakan **retrieval-augmented generation (RAG)** untuk personalisasi jawaban
- Buat segmentasi user otomatis (clustering, rule-based)

Teknologinya:

- Data pipeline: Apache Airflow / dbt
- Feature store: **Feast**
- Model: BERT / LLM custom fine-tuned
- API: FastAPI + **LangChain** untuk logic dan query ke knowledge base

Dengan semua itu, aplikasi AI bisa memberikan **personalized response**, seperti rekomendasi produk, prioritas layanan, atau auto-reply yang sesuai kepribadian pengguna.

---

## 📘 Glosarium

- **Entity Resolution**  
  Proses mengidentifikasi dan menyatukan data yang berasal dari berbagai sumber tetapi merujuk ke entitas yang sama.  
  Sumber: https://en.wikipedia.org/wiki/Record_linkage

- **Fuzzy Matching**  
  Teknik pencocokan data berdasarkan kemiripan, bukan persamaan persis.  
  Contoh tools: FuzzyWuzzy, RapidFuzz

- **NLP (Natural Language Processing)**  
  Cabang AI untuk memahami dan memproses bahasa manusia.  
  Sumber: https://en.wikipedia.org/wiki/Natural_language_processing

- **NER (Named Entity Recognition)**  
  Teknik untuk mengekstrak entitas seperti nama orang, organisasi, dan lokasi dari teks.  
  Sumber: https://spacy.io/usage/linguistic-features#named-entities

- **Embedding**  
  Representasi vektor dari teks untuk digunakan dalam model AI atau pencocokan semantik.  
  Sumber: https://jalammar.github.io/illustrated-word2vec/

- **Retrieval-Augmented Generation (RAG)**  
  Teknik yang menggabungkan pencarian informasi (retrieval) dengan generasi jawaban menggunakan LLM.  
  Sumber: https://huggingface.co/blog/rag

- **Feast**  
  Open source feature store untuk machine learning.  
  Sumber: https://feast.dev/

- **LangChain**  
  Framework untuk membangun aplikasi berbasis LLM yang kompleks.  
  Sumber: https://www.langchain.com/
