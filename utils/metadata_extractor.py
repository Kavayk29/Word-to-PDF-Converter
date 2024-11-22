from docx import Document

def extract_metadata(docx_path):
    """Extracts metadata from a Word document using python-docx."""
    doc = Document(docx_path)
    metadata = {}
    
    # Extract document properties (metadata)
    core_props = doc.core_properties
    metadata["Author"] = core_props.author
    metadata["Title"] = core_props.title
    metadata["Subject"] = core_props.subject
    metadata["Keywords"] = core_props.keywords
    metadata["Last Modified By"] = core_props.last_modified_by
    metadata["Created"] = core_props.created
    metadata["Modified"] = core_props.modified
    metadata["Content Status"] = core_props.content_status
    
    return metadata
from docx import Document

def extract_metadata(docx_path):
    """Extracts metadata from a Word document using python-docx."""
    doc = Document(docx_path)
    metadata = {}
    
    # Extract document properties (metadata)
    core_props = doc.core_properties
    metadata["Author"] = core_props.author
    metadata["Title"] = core_props.title
    metadata["Subject"] = core_props.subject
    metadata["Keywords"] = core_props.keywords
    metadata["Last Modified By"] = core_props.last_modified_by
    metadata["Created"] = core_props.created
    metadata["Modified"] = core_props.modified
    metadata["Content Status"] = core_props.content_status
    
    return metadata
