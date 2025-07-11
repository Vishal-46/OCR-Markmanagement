# app/ui.py
import streamlit as st
st.set_page_config(page_title="Mark Entry Automation", layout="wide")
# -------- SIDEBAR --------
st.sidebar.header("Upload Configuration")
semester = st.sidebar.selectbox("Semester", list(range(1, 9)))
exam_type = st.sidebar.selectbox("Exam Type", ["Internal 1", "Internal 2", "Model"])

uploaded = st.sidebar.file_uploader(
    "Upload scanned front pages",
    type=["jpg", "jpeg", "png", "pdf"],
    accept_multiple_files=True
)
if st.sidebar.button(" Process"):
    st.session_state["clicked"] = True
st.sidebar.markdown("---")
st.sidebar.header(" Download Data")
with st.sidebar.expander("Available formats"):
    st.button("Excel (coming soon)", disabled=True)
    st.button("PDF (coming soon)", disabled=True)

# -------- MAIN AREA --------
st.title(" Mark Entry Automation")

if "clicked" not in st.session_state or not uploaded:
    st.info("👈 Use the sidebar to choose semester/exam and upload files.")
else:
    st.success(f"{len(uploaded)} file(s) queued for processing.")
    st.warning("OCR & database insertion not wired yet – UI only.")
    st.empty()  # placeholder where a dataframe will appear later
    