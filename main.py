from lorem_text import lorem
import tiktoken

def tokenize(text_string: str, used_model: str) -> int:
    """tokenize the input string according to the model used

    Args:
        text_string (str): input string

    Returns:
        int: amount of tokens the input text encodes in.
    """    
    enc = tiktoken.encoding_for_model(used_model)
    return len(enc.encode(text_string))

def main():
    data = {"150": 10465, "250": 18038, "350": 27405}  
    print(f"""{"rows":<5}: amount of tokens""")
    
    for key, count in data.items():
        text = lorem.words(count)
        print(f"{key:<5}: {tokenize(text, "gpt-4o")}")
      


if __name__ == "__main__":
    main()
