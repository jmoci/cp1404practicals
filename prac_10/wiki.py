"""This module includes a program to get a wikipedia summary based on a user prompt."""


import wikipedia


def main():
    prompt = input("Enter page title: ")
    while prompt != "":
        try:
            result = wikipedia.page(prompt,auto_suggest=False)
            print(result.title)
            print(result.summary)
            print(result.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("we need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError as e:
            print(f"Page id \"{prompt}\" does not match any pages. Try another id!")
        prompt = input("Enter page title: ")
    print("Thank you.")
if __name__ == '__main__':
    main()