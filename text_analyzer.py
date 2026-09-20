from collections import Counter


def read_file(file_name):
    """Read a text file and return its contents as a string."""
    with open(file_name, "r") as file:
        return file.read()


def get_words(text):
    """Convert text to lowercase and return a list of words."""
    return text.lower().split()


def count_words(words):
    """Count how many times each word appears."""
    return Counter(words)


def find_long_words(words):
    """Return a list of words with more than three characters."""
    return [word for word in words if len(word) > 3]


def display_results(words, word_counts, long_words):
    """Display the text analysis results."""
    print(f"Total number of words: {len(words)}")
    print(f"Unique words count: {len(word_counts)}")

    print("Most frequent words:")
    for word, count in word_counts.most_common(5):
        print(f"'{word}': {count}")

    print(f"Long words (more than 3 characters): {len(long_words)}")


def analyze_text(file_name):
    """Analyze a text file and display word statistics."""
    text = read_file(file_name)
    words = get_words(text)
    word_counts = count_words(words)
    long_words = find_long_words(words)

    display_results(words, word_counts, long_words)


if __name__ == "__main__":
    analyze_text("sample.txt")