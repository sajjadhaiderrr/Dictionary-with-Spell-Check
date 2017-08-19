import json
from difflib import get_close_matches


# Load definitions
data = json.load(open("data.json"))

def dictionary(word):
    # print def if word in data
    if word in data:
        # Check if multiple definitions for word
        if type(data[word]) == list:
            for definition in data[word]:
                print(definition)
        else:
            print(data[word])
    # Get closest match for incorrectly typed word
    elif len(get_close_matches(word, data.keys())) > 0:
        suggestion = get_close_matches(word, data.keys())[0]
        print("Did you mean %s instead?" %suggestion)
        decision = input("Y or N: ")
        if decision == "Y":
            dictionary(suggestion)
        else:
            print("Are you sure the word is correct?")

    else:
        print("Are you sure the word is correct?")

word = input("Enter a word: ").lower()
dictionary(word)
