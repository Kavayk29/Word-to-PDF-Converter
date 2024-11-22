Overview
This project is a Streamlit-based web application that allows users to upload Word documents (.docx), convert them into PDF files, view their metadata, and optionally apply password protection to the generated PDFs. The application is designed to streamline document conversion and provide enhanced security features.

Features
Upload Word Documents: Supports .docx files for upload.
View Metadata: Extracts and displays metadata from the uploaded Word document (e.g., author, title, creation date, etc.).
Convert to PDF: Converts Word documents to PDF format using Pandoc.
Password Protection: Optionally apply a password to the generated PDF for added security.
Download PDFs: Provides a download link for both protected and unprotected PDFs.

Technology Stack-

Python Libraries:
streamlit: Web application framework.
python-docx: Extract metadata from Word documents.
PyPDF2: Add password protection to PDFs.

Conversion Tool:
Pandoc: Used for converting .docx files to .pdf.
Other Utilities:
os: File and directory management.
subprocess: For running external commands.
