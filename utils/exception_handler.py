class MetadataExtractionError(Exception):
    """Custom exception for metadata extraction errors."""
    pass

def log_exception(e, context=""):
    """Logs exceptions for debugging."""
    print(f"Exception in {context}: {str(e)}")
