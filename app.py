import os
import streamlit as st
from utils.docx_converter import docx_to_pdf
from utils.metadata_extractor import extract_metadata
from utils.exception_handler import log_exception, MetadataExtractionError
from PyPDF2 import PdfReader, PdfWriter

# Directories for uploads and converted PDFs
UPLOAD_FOLDER = "uploads"
CONVERTED_FOLDER = "converted"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

# Streamlit Web Application
st.title("Word to PDF Converter with Metadata Viewer and Password Protection")
st.write("Upload a Word document (.docx), and we'll convert it to a PDF for you and show its metadata!")

# File uploader section
uploaded_file = st.file_uploader("Choose a Word document", type=["docx"])

if uploaded_file:
    # Save uploaded file to the uploads directory
    docx_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(docx_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"Uploaded: {uploaded_file.name}")

    # Extract and display metadata
    try:
        metadata = extract_metadata(docx_path)
        st.subheader("File Metadata")
        for key, value in metadata.items():
            st.write(f"**{key}**: {value}")
    except MetadataExtractionError as e:
        st.error(str(e))
        log_exception(e, "Metadata Extraction")

    # Convert DOCX to PDF
    pdf_filename = os.path.splitext(uploaded_file.name)[0] + ".pdf"
    pdf_path = os.path.join(CONVERTED_FOLDER, pdf_filename)

    try:
        converted_pdf_path = docx_to_pdf(docx_path, pdf_path)
        if converted_pdf_path:
            st.success("Conversion Successful!")

            # Ask the user if they want to password-protect the PDF
            protect_pdf = st.checkbox("Password protect the PDF")

            if protect_pdf:
                # Ask for a password input from the user
                password = st.text_input("Enter a password for the PDF", type="password")

                # If password is entered, apply it to the PDF
                if password:
                    # Open the converted PDF
                    with open(converted_pdf_path, "rb") as f:
                        reader = PdfReader(f)
                        writer = PdfWriter()

                        # Add all pages to the writer
                        for page in reader.pages:
                            writer.add_page(page)

                        # Apply password protection
                        writer.encrypt(password)

                        # Save the protected PDF
                        protected_pdf_path = os.path.join(CONVERTED_FOLDER, f"protected_{pdf_filename}")
                        with open(protected_pdf_path, "wb") as output_pdf:
                            writer.write(output_pdf)

                        # Provide a download link for the protected PDF
                        with open(protected_pdf_path, "rb") as f:
                            st.download_button(
                                label="Download Protected PDF",
                                data=f,
                                file_name=f"protected_{pdf_filename}",
                                mime="application/pdf"
                            )

            else:
                # Provide a download link for the unprotected PDF
                with open(converted_pdf_path, "rb") as f:
                    st.download_button(
                        label="Download PDF",
                        data=f,
                        file_name=pdf_filename,
                        mime="application/pdf"
                    )

        else:
            st.error("There was an error during the conversion.")
    except Exception as e:
        st.error(f"Conversion failed: {str(e)}")
        log_exception(e, "PDF Conversion")
