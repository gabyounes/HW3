import requests
import string

# Book details
link1 = "https://www.gutenberg.org/cache/epub/84/pg84.txt"
author1 = "Mary Shelley"
book1 = "Frankenstein"

link2 = "https://www.gutenberg.org/cache/epub/345/pg345.txt"
author2 = "Oscar Wilde"
book2 = "The Picture of Dorian Gray"

def get_unique_words(link):
    """Fetches the book text from the link and counts unique words."""
    try:
        response = requests.get(link, timeout=10)  # Timeout for stability
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    except requests.RequestException as e:
        print(f"Error fetching the book from {link}: {e}")
        return {}

    unique_words = {}
    translator = str.maketrans("", "", string.punctuation)  # Remove all punctuation

    for line in response.text.splitlines():
        words = line.translate(translator).split()  # Remove punctuation and split words
        for word in words:
            word = word.lower()
            unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words

def compare_books(link1, author1, book1, link2, author2, book2):
    """Compares the unique words used by two different authors."""
    words1 = get_unique_words(link1)
    words2 = get_unique_words(link2)

    unique_count1 = len(words1)
    unique_count2 = len(words2)

    print(f"{author1} used {unique_count1} unique words in '{book1}'.")
    print(f"{author2} used {unique_count2} unique words in '{book2}'.")

    if unique_count1 > unique_count2:
        print(f"{author1} used more unique words than {author2} in '{book1}'.")
    elif unique_count2 > unique_count1:
        print(f"{author2} used more unique words than {author1} in '{book2}'.")
    else:
        print(f"Both authors used the same number of unique words.")

# Call function with corrected arguments
compare_books(link1, author1, book1, link2, author2, book2)