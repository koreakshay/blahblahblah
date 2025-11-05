def get_num_words(text):
    return len(text.split())


def sort_on(items):
    return items["num"]

def get_char_count(text):
    text_lower = text.lower()
    counts = {}
    for char in text_lower:
        counts[char] = counts.get(char,0) + 1
    return counts
