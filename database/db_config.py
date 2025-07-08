# database/supabase_client.py
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_API_KEY")

try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    print(" Supabase client initialized successfully!")

    # Fetch 5 rows from students to test
    response = supabase.table("students").select("*").limit(5).execute()
    print(" Sample data from students table:", response.data)

except Exception as e:
    print(" Connection failed:", e)
