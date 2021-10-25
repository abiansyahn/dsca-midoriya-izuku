from random import sample

def generate_password(n_token=3):
    """Generate lower case password from word.txt
    
    Args:
        n_token (int): number of token to be included
            in password
            
    Returns:
        str: password
    """
    with open("words.txt", "r") as f:
        word_list = f.read().split("\n")
    tokens = sample(word_list, k=n_token)
    return "".join(tokens).lower()