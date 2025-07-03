# Mark Entry Automation System

This is a mark-entry automation tool built to help department staff avoid manual entry of student marks into Excel/Sheets. It uses OCR to extract register numbers, subject codes, and total marks from scanned front pages of answer booklets.

## ✳️ Features

- Upload single or multiple answer scripts (batch-wise)
- OCR extraction using Tesseract + OpenCV
- Manual selection of Semester and Exam Type (Internal 1, Internal 2, Model)
- PostgreSQL backend (compatible with Supabase)
- Download data in Excel format by filters
- Beginner-friendly and extensible project

---

## 🗂 Folder Structure
<pre lang="text"> ```text mark-entry-automation/ │ ├── app/ # Core Streamlit + OCR application │ ├── __init__.py │ ├── main.py # Streamlit app (UI + logic) │ ├── ocr.py # OCR + OpenCV preprocessing │ ├── parser.py # Parse structured data from OCR text │ ├── uploader.py # Single and batch upload logic │ ├── utils.py # Utility functions (e.g., validation, cleaning) │ └── config.py # Central config (e.g., subjects, sems) │ ├── database/ # PostgreSQL / Supabase logic │ ├── __init__.py │ ├── db_config.py # Connection to DB │ ├── models.py # Schema-like structures (subject, student, mark) │ ├── queries.py # Insert, fetch, update functions │ ├── data/ # Temporary user data (not pushed to GitHub) │ └── sample_uploads/ # 59 pages or single uploads go here │ ├── tests/ # Unit & component tests │ ├── test_ocr.py │ ├── test_parser.py │ └── test_queries.py │ ├── notebooks/ # (Optional) Jupyter notebooks for experimentation │ └── ocr_testing.ipynb │ ├── assets/ # Static files (logo, templates, sample scans) │ ├── logo.png │ └── test_sheet.jpg │ ├── .gitignore # Ignore cache, env, uploads, etc. ├── requirements.txt # Python dependencies ├── README.md # Project overview + instructions ├── .env.example # Sample env variables (DB creds) └── setup.sh # (Optional) Script to setup virtualenv + DB ``` </pre>
