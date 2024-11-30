from transformers import pipeline
import torch

def get_summarization_model(model_name, device="cpu"):
    """Load a pre-trained summarization model."""
    if device == "cuda" and not torch.cuda.is_available():
        print("Warning: CUDA device specified, but no GPU is available. Falling back to CPU.")
        device = "cpu"
    return pipeline("summarization", model=model_name, device=0 if device == "cuda" else -1)