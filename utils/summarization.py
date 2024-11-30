def summarize_text(model, text, max_input_length, max_output_length):
    """Generate a summary for a given text."""
    if len(text) > max_input_length:
        text = text[:max_input_length]
    
    summary = model(text, max_length=max_output_length, min_length=30, do_sample=False)
    return summary[0]['summary_text']