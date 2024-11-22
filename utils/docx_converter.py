import os
import subprocess
from utils.exception_handler import MetadataExtractionError

def docx_to_pdf(docx_path, pdf_path):
    """Converts a DOCX file to PDF using Pandoc."""
    try:
        # Use Pandoc to convert DOCX to PDF
        result = subprocess.run(
            ['pandoc', docx_path, '-o', pdf_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return pdf_path
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error during conversion: {e.stderr.decode('utf-8')}")
