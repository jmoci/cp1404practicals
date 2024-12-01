"""This module includes a program to get a wikipedia summary based on a user prompt."""


import wikipedia


def main():
    prompt = input("Enter page title: ")
    while prompt != "":
        result = wikipedia.search(prompt)[0]
        try:
            print(wikipedia.summary(result,auto_suggest = False))
        except wikipedia.exceptions.DisambiguationError as e:
            print("we need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        prompt = input("Enter page title: ")

if __name__ == '__main__':
    main()