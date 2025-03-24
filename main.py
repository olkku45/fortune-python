import random

with open("quotes.txt", "r") as file:
    w_newline = [line.rstrip('\n') for line in file]


def split_file_into_chunks(file): 
    quotes = [""]

    for line in file:
        if line != "%":
            if quotes[-1]:
                quotes[-1] += " "
            quotes[-1] += line
        
        else:
            quotes.append("")

    return quotes


quotes = split_file_into_chunks(w_newline)


def get_random_quote(quotes):
    return random.choice(quotes)


if __name__ == "__main__":
    print(get_random_quote(quotes)) 
