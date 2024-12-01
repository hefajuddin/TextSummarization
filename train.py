# from utils.data_loader import load_data
from models.llm_model import get_summarization_model
from utils.summarization import summarize_text
from config import CONFIG

def main():
    # Load data
    # data = load_data("data/sample_texts.json")
    while True:
        data=input("Input your text detail that expect to summarize: ")
        if data !="":
            break

    # Load model
    model = get_summarization_model(CONFIG["model_name"], CONFIG["device"])
    
    # Perform summarization
    # for item in data:
    # text = item["content"]
    text = data
    summary = summarize_text(model, text, CONFIG["max_input_length"], CONFIG["max_output_length"])
    # print(f"Original Text: {text}")
    print(f"Summary: {summary}\n")

if __name__ == "__main__":
    main()