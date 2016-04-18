import random

def tetris_pieces():
    pieces = ["O", "I", "S", "Z", "L", "J", "T"]
    random.shuffle(pieces)
    return "".join(pieces)

def bag():
    output = ""
    while len(output) <= 50:
        output += tetris_pieces()
    return output[:50]

print(bag())
