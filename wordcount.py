import string
import re


def word_count(stories):
    if type(stories) == list:
        return [split_sentence(story) for story in stories]
    elif type(stories) == str:
        print(split_sentence(stories))


def split_sentence(sentence):
    words = remove_splchar(sentence.lower()).split()
    return {word: words.count(word) for word in sorted(set(words))}


def remove_splchar(words):
    return re.sub('[' + string.punctuation + ']', '', words)