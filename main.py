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
    quote_index = random.randint(1, len(quotes) + 1)

    return quotes[quote_index]


if __name__ == "__main__":
    print(get_random_quote(quotes)) 
