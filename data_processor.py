#The given code were taken snippet from AI chatbot purely for learning purpose

# data_processor.py
# Real-world snippet: Preprocessing raw dataset for AI/ML models


def clean_missing_values(data):
    """Filter out null or missing entries from a raw feature list."""
    cleaned = [item for item in data if item is not None and item != ""]
    return cleaned


if __name__ == "__main__":
    raw_dataset = ["feature_1", None, "feature_2", "", "feature_3"]
    print("Raw Data:", raw_dataset)

    processed_data = clean_missing_values(raw_dataset)
    print("Cleaned Data:", processed_data)