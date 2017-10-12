text_file = "test.txt"


def read_file(text_file):
    try:
        with open(text_file, "r") as handle:
            data = handle.read()
            return data

    except FileNotFoundError:
        return None


def single_word(text_file):

    with open("test.txt", "r") as handle:

        data = handle.read()
        counter = 0
        for word in data.split():
            if word == 'Python':
                counter += 1
                return counter


def line_number(text_file):
    with open(text_file, "r") as handle:
        data = handle.readlines()
        return data


def longest_number(text_file):
    with open("test.txt", "r") as handle:
        data = handle.read()
        results = []
        for x in data.split():
            word_length = len(x)
            if word_length == 16:
                word_length = x
                results.append(word_length)
