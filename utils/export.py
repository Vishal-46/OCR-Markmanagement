import pandas as pd
import io
from fpdf import FPDF

def generate_excel(df):
    output = io.BytesIO()
    df.to_excel(output, index=False, engine='openpyxl')
    output.seek(0)
    return output.read()

def generate_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for i, row in df.iterrows():
        line = f"{row['register_number']} - {row['name']} - {row['subject_code']} - {row['mark']}"
        pdf.cell(200, 10, txt=line, ln=1)

    output = io.BytesIO()
    pdf.output(output)
    return output.getvalue()
 