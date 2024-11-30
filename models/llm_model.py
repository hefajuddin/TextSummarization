from transformers import pipeline

def get_summarization_model(model_name, device="cpu"):
    """Load a pre-trained summarization model."""
    return pipeline("summarization", model=model_name, device=0 if device == "cuda" else -1)